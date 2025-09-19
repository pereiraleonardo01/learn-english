from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.utils.text import slugify
from dotenv import load_dotenv
from .models import Word, Phrase, SiteConfig
import requests
import io


def home(request):
    return render(request, 'index.html')


def get_ultils():
    config = SiteConfig.objects.first()

    return {
        "key": config.speech_api_key if config else None,
        "region": config.speech_api_region if config else None,
    }


def reading(request):
    phrase = request.GET.get('phrase')
    if not phrase:
        return JsonResponse({'error': 'Frase não recebida'}, status=400)

    load_dotenv()
    dados = get_ultils()
    subscription_key = dados['key']
    region = dados['region']

    if not subscription_key or not region:
        return JsonResponse({'error': 'Configuração da API não encontrada'}, status=500)

    url = f"https://{region}.tts.speech.microsoft.com/cognitiveservices/v1"
    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "audio-16khz-32kbitrate-mono-mp3",
        "User-Agent": "PythonTTSClient"
    }

    ssml = f"""
    <speak xmlns="http://www.w3.org/2001/10/synthesis"
        xmlns:mstts="http://www.w3.org/2001/mstts"
        version="1.0" xml:lang="en-US">
        <voice name="en-US-BrianMultilingualNeural">
            <mstts:express-as style="general">
                <prosody rate="5%" pitch="2%">
                    {phrase}
                </prosody>
            </mstts:express-as>
        </voice>
    </speak>
    """

    response = requests.post(url, headers=headers, data=ssml)
    if response.status_code == 200:
        file_temp = io.BytesIO(response.content)
        return FileResponse(file_temp, content_type='audio/mpeg')

    else:
        print("Erro:", response.text)
        return JsonResponse({'error': 'Erro ao gerar áudio'}, status=500)


@csrf_exempt
def play_audio(request):
    if request.method == 'POST':
        phrase = request.POST.get('phrase')
        if phrase:
            reading(phrase)
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Frase vazia'})
    return JsonResponse({'status': 'error', 'message': 'Método inválido'})


def add_phrase(request):
    return render(request, "add_phrases.html")


def add_word_phrases(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        word = request.POST.get('word')
        phrase = request.POST.get('phrase')
        explanation = request.POST.get('explanation')

        # Validação simples (opcional)
        if not type or not word or not phrase:
            messages.error(request, 'Preencha todos os campos obrigatórios.')
        else:
            # Cria ou recupera a word
            word_obj, created = Word.objects.get_or_create(
                word=word,
                defaults={'type': type}
            )

            # Cria a phrase associada
            Phrase.objects.create(
                word=word_obj,
                phrase=phrase,
                explanation=explanation,
                slug=slugify(f"{phrase}")
            )

            messages.success(request, 'Frase adicionada com sucesso!')
            return redirect('add_word_phrases')

    # Frases salvas para exibir na página
    latest_phrases = Phrase.objects.order_by('-id')[:5]

    return render(request, 'add_phrases.html', {
        'latest_phrases': latest_phrases
    })


def detailed_phrase(request, word, phrase_id, slug):
    word_obj = get_object_or_404(Word,  word=word)
    detailed = get_object_or_404(
        Phrase, id=phrase_id, slug=slug, word=word_obj)
    context = {
        "detailed": detailed
    }

    return render(request, 'detailed.html', context)

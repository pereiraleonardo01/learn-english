from django import forms
from .models import Word, Phrase


class WordPhraseForm(forms.Form):
    word = forms.CharField(max_length=100, label="Palavra")
    type = forms.ChoiceField(choices=Word._meta.get_field(
        'type').choices, label="Tipo gramatical")
    phrase = forms.CharField(max_length=255, label="Frase", widget=forms.TextInput(
        attrs={'placeholder': 'Frase completa'}))
    explanation = forms.CharField(label="Explicação", widget=forms.Textarea(
        attrs={'placeholder': 'Explicações sobre a frase...'}))


# class PhraseForm(forms.ModelForm):
#     class Meta:
#         model = Phrase
#         fields = ['type', 'word', 'phrase', 'explanation']
#         widgets = {
#             'type': forms.RadioSelect,
#             'word': forms.TextInput(attrs={'placeholder': 'Palavra-chave'}),
#             'phrase': forms.TextInput(attrs={'placeholder': 'Frase completa'}),
#             'explanation': forms.Textarea(attrs={'placeholder': 'Explicações sobre a frase...'}),
#         }


class WordPhraseForm(forms.Form):
    word = forms.CharField(max_length=100, label="Palavra")

    type = forms.ChoiceField(
        choices=[
            ('substantivo', 'Substantivo'),
            ('verbo', 'Verbo'),
            ('adjetivo', 'Adjetivo'),
        ],
        widget=forms.RadioSelect
    )

    phrase = forms.CharField(max_length=255, label="Frase", widget=forms.TextInput(
        attrs={'placeholder': 'Frase completa'}))
    explanation = forms.CharField(label="Explicação", widget=forms.Textarea(
        attrs={'placeholder': 'Explicações sobre a frase...'}))

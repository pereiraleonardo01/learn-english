from django.contrib import admin
from django.urls import path
from Learning_English.views import home, reading, add_word_phrases, detailed_phrase
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('tts', reading, name='reading'),
    path('adicionar-frases/', add_word_phrases, name='add_word_phrases'),
    path('frase/<str:word>/<slug:slug>/<int:phrase_id>/',
         detailed_phrase, name="detailed_phrase"),
]

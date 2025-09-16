from django.contrib import admin
from django.urls import path
from Learning_English.views import home, reading, add_word_phrases
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('tts', reading, name='reading'),
    path('adicionar-frases/', add_word_phrases, name='add_word_phrases'),
]

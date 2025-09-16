from django.contrib import admin
from .models import Word, Phrase, SiteConfig


admin.site.register(Word)
admin.site.register(Phrase)
admin.site.register(SiteConfig)

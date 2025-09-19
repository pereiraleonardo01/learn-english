from django.db import models
from django.utils.text import slugify


class Word(models.Model):
    word = models.CharField(max_length=100, unique=True)

    type = models.CharField(max_length=20, choices=[
        ('substantivo', 'Substantivo'),
        ('verbo', 'Verbo'),
        ('adjetivo', 'Adjetivo'),
    ])

    def __str__(self):
        return f"{self.word} ({self.get_type_display()})"


class Phrase(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    phrase = models.CharField(max_length=255)
    explanation = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.phrase}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.phrase


class SiteConfig(models.Model):
    name = models.CharField(max_length=100, default="Configuração Geral")
    speech_api_key = models.CharField(max_length=255)
    speech_api_region = models.CharField(max_length=255)

    def __str__(self):
        return self.name

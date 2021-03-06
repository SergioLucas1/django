from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(satus='publicado')

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='rascunho')
    objects  = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])


    class Meta:
        ordering = ('-publicado',)


    def __str__(self):
        return self.titulo


from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'publicado', 'status')
    list_filter = ('status', 'criado', 'publicado', 'autor')
    raw_id_fields = ('autor',)
    date_hierarchy = 'publicado'
    search_fields = ('conteudo', 'titulo')
    prepopulated_fields = {'slug': ('titulo',)}

# Create your models here.

"""
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

"""
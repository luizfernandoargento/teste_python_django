from django.contrib import admin
from .models import Post

# Registrar uma postagem no site
# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Para visualizar as informações na tabela da página admin
    list_display = ("tittle", "slug", "author", "created", "updated")
    # Preenche automaticamente o campo "slug" com o título.
    prepopulated_fields = {"slug": ("tittle",)}
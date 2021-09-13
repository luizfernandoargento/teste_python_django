from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Criar classe que herda Model do models.
# Como estamos fazendo Blog, criamos um "artigo" Post.
class Post(models.Model):
    tittle = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    # Slug é endereço do título da página, podenso ser acessado como
    # exemplo "www.meusite.com/blog/introducao-ao-django".
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    # "body" é o corpo do post.
    created = models.DateTimeField(auto_now_add=True)
    # Ao criar um posto, é adicionado automaticamente data da criação.
    updated = models.DateTimeField(auto_now=True)
    # Ao contrário do auto_now_add, ele atualiza a data automaticamente.

    # Ordenar as postagens pelo atributo created no sentido inverso.
    class Meta:
        ordering = ("-created",)

    # Para mudar o título de Post object (1) para o título da postagem.
    def __str__(self):
        return self.tittle

    # Se você acessar o shell e digitar:
    # ~ from blog1.models import Post
    # ~ post = Post.objects.get(id=1)
    # ~ post.get_absolute_url()
    # Ele imprime o endereço da url completo para acessar o post em questão!
    def get_absolute_url(self):
        # "reverse" Define a url de um recurso
        return reverse("blog1:detail", kwargs={"slug": self.slug})
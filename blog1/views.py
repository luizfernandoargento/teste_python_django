from django.views.generic import DetailView, ListView
# DetailView para mostrar um post e ListView para listar todos.
from .models import Post

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

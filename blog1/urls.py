from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = "blog1"
urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail" ),
]
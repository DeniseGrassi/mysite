# blog/urls.py

from django.urls import path

from .views.post_view import PostView 

urlpatterns = [
    path('', PostView.as_view(), name='home'),  # rota raiz com nome 'home'
]

from django.urls import path
from .views import TweetViewSet

urlpatterns = [
    path('tweets/', TweetViewSet.as_view({'get': 'list', 'post': 'create'}), name='tweet-list'),  # Listar tweets e criar novos tweets
    path('tweets/<int:pk>/', TweetViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='tweet-detail'),  # Detalhes, atualizar e deletar tweet específico
]

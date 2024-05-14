from django.urls import path
from .views import TweetViewSet

urlpatterns = [
	path('tweets/', TweetViewSet.as_view({'get': 'list', 'post': 'create'}), name='tweet-list'),  # Endpoint para listar tweets e criar novos tweets
]
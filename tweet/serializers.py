from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Tweet
        fields = ['id', 'user' ,'username', 'tweet']
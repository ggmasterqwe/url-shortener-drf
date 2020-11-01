from rest_framework import serializers
from .models import Url

class UrlPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ['slug', 'user_url', 'user']

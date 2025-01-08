from rest_framework import serializers
from .models import Posts

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    class Meta:
        model = Posts
        fields='__all__'
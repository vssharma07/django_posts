from rest_framework import serializers
from .models import Post, Comment, User


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ['id', 'post', 'author', 'text', 'created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'first_name', 'last_name', 'username']

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['id', 'title', 'content', 'author', 'published_date', 'created_at', 'updated_at']
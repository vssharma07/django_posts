from django.shortcuts import render
from rest_framework import generics, permissions, pagination
from .serializers import PostSerializer, CommentSerializer
from django.views.generic import ListView, DetailView
from .models import Post, Comment

class HomeView(ListView):
	model = Post
	template_name = 'home.html'

class CustomPageNumberPagination(pagination.PageNumberPagination):
	page_size = 1  # Number of items per page
	page_size_query_param = 'page'
	max_page_size = 100

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = CustomPageNumberPagination

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = CustomPageNumberPagination

class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)


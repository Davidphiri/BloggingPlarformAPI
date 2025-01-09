from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
# Ensure that PostSerializer is defined in serializers.py

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'
    
class PostList(APIView):
    def get(self, request, format=None):
        title = request.query_params.get('title','')
        
        if title:
            posts = Post.objects.filter(title__icontains=title)
            
        else:
            posts = Post.objects.all()
            
            serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        pass
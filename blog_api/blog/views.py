from django.shortcuts import render
from .models import Comment,Post
from .serializers import CommentSerializer,PostSerializer
from rest_framework import viewsets,permissions

def blog_frontend_view(request):
    return render(request, 'blog/blog_frontend.html')

class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)        


# Create your views here.

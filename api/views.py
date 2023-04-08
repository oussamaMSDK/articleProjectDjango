from django.shortcuts import render
from .models import Article
from .serializer import ArticleSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

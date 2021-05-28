from django.shortcuts import render,redirect
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all()
    return render()
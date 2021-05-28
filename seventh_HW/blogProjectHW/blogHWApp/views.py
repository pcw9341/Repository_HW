from django.shortcuts import render,redirect
# Create your views here.
from .models import Article

def index(request):
    movie_count = Article.objects.filter(category="movie").count()
    drama_count = Article.objects.filter(category="drama").count()
    programming_count = Article.objects.filter(category="programming").count()
    return render(request,'index.html',{'movie_count':movie_count, 'drama_count':drama_count,'programming_count':programming_count})

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    return render(request,'detail.html',{'article':article})

def new(request):
    if request.method == "POST" :
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category']
        )
        return redirect('detail',article_pk=new_article.pk)

    return render(request,'new.html')

def movie(request):
    articles = Article.objects.filter(category="movie")
    return render(request,'movie.html',{'articles':articles})

def drama(request):
    articles = Article.objects.filter(category="drama")
    return render(request,'drama.html',{'articles':articles})

def programming(request):
    articles = Article.objects.filter(category="programming")
    return render(request,'programming.html',{'articles':articles})



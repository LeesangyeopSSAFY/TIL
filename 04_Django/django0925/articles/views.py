from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method=='POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form=ArticleForm()
    context={
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article=get_object_or_404(Article, pk=pk)
    context={
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article=get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article=get_object_or_404(Article, pk=pk)
    if request.method=='POST':
        form=ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form=ArticleForm(instance=article)
    context={
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
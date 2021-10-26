from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http.response import JsonResponse, HttpResponse
from .serializers import ArticleSerializer, ArticleListSerializer
from .models import Article

# Create your views here.
# def article_html(request):
#     articles = Article.objects.all()
#     context = {
#         'articles': articles,
#     }
#     return render(request, 'articles/article.html', context)


# def article_json_1(request):
#     articles = Article.objects.all()
#     articles_json = []

#     for article in articles:
#         articles_json.append(
#             {
#                 'id': article.pk,
#                 'title': article.title,
#                 'content': article.content,
#                 'created_at': article.created_at,
#                 'updated_at': article.updated_at,
#             }
#         )
#     return JsonResponse(articles_json, safe=False)


# def article_json_2(request):
#     articles = Article.objects.all()
#     data = serializers.serialize('json', articles)
#     return HttpResponse(data, content_type='application/json')


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET': 
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'데이터 {article_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
from django.db import models

# Create your models here.
class Article(models.Model): # django.db.models.Model을 상속받는다.
    title = models.CharField(max_length=10) # 하나의 필드(컬럼, 열)이고 CharField는 각 컬럼의 데이터 타입을 알려준다.
    content = models.TextField() # TextFeild와 CharField는 text이지만 길이에 차이가 있다.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
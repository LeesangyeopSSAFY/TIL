from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# class Covenience(models.Model):
#     name = models.CharField(max_length=50)
#     location = models.TextField()
#     phone = models.TextField()

#     def __str__(self):
#         return self.name

# class Item(models.Model):
#     convenience = models.ForeignKey(Covenience, on_delete=models.CASCADE)
#     type = models.CharField(max_length=50)
#     quantity = models.IntegerField()
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.type
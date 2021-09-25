from django.db import models

def articles_image_path(instance, filename):
    return f'user_{instance.pk}/{filename}'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

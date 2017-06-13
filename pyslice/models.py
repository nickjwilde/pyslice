from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.title

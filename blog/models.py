from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    draft = models.TextField(null=True)
    published_date = models.DateField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title
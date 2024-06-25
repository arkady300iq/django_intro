from django.db import models
from datetime import datetime, timedelta

class Author(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=40)
    content = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def published_recently(self):
        now = datetime.now()
        return self.published_date >= now -timedelta(days=7)


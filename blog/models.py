from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=40)
    content = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
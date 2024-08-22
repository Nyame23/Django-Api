from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateField()
    publication_time = models.TimeField(default=timezone.now)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)

    def __str__(self):
        return self.title

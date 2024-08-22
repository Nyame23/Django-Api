# myapp/management/commands/delete_articles.py
from django.core.management.base import BaseCommand
from myapp.models import Article  # Replace 'myapp' with your app name

class Command(BaseCommand):
    help = 'Delete all articles'

    def handle(self, *args, **kwargs):
        Article.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all articles'))

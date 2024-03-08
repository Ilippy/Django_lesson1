from myapp.models import Author, Post
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Create post."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='UserID')
        parser.add_argument('title', type=str, help='Title')
        parser.add_argument('content', type=str, help='content')
        parser.add_argument('is_published', type=bool, help='is_published')

    def handle(self, *args, **kwargs):
        user = Author.objects.get(pk=kwargs.get('pk'))
        post = Post(author=user, title=kwargs['title'], content=kwargs['content'], is_published=kwargs['is_published'])

        post.save()
        self.stdout.write(f'{post}')

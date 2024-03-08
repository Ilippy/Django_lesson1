from django.core.management.base import BaseCommand
from myapp.models import Post


class Command(BaseCommand):
    help = "Delete post by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Post ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        post = Post.objects.filter(pk=pk).first()
        if post is not None:
            post.delete()
        self.stdout.write(f'{post}')

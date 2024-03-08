from django.core.management.base import BaseCommand
from myapp.models import Post


class Command(BaseCommand):
    help = 'Get posts by title'

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help="Title")

    def handle(self, *args, **options):
        title = options['title']
        post = Post.objects.filter(title=title).first()
        self.stdout.write(f"{post}")

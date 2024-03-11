from django.core.management.base import BaseCommand
from myapp.models import Author, Post
from random import choice

class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Amount of fake data')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(
                firstname=f'Name{i}',
                lastname=f"LastName{i}",
                email=f'mail{i}@mail.ru',
                biography=f"biography{i}"
            )
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title{j}',
                    content=f'Text from{author.firstname} {author.lastname} #{j} is bla bla bla many long text',
                    author=author,
                    is_published=choice((True, False))
                )
                post.save()

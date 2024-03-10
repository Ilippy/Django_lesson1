from homeworkapp.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Delete User"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='UserID')

    def handle(self, *args, **options):
        User.objects.get(pk=options['pk']).delete()
        self.stdout.write('User deleted!')

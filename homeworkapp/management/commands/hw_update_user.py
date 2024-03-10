from homeworkapp.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Update user"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('-n', '--name', type=str, help='User name optional')
        parser.add_argument('-e', '--email', type=str, help='User email optional')
        parser.add_argument('-p', '--phone', type=str, help='User phone optional, format: +74951112233')
        parser.add_argument('-a', '--address', type=str, help='User address optional')

    def handle(self, *args, **options):
        user = User.objects.get(pk=options['pk'])

        if name := options['name']:
            user.name = name

        if email := options['email']:
            user.email = email

        if phone := options['phone']:
            user.phone_number = phone

        if address := options['address']:
            user.address = address

        user.save()
        self.stdout.write(
            self.style.SUCCESS(f"User updated.\n{user}")
        )

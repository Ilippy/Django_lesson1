from django.core.management import BaseCommand
from users.models import User
from django.core.exceptions import ValidationError


class Command(BaseCommand):
    help = 'Создание кастомного суперюзера'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('first_name', type=str)
        parser.add_argument('last_name', type=str)

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        email = kwargs['email']
        first_name = kwargs['first_name']
        last_name = kwargs['last_name']
        password = input('Password: ')

        try:
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            self.stdout.write(self.style.SUCCESS('Суперпользователь создан'))
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f'Ошибка: {e.message}'))
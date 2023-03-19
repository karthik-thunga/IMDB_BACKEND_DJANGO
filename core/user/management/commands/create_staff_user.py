from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a new staff user.'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='The email address of the user.')
        parser.add_argument('password', type=str, help='The password for the user.')
        parser.add_argument('username', type=str, help='The username for the user.')


    def handle(self, *args, **options):
        User = get_user_model()
        email = options['email']
        password = options['password']
        username = options['username']
        user = User.objects.create_user(username=username, email=email, password=password, is_staff=True)
        self.stdout.write(self.style.SUCCESS(f'Successfully created staff user with email: {email}'))
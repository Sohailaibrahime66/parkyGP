from django.core.management.base import BaseCommand
from parking.models import User

class Command(BaseCommand):
    help = 'Creates a superuser with predefined email and password'

    def handle(self, *args, **options):
        email = "admin@smartparking.com"
        password = "123456"

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING("Admin already exists!"))
        else:
            User.objects.create_superuser(email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser {email} created successfully."))

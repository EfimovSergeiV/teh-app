from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        pass

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


token = Token.objects.create(user_id=3, key='f832d03d8b1b7ca9d6bd54534b95d9a562703655')

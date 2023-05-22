from django.core.management.base import BaseCommand, CommandError
from storage.models import FileHistoryModel, FileArchiveModel
import math
from random import randint


class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        pass

max = 150
count = 0

queryset = FileHistoryModel.objects.get(id=3)

authors = [
    "Петя Пупкин",
    "Василий Залупкин",
    "Владимир Путин",
    "Дмитрий Медведев",
    "Владимир Зеленский",
    "Джордш Буш",
    "Ангела Меркиль",
]



create_random_date = f"20{randint(10,23)}-{randint(1, 12)}-{randint(1, 29)} {randint(7, 18)}:{randint(1,60)}:22.273656"

print(create_random_date)

while count < max:
    count += 1
    
    FileHistoryModel.objects.create(
        latest = queryset.latest,
        author = authors[randint(0, len(authors) - 1)],
        created_date = create_random_date,
        name = "Модели",
        md5 = "55c3483e66885e4faf394789e71952c8",
        file = "/files/storage/models/7/debian_9PEzTJt.zip",
    )
from django.core.management.base import BaseCommand

from instaparser.models import TaskForParse
from scrapy_parser.scrapy_parser.runner import start_parsing


class Command(BaseCommand):
    help = 'Парсит данные подписчиков указанного пользователя'

    def handle(self, *args, **options):
        task = TaskForParse.objects.filter(status=TaskForParse.Status.WAITING).order_by('created_at').first()
        if task:
            # task.status = TaskForParse.Status.IN_PROGRESS
            # task.save()
            start_parsing(task.user_to_scrape)


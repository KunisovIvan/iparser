from django.core.management.base import BaseCommand

from instaparser.models import TaskForParse
from instaparser.views.misc import write_file
from scrapy_parser.scrapy_parser.runner import start_parsing


class Command(BaseCommand):
    help = 'Парсит данные подписчиков указанного пользователя'

    def handle(self, *args, **options):
        task = TaskForParse.objects.filter(status=TaskForParse.Status.WAITING).order_by('created_at').first()
        if task:
            user_to_scrape = task.user_to_scrape
            user_id = task.user.id
            TaskForParse.objects.filter(user_to_scrape=user_to_scrape,
                                        user_id=user_id).update(status=TaskForParse.Status.IN_PROGRESS)
            try:
                start_parsing(user_to_scrape, user_id)
            except Exception:
                TaskForParse.objects.filter(user_to_scrape=user_to_scrape,
                                            user_id=user_id).update(status=TaskForParse.Status.ERROR)

            task = TaskForParse.objects.filter(user_to_scrape=user_to_scrape, user_id=user_id).first()
            count_of_data = task.data_from_parse.all().count()
            if count_of_data:
                task.count_parse_data = count_of_data
                task.save()
                if not task.next_max_id:
                    task.status = TaskForParse.Status.DONE
                    task.save()
                    write_file(task)
                else:
                    task.status = TaskForParse.Status.WAITING
                    task.save()
            else:
                task.status = TaskForParse.Status.ERROR
                task.save()

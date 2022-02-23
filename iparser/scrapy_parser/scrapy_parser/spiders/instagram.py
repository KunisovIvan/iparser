from datetime import timedelta

import scrapy
from django.utils import timezone
from scrapy.http import HtmlResponse
import re
import json

from instaparser.models import InstagramAccount, TaskForParse
from scrapy_parser.scrapy_parser.items import ScrapyParserItem


class InstagramSpider(scrapy.Spider):
    """Класс для парсинга instagram."""

    name = 'instagram'
    allowed_domains = ['instagram.com']
    start_urls = ['https://www.instagram.com/']
    login_url = "https://www.instagram.com/accounts/login/ajax/"

    # Ограничение instagram на 500 действий в сутки
    count_for_parse = 500

    def __init__(self, user_to_scrape, user):
        super().__init__()
        self.user_to_scrape = user_to_scrape
        self.user = user

    def parse(self, response: HtmlResponse, ** kwargs):

        username, enc_password = self.select_instagram_account()
        print(username)
        yield scrapy.FormRequest(
            self.login_url,
            callback=self.user_login,
            method="POST",
            formdata={"username": username, "enc_password": enc_password},
            headers={"X-CSRFToken": self.fetch_csrf_token(response.text)}
        )

    def user_login(self, response: HtmlResponse):

        json_data = response.json()
        print('json_data-> ', json_data)
        if json_data["user"] and json_data["authenticated"]:
            self.user_id = json_data["userId"]
            user_to_scrape_url = f"/{self.user_to_scrape}"
            yield response.follow(
                user_to_scrape_url,
                callback=self.user_data_parse
            )

    def user_data_parse(self, response: HtmlResponse):

        task = TaskForParse.objects.filter(user_to_scrape=self.user_to_scrape, user_id=self.user).first()
        user_id = self.fetch_user_id(response.text, self.user_to_scrape)

        if task.type_of_parse == TaskForParse.TypeOfParse.FOLLOWERS:
            url = (f'https://i.instagram.com/api/v1/friendships/{user_id}/followers/'
                   f'?count={self.count_for_parse}&search_surface=follow_list_page')
        else:
            url = (f'https://i.instagram.com/api/v1/friendships/{user_id}/following/'
                   f'?count={self.count_for_parse}')

        if task.next_max_id:
            url += f'&max_id={task.next_max_id}'

        yield response.follow(
            url,
            callback=self.parse_followers,
        )

    def parse_followers(self, response: HtmlResponse):

        task = TaskForParse.objects.filter(user_to_scrape=self.user_to_scrape, user_id=self.user).first()

        task.next_max_id = response.json().get('next_max_id', '')
        task.save()

        username_list = [x.username for x in task.data_from_parse.all()]

        followers_pk_list = [i['pk'] for i in response.json()['users'] if i['username'] not in username_list]

        for pk in followers_pk_list:
            follower_to_scrape_url = f'https://i.instagram.com/api/v1/users/{pk}/info/'
            yield response.follow(
                    follower_to_scrape_url,
                    callback=self.parse_follower,
                )

    def parse_follower(self, response: HtmlResponse):

        data = response.json()['user']

        username = data.get('username')
        full_name = data.get('full_name')
        biography = data.get('biography')
        contact_phone_number = data.get('contact_phone_number')
        public_email = data.get('public_email')
        follower_count = data.get('follower_count')
        following_count = data.get('following_count')
        following_tag_count = data.get('following_tag_count')
        is_private = data.get('is_private')
        media_count = data.get('media_count')
        usertags_count = data.get('usertags_count')
        business_contact_method = data.get('business_contact_method')
        instagram_location_id = data.get('instagram_location_id')
        whatsapp_number = data.get('whatsapp_number')

        yield ScrapyParserItem(
            username=username,
            full_name=full_name,
            biography=biography,
            contact_phone_number=contact_phone_number,
            public_email=public_email ,
            follower_count=follower_count,
            following_count=following_count,
            following_tag_count=following_tag_count,
            is_private=is_private,
            media_count=media_count,
            usertags_count=usertags_count,
            business_contact_method=business_contact_method,
            instagram_location_id=instagram_location_id,
            whatsapp_number=whatsapp_number,
            user_to_scrape=self.user_to_scrape,
        )

    @staticmethod
    def fetch_csrf_token(text):
        """Получаем токен для авторизации."""

        matched = re.search('\"csrf_token\":\"\\w+\"', text).group()
        return matched.split(':').pop().replace(r'"', '')

    @staticmethod
    def fetch_user_id(text, username):
        """Получаем id желаемого пользователя."""

        matched = re.search(
            '{\"id\":\"\\d+\",\"username\":\"%s\"}' % username, text
        ).group()
        return json.loads(matched).get('id')

    @staticmethod
    def fetch_count_followers(text):
        """Получаем количество подписчиков желаемого пользователя."""

        matched = re.search('\"edge_followed_by\":{\"count\":\d+', text).group()
        return matched.split(':').pop()

    @staticmethod
    def select_instagram_account() -> tuple:
        """Получаем учетные данные неиспользованного аккаунта."""

        instagram_account = InstagramAccount.objects.filter(is_used=False).first()
        if instagram_account:
            instagram_account.is_used = True
            instagram_account.used_at = timezone.now()
            instagram_account.save()
        else:
            time_period = timezone.now() - timedelta(days=1)
            InstagramAccount.objects.filter(used_at__lt=time_period).update(is_used=False)
            instagram_account = InstagramAccount.objects.filter(is_used=False).first()
            if instagram_account:
                instagram_account.is_used = True
                instagram_account.used_at = timezone.now()
                instagram_account.save()
            else:
                return '', ''

        return instagram_account.username, instagram_account.enc_password



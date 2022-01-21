from django.contrib import admin

from instaparser.models import TaskForParse, Data


class TaskForParseAdmin(admin.ModelAdmin):
    """Выводить модель TaskForParse"""

    list_display = ['user', 'user_to_scrape', 'status', 'created_at', 'updated_at']


class DataAdmin(admin.ModelAdmin):
    """Выводить модель TaskForParse"""

    list_display = [
        'id',
        'username',
        'full_name',
        'biography',
        'is_private',
        'follower_count',
        'following_count',
        'following_tag_count',
        'media_count',
        'usertags_count',
        'contact_phone_number',
        'public_email',
        'whatsapp_number',
        'business_contact_method',
        'instagram_location_id',
    ]


admin.site.register(TaskForParse, TaskForParseAdmin)
admin.site.register(Data, DataAdmin)

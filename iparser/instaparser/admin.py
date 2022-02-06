from django.contrib import admin

from instaparser.models import TaskForParse, Data, InstagramAccount


class TaskForParseAdmin(admin.ModelAdmin):
    """Выводить модель TaskForParse"""

    list_display = ['id', 'user', 'user_to_scrape', 'status', 'file', 'created_at', 'updated_at']
    list_editable = ['status', 'file']


class InstagramAccountAdmin(admin.ModelAdmin):
    """Выводить модель InstagramAccount"""

    list_display = ['id', 'username', 'is_used']
    list_editable = ['is_used', ]


class DataAdmin(admin.ModelAdmin):
    """Выводить модель TaskForParse"""

    list_display = [
        'id',
        'task_for_parse',
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
admin.site.register(InstagramAccount, InstagramAccountAdmin)

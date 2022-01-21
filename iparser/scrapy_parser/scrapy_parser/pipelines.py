from instaparser.models import Data, TaskForParse


class ScrapyParserPipeline:

    def process_item(self, item, spider):

        task_for_parse = TaskForParse.objects.filter(user_to_scrape=item.get("user_to_scrape")).first()

        Data.objects.create(
            task_for_parse=task_for_parse,
            username=item.get('username'),
            full_name=item.get('full_name'),
            biography=item.get('biography'),
            is_private=item.get('is_private'),
            follower_count=item.get('follower_count'),
            following_count=item.get('following_count'),
            following_tag_count=item.get('following_tag_count'),
            media_count=item.get('media_count'),
            usertags_count=item.get('usertags_count'),
            contact_phone_number=item.get('contact_phone_number'),
            public_email=item.get('public_email'),
            whatsapp_number=item.get('whatsapp_number'),
            business_contact_method=item.get('business_contact_method'),
            instagram_location_id=item.get('instagram_location_id'),
        )

        return item

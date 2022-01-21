# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyParserItem(scrapy.Item):

    username = scrapy.Field()
    full_name = scrapy.Field()
    follower_count = scrapy.Field()
    following_count = scrapy.Field()
    following_tag_count = scrapy.Field()
    is_private = scrapy.Field()
    media_count = scrapy.Field()
    biography = scrapy.Field()
    usertags_count = scrapy.Field()
    business_contact_method = scrapy.Field()
    instagram_location_id = scrapy.Field()
    contact_phone_number = scrapy.Field()
    public_email = scrapy.Field()
    whatsapp_number = scrapy.Field()
    user_to_scrape = scrapy.Field()

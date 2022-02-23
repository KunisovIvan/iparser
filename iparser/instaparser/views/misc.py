import pandas as pd


def write_file(task) -> None:
    """ Записывает спаршенные даннык в файл"""

    username_list = []
    full_name_list = []
    biography_list = []
    is_private_list = []
    follower_count_list = []
    following_count_list = []
    following_tag_count = []
    media_count_list = []
    usertags_count_list = []
    contact_phone_number_list = []
    public_email_list = []
    whatsapp_number_list = []
    business_contact_method_list = []
    instagram_location_id_list = []

    for item in task.data_from_parse.all():
        username_list.append(item.username)
        full_name_list.append(item.full_name)
        biography_list.append(item.biography)
        is_private_list.append(item.is_private)
        follower_count_list.append(item.follower_count)
        following_count_list.append(item.following_count)
        following_tag_count.append(item.following_tag_count)
        media_count_list.append(item.media_count)
        usertags_count_list.append(item.usertags_count)
        contact_phone_number_list.append(item.contact_phone_number)
        public_email_list.append(item.public_email)
        whatsapp_number_list.append(item.whatsapp_number)
        business_contact_method_list.append(item.business_contact_method)
        instagram_location_id_list.append(item.instagram_location_id)

    df = pd.DataFrame({
        'Username': username_list,
        'ФИО': full_name_list,
        'Описание профиля': biography_list,
        'Приватный ли аккаунт': is_private_list,
        'Кол-во подписчиков': follower_count_list,
        'Кол-во подписок': following_count_list,
        'Кол-во подписок на теги': following_tag_count,
        'Кол-во публикаций': media_count_list,
        'Кол-во тегов пользователя': usertags_count_list,
        'Телефон': contact_phone_number_list,
        'Email': public_email_list,
        'Whatsapp': whatsapp_number_list,
        'Способ связи': business_contact_method_list,
        'id геолокации': instagram_location_id_list,
    })

    df.to_excel(f'/home/ivan/Project/Iparser/iparser/media/file/{task.user_to_scrape}.xlsx')
    task.file.name = f'file/{task.user_to_scrape}.xlsx'
    task.save()

from django import forms
from django.forms import RadioSelect


class HomeForm(forms.Form):
    username = forms.CharField(label='', widget=forms.Textarea())
    type_of_parse = forms.ChoiceField(label='Выберите тип сбора данных',
                                      widget=RadioSelect(),
                                      choices=[(1, 'Сбор данных о подписчиках'),
                                               (2, 'Сбор данных о подписках')])
    is_parse_new_data = forms.ChoiceField(label='Собирать только новые данные',
                                          widget=RadioSelect(),
                                          choices=[(1, 'Только новые данные (рекомендуется)'),
                                                   (2, 'Собирать данные с нуля')])

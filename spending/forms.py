from django import forms
from django.contrib.auth.models import User
from spending.models import SpendingType
from account.models import Account


class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            'all': ('/static/css/pickmeup.css',)
        }
        js = ('/static/js/jquery.pickmeup.min.js',
              '/static/js/date.input.js')

    def __init__(self):
        super().__init__(
            {'class': 'date', 'size': '8'},
        )


class SpendingForm(forms.Form):
    date = forms.DateField(
        required=True,
        label='Дата',
        input_formats=[
            '%d-%m-%Y',
            '%d-%m-%y',
            '%d/%m/%y',
            '%d/%m/%Y',
            '%d.%m.%y',
            '%d.%m.%Y'
        ],
        widget=CalendarWidget
    )
    money = forms.IntegerField(
        label='Сумма*',
        required=True,
    )
    comment = forms.CharField(
        max_length=32, required=False,
        label='Комментарий',
    )
    owner = forms.ModelChoiceField(
        queryset=User.objects.all(),
        empty_label=None,
        required=False,
        label='Автор',
    )
    spendingType = forms.ModelChoiceField(
        queryset=SpendingType.objects.all(),
        required=True,
        label='Тип траты*',
        empty_label='Выбери тип траты',
    )
    incomeType = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        required=True,
        label='Источник денег',
    )

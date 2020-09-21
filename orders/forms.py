from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name',
                  'last_name',
                  'email',
                  'address',
                  'postal_code',
                  'phone_number'
                  ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': "control-label", 'id': "Имя",
                                                 'placeholder': "Введите ваше имя"}),
            'last_name': forms.TextInput(attrs={'class': "control-label", 'id': "Фамилия",
                                                'placeholder': "Введите вашу фамилию"}),
            'email': forms.TextInput(attrs={'class': "control-label", 'id': "Электронная почта",
                                            'placeholder': "Введите вашу почту"}),
            'address': forms.TextInput(attrs={'class': "control-label", 'id': "Адрес",
                                              'placeholder': "Введите ваш полный адрес"}),
            'postal_code': forms.TextInput(attrs={'class': "control-label", 'id': "Почтовый адрес",
                                                  'placeholder': "Введите ваш почтовый адрес"}),
            'phone_number': forms.TextInput(attrs={'class': "control-label", 'id': "Номер телефона",
                                            'placeholder': "Введите ваш номер телефона"}),
        }
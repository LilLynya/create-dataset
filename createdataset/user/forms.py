from django import forms
from django.contrib.auth.forms import AuthenticationForm, get_user_model


class AuthForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
        labels = {
            'username': 'Введите Ваш логин',
            'password': 'Введите Ваш пароль'
        }


class RegisterForm(forms.ModelForm):
    username = forms.CharField(min_length=3)
    password = forms.CharField(min_length=8, max_length=255)
    password1 = forms.CharField(min_length=8, max_length=255)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Введите логин',
            'password': 'Введите пароль',
            'password1': 'Повторите пароль'
        }

    def clean_password2(self):
        clean_data = self.cleaned_data
        if clean_data['password'] != clean_data['password2']:
            raise forms.ValidationError("Пароли не совпадают.")
        else:
            return clean_data['password']

    def clean_email(self):
        user_email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=user_email).exists():
            raise forms.ValidationError("Данная почта уже зарегистрирована.")
        else:
            return user_email
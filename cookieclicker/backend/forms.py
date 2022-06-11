from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']

    username = forms.CharField(
        min_length = 3,
        max_length = 20,
        label = 'Имя пользоватея',
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}),
    )
    password = forms.CharField(
        min_length = 3,
        max_length = 20,
        label = 'Пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}),
    )
    password_confirm = forms.CharField(
        min_length = 3,
        max_length = 20,
        label = 'Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль еще раз'}),
    )

    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают друг с другом")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        if commit:
            user.save()
        return user

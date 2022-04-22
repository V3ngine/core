from django import forms


class LoginForm(forms.Form):
    name = forms.CharField(label='Имя пользователя', required=True)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(), required=True)
    mail = forms.EmailField(label='Электронная почта', required=True)


class PostForm(forms.Form):
    title = forms.CharField(label='Заголовок',max_length=100)
    message = forms.CharField(label='Пост',max_length=1000, widget=forms.Textarea())
    author = forms.CharField(label='Автор',max_length=30)

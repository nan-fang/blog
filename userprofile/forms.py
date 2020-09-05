from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserLoginForm(forms.Form):#Forms类不与数据库进行直接交互，登录登出用Forms就好
    username = forms.CharField()
    password = forms.CharField()

class UserRegisterForm(forms.ModelForm):#ModelForms类需要与数据库交互，比如新建、更新等

    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username','email')

    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password') 
        else:
            raise forms.ValidationError("密码输入不一致，请重试。")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone','bio')

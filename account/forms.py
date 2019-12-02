from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):                                                     #ModelForm상속
    password = forms.CharField(label='Password', widget=forms.PasswordInput)            #password-> Meta class 안 fields에서 설정가능하지만 CharField이기 때문에 widget옵션을사용해 지정
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    class Meta:                                                                         #기존에 있는 모델의 입력 폼
        model = User
        fields = ['username','email']

    def clean_password2(self):                                                          #유효성 검사 메소드 ->password와 password2가 같은지 검사
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']
from .models import User
from django import forms
import re
CHOISES=(
    ('Buy','Buyer'),
    ('Sell','Seller')
)
def min_length_8_validator(value):
    if len(value) < 8:
        raise forms.ValidationError('8글자 이상 입력해주세요')

def need_alpha_and_special(value):
    pattern = re.compile('(?=.*\d{1,50})(?=.*[~`!@#$%\^&*()-+=]{1,50})(?=.*[a-zA-Z]{1,50}).{8,50}$')
    if pattern.match(value)== None:
        raise forms.ValidationError('비밀번호는 영문 및 특수기호를 각각 1개 이상 포함해야합니다.')

class RegisterForm(forms.ModelForm):                                                     #ModelForm상속
    password = forms.CharField(label='Password', widget=forms.PasswordInput, validators=[need_alpha_and_special])            #password-> Meta class 안 fields에서 설정가능하지만 CharField이기 때문에 widget옵션을사용해 지정
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput, validators=[need_alpha_and_special])
    classification = forms.ChoiceField(choices=CHOISES, widget=forms.Select)
    username = forms.CharField(validators=[min_length_8_validator])
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder']="Your Name"
        self.fields['password'].widget.attrs['placeholder']="Password"
        self.fields['password2'].widget.attrs['placeholder']="Repeat Password"

    class Meta:                                                                         #기존에 있는 모델의 입력 폼
        model = User
        fields = ['username','name','pw','id']

    def clean_password2(self):                                                          #유효성 검사 메소드 ->password와 password2가 같은지 검사
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']
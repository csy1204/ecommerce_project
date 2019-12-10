from .models import User
from django import forms

CHOISES=(
    ('Buy','Buyer'),
    ('Sell','Seller')
)

class RegisterForm(forms.ModelForm):                                                     #ModelForm상속
    password = forms.CharField(label='Password', widget=forms.PasswordInput)            #password-> Meta class 안 fields에서 설정가능하지만 CharField이기 때문에 widget옵션을사용해 지정
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    classification = forms.ChoiceField(choices=CHOISES, widget=forms.Select)
    
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
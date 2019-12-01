from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.

def register(request):
    if request.method == 'POST':                                                                #회원 가입 정보가 전달
        user_form = RegisterForm(request.POST)                                                  #RegisterForm으로 유효성 검사
        if user_form.is_valid():
            new_user = user_form.save(commit=False)                                             #commit=False -> 데이터베이스에 넘기지 않음 객체만 만들어짐
            new_user.set_password(user_form.cleaned_data['password'])                           #비밀번호 지정 + 암호화
            new_user.save()                                                                     #실제로 데이터베이스에 저장
            return render(request, 'registration/register_done.html', {'new_user':new_user})

    else:
        user_form = RegisterForm()                                                              

    return render(request, 'registration/register.html',{'form':user_form})
from django.shortcuts import render, render_to_response
from .forms import RegisterForm
# Create your views here.
def register(request):
    if request.method == 'POST':                                                                #회원 가입 정보가 전달
        user_form = RegisterForm(request.POST)                                                  #RegisterForm으로 유효성 검사
        if user_form.is_valid():
            new_user = user_form.save(commit=False)                                             #commit=False -> 데이터베이스에 넘기지 않음 객체만 만들어짐
            new_user.set_password(user_form.cleaned_data['password'])                           #비밀번호 지정 + 암호화
            new_user.classification=request.POST['classification']
            new_user.pw = request.POST['password']
            new_user.id = request.POST['username']
            new_user.save()                 
            return render(request, 'registration/register_done.html', {'new_user':new_user})
        else:
            return render(request, 'registration/register.html',{'form':user_form})
    else:
        user_form = RegisterForm()                                                              

    return render(request, 'registration/register.html',{'form':user_form})
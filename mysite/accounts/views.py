from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .forms import SignupForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html',{'form':form})


class MyPasswordChangeView(PasswordChangeView) :
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.info(self.request, '암호 변경을 완료했습니다!')
        return super().form_valid(form)
    


# Cookie Test 
def cookie_test(request, code):
    response = render(request, 'registration/cookieTest.html')
    if code == 'add':
        response.set_cookie('model', 'A001')
        response.set_cookie('prod', 'EV9')
    elif code == 'get' :
        model = request.COOKIES.get('model')
        prod = request.COOKIES.get('prod')
        print(model, prod)
    elif code == 'del' :
        response.delete_cookie('model')
        response.delete_cookie('prod')
    return response
        

from django.contrib.sessions.backends.db import SessionStore

# Session Test
def session_test(request, code):
    response = render(request, 'registration/sessionTest.html')
    session = request.session
    if code == 1:
        user = request.user        
        print(user,':', session)
    elif code == 2 :        
        session['model'] = 'A001'
        session['prod'] = 'EV9'
        print('session 데이터 등록')
    elif code == 3:
        model = session.get('model')
        prod = session.get('prod')
        print('session 데이터 추출')
        print(model, prod)
    elif code == 4:
        session.pop('model')
        print('session 데이터 삭제')
        session.pop('prod')
    return response    


    


    

 
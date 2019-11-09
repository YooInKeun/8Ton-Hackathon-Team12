from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
    return render(request, 'accounts_index.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('accounts:index')

    return render(request,'signup.html')
    


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('accounts:index')
        else:
            return render(request, 'login.html', {'error':'아이디 혹은 비밀번호가 맞지 않습니다.'})
    else:
        return render(request, 'login.html')



def logout(request):

    auth.logout(request)
    return redirect('accounts:index')
    

    
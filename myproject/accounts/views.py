from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def home(request):
    return render(request, 'accounts_index.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'accoutns/signup.html',{'error' : 'Username has already been taken'})
            except User.DoesNotExist:
                user = user.objects.create_user(
                    request.POST['username'], passoword = request.POST['password1'])
                auth.login(request.user)
                return redirect('home')

        else:
            return render(reqeust, 'signup.html', {'error':'Password must match'})

    else:
        return render(request, 'signup.html')
    


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(request, username = username, password = password1)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error':'아이디 혹은 비밀번호가 맞지 않습니다.'})
    else:
        return render(request, 'login.html')



def logout(request):

    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

    return render(request,'accounts_index.html')

    
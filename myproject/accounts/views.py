from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create.get(username = request.POST['username'])
                return render(request, 'accoutns/signup.html',{'error' : 'Username has already been taken'})
            except User.DoesNotExist:
                user = user.objects.create_user(
                    request.POST['username'], passoword = request.POST['password1'])
                auth.login(request.user)
                return redirect('index')

        else:
            return render(reqeust, 'accounts/signup.html', {'error':'Password must match'})

    else:
        return render(request, 'accounts/signup.html')
    


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(request, username = username, password = password1)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error':'아이디 혹은 비밀번호가 맞지 않습니다.'})
    else:
        return render(request, 'login.html')



def logout(request):

    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')

    return render(request,'index.html')

    
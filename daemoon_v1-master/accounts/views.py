from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def signup(request):
    if request.method == "POST":
        if request.POST.get('password1') == request.POST.get('password2'):
            user = User.objects.create_user(
                username = request.POST.get('username'),
                password = request.POST.get('password') 
            )
            auth.login(request,user)
            return redirect('/posts/')
        return render(request,'signup.html')
    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/posts/')
        else:
            return render(request,'login.html',{'error': '아이디 혹은 비밀번호가 잘못되었습니다.'})
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
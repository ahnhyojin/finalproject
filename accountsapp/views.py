from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def signup(request):
    # if request.method == 'POST':
    #     if request.POST['password1'] == request.POST['password2']:
    #         user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
    #         auth.login(request, user)  # user, 8번줄의 user와 같은
    #         return redirect('index')
    # return render(request, 'signup.html')  # 라이브러리에 있는 accounts/signup.html 은 뭐지??

    if request.method == 'POST':
            # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': '이미 존재하는 아이디입니다.'})     #accounts/signup.html'나는 왜 이 주소로 치면 애러 뜨지? 이케 쓰면 템플릿이 없데
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])              
                auth.login(request, user)
                return redirect('index')
        else:
            return render(request, 'signup.html', {'error': '비밀번호가 일치하지 않습니다.'})
    else:
            # User wants to enter info
        return render(request, 'signup.html')

def login(request):
    if request.method =='POST' :
        userID = request.POST['username']
        passWord = request.POST['password']
        user = auth.authenticate(request, username = userID, password = passWord)
        if user is not None :  #회원정보가 없다면 None출력 not None : 회언정보가 있다
            auth.login(request,user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error' : '아이디 혹은 비밀번호가 올바르지 않습니다.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST' :
        auth.logout(request)
        return redirect('index')
    return render(request, 'new.html')
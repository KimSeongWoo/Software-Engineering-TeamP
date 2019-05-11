from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .forms import UserForm, LoginForm, ProfileShowForm, PasswordModifyForm
from .models import Profile

# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        data ={'username': request.user,'is_authenticated': request.user.is_authenticated}
    else:
        data ={'username': request.user.username,'password':request.user.password,'is_authenticated': request.user.is_authenticated}
    return render(request, 'Login/home.html', context={'data': data})

def loginview(request):
    if request.method=="POST":
        form = LoginForm(request.POST)
        name = request.POST['username']
        pwd=request.POST['password']
        #인증
        user = authenticate(username=name,password=pwd)
        if user is not None:
            login(request,user)
            #return redirect("home")#시작페이지로 이동
            return redirect("Posting/posting")
        else:
            return render(request,"Login/login_error.html")
    else: #GET방식이면 로그인 페이지로 이동
        form = LoginForm()
        return render(request, "Login/login.html", {"form": form})

def logoutview(request):
    logout(request)
    return redirect("/")

def register(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request,new_user)
            return redirect("/")#시작페이지로 이동
        else:
            return render(request, 'Login/register_error.html')
    else: #GET방식이면 회원가입 페이지로 이동
        form = UserForm()
        return render(request, "Login/register.html",{"form":form}) #'A'을 html에 B로 던지겠다

#--------------------Profile----------------------
@login_required # 로그인 여부를 검사하여 접근을 통제할 수 있다. 단, 함수형 뷰일때만
def profileview(request,myid):
    infos = Profile.objects.all()
    return render(request, "Profile/profile.html")
    

#--------------------modify-----------------------프로필, 비밀번호
@login_required 
def passwordmodify(request): #미완성
     if request.method=="POST":
        form = LoginForm(request.POST)
        name = request.POST['username']
        pwd=request.POST['password']
        #인증
        user = authenticate(username=name,password=pwd)
        if user is not None:
            login(request,user)
            #return redirect("home")#시작페이지로 이동
            return redirect("Posting/My_posting_list")
        else:
            return render(request,"Login/login_error.html")
     else: #GET방식이면 비밀번호 변경 페이지로 이동
        form = PasswordModifyForm()
        return render(request, "Modify/password.html", {"form": form})


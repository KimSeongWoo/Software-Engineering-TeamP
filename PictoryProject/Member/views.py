from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserForm, LoginForm, ProfileShowForm, ProfileEditForm, PasswordEditForm
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
            return redirect("home")#시작페이지로 이동
            #return redirect("Posting/posting")
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
        profile_num = Profile.objects.count()
        only_admin = User.objects.count()
        if form.is_valid():
            if profile_num==0: #admin만 존재하고 그 프로필이 없을경우
                admin = User.objects.first()
                Profile.objects.create(owner_id=admin.id)
            new_user = User.objects.create_user(**form.cleaned_data)
            Profile.objects.create(owner_id=new_user.id, name = new_user.username, photo='images/basic_image.jpg') #기본 프로필사진 설정
            login(request,new_user)
            return redirect("/")#시작페이지로 이동
        else:
            return render(request, 'Login/register_error.html')
    else: #GET방식이면 회원가입 페이지로 이동
        form = UserForm()
        return render(request, "Login/register.html",{"form":form}) #'A'을 html에 B로 던지겠다

def user_list(request):
    users = User.objects.all()
    context = {'users': users,}
    return render(request, 'user_list.html', context)

#--------------------Profile----------------------
@login_required # 로그인 여부를 검사하여 접근을 통제할 수 있다. 단, 함수형 뷰일때만
def myprofile(request):
    user=request.user
    profile = Profile.objects.get(owner_id = user.id)
    data ={'사진':profile.photo,'이름': profile.name,'Email' : profile.email,'phone':profile.phone,'소개말':profile.introduction,}
    return render(request, 'profile/myprofile.html', context={'data': data})

@login_required
def user_detail(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    profile = Profile.objects.get(owner_id = user.id)
    #posts = Post.objects.filter(owner=user)
    data ={'이름': profile.name,'Email' : profile.email,'phone':profile.phone,'소개말':profile.introduction,}
    return render(request, 'user_detail.html', context={'data': data})

    
#--------------------edit-----------------------프로필, 비밀번호
@login_required 
def profile_edit(request):
     if request.method=="POST":
        form = ProfileEditForm(request.POST)
        if form.is_valid() :
            user=request.user
            new_profile = Profile.objects.get(owner_id = user.id)
            new_profile.photo = request.FILES['photo']
            new_profile.name = form.cleaned_data['name']
            new_profile.email = form.cleaned_data['email']
            new_profile.phone = form.cleaned_data['phone']
            new_profile.introduction = form.cleaned_data['introduction']
            new_profile.save()
            return redirect("myprofile")
        else:
            return render(request,"profile/myprofile.html")
     else: #GET방식
        form = ProfileEditForm()
        return render(request, "profile/myprofile_edit.html", {"form": form})

@login_required 
def password_edit(request):
     if request.method=="POST":
        form = PasswordEditForm(request.POST)
        user=request.user
        if form.is_valid() :
            user.set_password(form.cleaned_data['password'])
            user.save()
            logout(request)
            return redirect("home")
        else:
            return render(request,"profile/password_edit_error.html")
     else: #GET방식
        form = PasswordEditForm()
        return render(request, "profile/password_edit.html", {"form": form})


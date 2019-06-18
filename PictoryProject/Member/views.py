from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserForm, LoginForm, ProfileShowForm, ProfileEditForm, PasswordEditForm
from .models import Profile


# Create your views here.

def home(request):
    if not request.user.is_authenticated: 
        data ={'username': request.user,'is_authenticated': request.user.is_authenticated}
        return render(request, 'Login/home.html', context={'data': data})
    else:  #여기서 프로필 보여주는걸로
        data ={'username': request.user.username,'password':request.user.password,'is_authenticated': request.user.is_authenticated}
        profile=Profile.objects.get(owner_id=request.user.id)
        return render(request, 'Login/home.html', context={'data': data, 'profile':profile})

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

#--------------------MY-----------------------------------------------------------------------------------------------------------나 관리용
#--------------------Profile----------------------
@login_required # 로그인 여부를 검사하여 접근을 통제할 수 있다. 단, 함수형 뷰일때만
def myprofile(request):
    user=request.user
    profile = Profile.objects.get(owner_id = user.id)
    data ={'사진':profile.photo,'이름': profile.name,'Email' : profile.email,'phone':profile.phone,'소개말':profile.introduction,}
    return render(request, 'profile/myprofile.html', context={'data': data})
    
#--------------------edit-----------------------프로필, 비밀번호
@login_required 
def profile_edit(request):
     if request.method=="POST":
        form = ProfileEditForm(request.POST)
        if form.is_valid() :
            user=request.user
            new_profile = Profile.objects.get(owner_id = user.id)
            if(request.POST.get('photo')!=''):
                new_profile.photo=request.FILES['photo']
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
        user=request.user
        old_profile = Profile.objects.get(owner_id = user.id)
        return render(request, "profile/myprofile_edit.html", context = {"form": form, "old" : old_profile})

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


#------------------------follow시 view--------------------------------
@login_required
def follow_this_account(request,user_pk):
    user = get_object_or_404(User, pk=user_pk) #대상의 유저
    userprofile = Profile.objects.get(owner_id = user.id)
    afollow = request.user #팔로우 하는 자신
    myprofile = Profile.objects.get(owner_id = afollow.id) # 내프로필에서
    myprofile.following.add(userprofile)#내가 팔로우 하는 사람으로 추가하고
    userprofile.followers.add(myprofile)#대상의 유저 follower에 나를 추가한다.
    return redirect('user_detail', user_pk=user.id)

#팔로우를 이미 했을 때를 검사해줘야 html내
def dont_follow(request,user_pk) :
    user = get_object_or_404(User, pk=user_pk) #대상의 유저
    userprofile = Profile.objects.get(owner_id = user.id)
    afollow = request.user #팔로우 하는 자신
    myprofile = Profile.objects.get(owner_id = afollow.id) # 내프로필에서
    userprofile.followers.remove(myprofile)#대상의 유저 follower에 나를 제거한다.
    myprofile.followers.remove(userprofile)#내가 팔로우 하는 사람으로 제거하고

    #대상의 유저 follower에 나를 제거한다.
    return redirect('user_detail', user_pk=user.id)

def myfollow_list_view(request) :
    user = request.user
    userprofile = Profile.objects.get(owner_id = user.id)
    myfollowing = userprofile.filter(following = userprofile.id)
    myfollowers = userprofile.followers.filter(from_profile_id = userprofile.id)
    context = {'followers': followers, 'followings' : myfollowing,}
    return render(request, 'myfollow_list.html', context)

#-----------------------------------------Others-------------------------------------------------------------타인에게 접속용

def user_list(request):
    users = User.objects.all()
    context = {'users': users,}
    return render(request, 'user_list.html', context)

@login_required
def user_detail(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    profile = Profile.objects.get(owner_id = user.id)
    data ={'owner':profile.owner_id,'이름': profile.name,'Email' : profile.email,'phone':profile.phone,'소개말':profile.introduction,}
    return render(request, 'OthersProfile.user_detail.html', context={'data': data})

@login_required
def userfollow_list_view(request,user_pk) :
    ...

@login_required
def user_detail_posts  (request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    profile = Profile.objects.get(owner_id = user.id)
    data ={'owner':profile.owner_id,'이름': profile.name,'Email' : profile.email,'phone':profile.phone,'소개말':profile.introduction,}
    return render(request, 'OthersProfile.user_detail_posts.html', context={'data': data})
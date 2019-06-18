from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from django.contrib.auth.models import User
import sys
sys.path.append("..")   #상위 폴더 import는 이렇게 한다
from Member.models import Profile 


# Create your views here.

def posting(request):
    postings=Post.objects.filter(user_id=request.user.id).order_by('-pub_date') #현재 유저의 포스팅만 가져오기
    #postings=Post.objects.all().order_by('-pub_date')  #이건 타임라인에서 쓸 것
    profile=Profile.objects.get(owner_id=request.user.id)
    comment = Comment()
    comment = Comment.objects.all()
    allprofile = Profile.objects.all()
    return render(request, 'Posting/My_posting_list.html',{'postings':postings, 'profile':profile,'all_comment':comment,'who':allprofile}) #dictionary 여러개 보내는 거 되나? 하나안엔 되네

def new(request):
    return render(request,'Posting/new.html')

def create(request):
    post = Post()
    post.title = request.POST.get('title',False)
    post.description = request.POST.get('des',False)
    post.pub_date = timezone.datetime.now()
    post.image = request.FILES['image']
    post.like=0
    post.TMP=0
    post.user=get_object_or_404(User,pk=request.POST.get('user_id',False))
    post.save()

    return redirect('/posting/')

def delete(request, post_id):
    post=get_object_or_404(Post, pk=post_id)
    post.delete()

    return redirect('/posting/')


def edit(request, post_id):
    old_post = get_object_or_404(Post,pk=post_id)
    return render(request, "Posting/edit.html", {"old" : old_post})

def update(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
    post.title = request.POST.get('title',False)
    post.description = request.POST.get('des',False)
    post.pub_date = timezone.datetime.now()
    if(request.POST.get('image')!=''):
        post.image=request.FILES['image']
    post.save()

    return redirect('/posting/')


#--------------------------comment-------------------------------------//대화형식으로 만들어보자
#___________________________ my posting에 comment
def comment_create(request,post_pk):
    #cur_post = get_object_or_404(Post, id = post_pk )
    new_comment = Comment()
    new_comment.body = request.POST['body']
    new_comment.cub_date = timezone.datetime.now()
    new_comment.post =  Post.objects.get(id = post_pk)
    new_comment.owner = Profile.objects.get(owner_id = new_comment.post.user_id)
    new_comment.save() 
    return redirect("posting")

def comment_update(reqeust,comment_pk) :
    if reqeust.method=="POST":
        updated = Comment.objects.get(id = comment_pk)
        updated.body = reqeust.POST['body']
        updated.save()
        return redirect("posting")
    else :
        updated = Comment.objects.get(id = comment_pk)
        return render(reqeust,"Comments/comment_update.html",{'comment':updated})


def comment_delete(reqeust,comment_pk):
    delcomment = Comment.objects.get(id = comment_pk)
    delcomment.delete()
    return redirect("posting")
    #cur_comment = get_object_or_404(Comment,id = comment_pk)
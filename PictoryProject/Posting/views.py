from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from django.contrib.auth.models import User
from .models import Post,Comment

# Create your views here.

def posting(request):
    postings=Post.objects.all().order_by('-pub_date')
    return render(request, 'Posting/My_posting_list.html',{'postings':postings})

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

    return redirect('/posting/' + str(post.id))
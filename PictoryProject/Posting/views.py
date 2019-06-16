from django.shortcuts import render

# Create your views here.

def posting(request):
    return render(request, 'Posting/My_posting_list.html')

def new(request):
    return render(request,'Posting/new.html')
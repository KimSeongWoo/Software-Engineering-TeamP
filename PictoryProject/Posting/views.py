from django.shortcuts import render

# Create your views here.

def posting(request):
    return render(request, 'My_posting_list.html')
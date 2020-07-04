from django.shortcuts import render
from .models import Post

def post_list(request):
   
    info = Post.objects.all()
    context={
        'post_list':info
    }
    return render(request,'blog/post_list.html',context)

def post_detail(request,id):
   
    detail_info = Post.objects.get(id=id)
    context={
        'detail_info':detail_info
    }
    return render(request,'blog/post_detail.html',context)    

def home(request): 
     return render(request,'base.html')  





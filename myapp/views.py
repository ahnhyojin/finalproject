from django.shortcuts import render, get_object_or_404
from . models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all
    return render(request, 'index.html', {'posts':posts})

# 상세페이지
def detail(request, post_id):
    postdetail = get_object_or_404(Post, pk= post_id)
    return render(request,'detail.html', {'posts': postdetail})

# upload 

# 수정(upda)
def edit(request):
    return render(request, 'edit.html')


def food1(request):
    
    return render(request,'food1.html')



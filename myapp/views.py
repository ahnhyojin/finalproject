from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from . models import Post

# Create your views here.
def index(request):
    posts = Post.objects
    return render(request, 'index.html', {'post' : posts})

# 상세페이지
def detail(request, post_id):
    postdetail = get_object_or_404(Post, pk= post_id)
    return render(request,'detail.html', {'posts': postdetail})

def create(request):
    if request.method == "GET":
        return render(request, 'new.html')
    else:
        newpost = Post()
        newpost.author = request.user
        newpost.title = request.POST['title']
        newpost.body = request.POST['fulltext']
        newpost.image = request.FILES['image']
        newpost.pub_date = timezone.datetime.now()
        newpost.save()
        return redirect('/detail/'+ str(newpost.id))

# upload (write)
def new(request):
    return render(request, 'new.html')

# 수정하기 (update)
def edit(request,post_id):
    postupdate = get_object_or_404(Post, pk = post_id)
    return render(request,'edit.html', {'postupdate' : postupdate})

def editSend(request, postupdate_id):
    if request.method == "GET":
        return render(request, 'edit.html')
    else:
        updateSendPost =  get_object_or_404(Post, pk =  postupdate_id)
        updateSendPost.title = request.POST['updatetitle']   # .title 이건 모델에서 정해준 이름이랑 같은건가?
        updateSendPost.body = request.POST['updatefulltext']
        updateSendPost.image = request.FILES['image']
        updateSendPost.pub_date = timezone.datetime.now()
        updateSendPost.save()
        return redirect('/detail/'+ str(updateSendPost.id))

def introduce(request):
    return render(request, 'introduce.html')




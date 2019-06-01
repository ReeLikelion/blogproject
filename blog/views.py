from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Blog

# Create your views here.

def home(request):
    blogs = Blog.objects # 쿼리셋
    blog_list = Blog.objects.all().order_by('-pub_data')
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})


def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'detail': details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_data = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_data = timezone.datetime.now()
        blog.save()
        return redirect('/blog/' + str(blog.id))
    return render(request, 'edit.html', {'blog':blog})

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()
    return redirect('/')


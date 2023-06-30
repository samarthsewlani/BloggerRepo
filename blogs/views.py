from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm
import datetime

def home(request):
    context = { 'blogs' : Blog.objects.all() }
    return render(request, 'blogs/base.html', context)

def contact(request):
    return render(request, 'blogs/contact.html')

def category(request):
    return render(request, 'blogs/page_in_construction.html')

@login_required
def create_blog(request):
    if request.method=="POST":
        form = BlogForm(request.POST, request.FILES)
        form.instance.author = request.user
        form.instance.date_posted = datetime.datetime.now()
        if form.is_valid():
           blog = form.save()
           print("New Blog :- ", blog)
           return redirect('home')
        else:
            print("Errors:-", form.errors)
            print(form.instance.cover)
            context = { 'form': form }
            return render(request, 'blogs/new_blog.html', context)
    form = BlogForm()
    context = { 'form': form }
    return render(request, 'blogs/new_blog.html', context)

@login_required
def update_blog(request, bid):
    blog = Blog.objects.filter(id = bid).first()
    if request.method=="POST":
        form = BlogForm(request.POST, request.FILES)
        form.instance.author = request.user
        form.instance.date_posted = datetime.datetime.now()
        if form.is_valid():
           blog = form.save()
           print("New Blog :- ", blog)
           return redirect('home')
        else:
            print("Errors:-", form.errors)
            print(form.instance.cover)
            context = { 'form': form }
            return render(request, 'blogs/update_blog.html', context)
    form = BlogForm( instance = blog )
    context = { 'form': form }
    return render(request, 'blogs/update_blog.html', context)

@login_required
def confirm_delete(request, bid):
    blog = Blog.objects.filter(id = bid).first()
    context = { 'blog' : blog }
    return render(request, 'blogs/confirm_delete.html', context)

@login_required
def delete(request, bid):
    blog = Blog.objects.filter(id = bid).delete()
    return redirect('home')


def bloglist(request):
    context = { 'blogs' : Blog.objects.all() }
    return render(request, 'blogs/base.html', context)

def blog_detail(request, bid):
    blog = Blog.objects.filter(id = bid).first()
    context = { 'blog' : blog }
    return render(request, 'blogs/blog_detail.html', context)

def blog_detail_new(request, bid):
    blog = Blog.objects.filter(id = bid).first()
    context = { 'blog' : blog }
    return render(request, 'blogs/blog_detail_new.html', context)


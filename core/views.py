from django.core.checks import messages
from core.models import Blog
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.text import slugify
import string
import random
from . import models, forms

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

def home(request):
    blogs = models.Blog.objects.all().order_by('date')
    return render(request, 'core/home.html', {'blogs': blogs})


@login_required 
def blogView(request, slug):
    blog = models.Blog.objects.get(slug = slug)
    likeCount = blog.likeCount()

    liked = False
    if blog.likes.filter(id = request.user.id).exists():
        liked = True

    context = {
        'blog': blog,
        'likeCount': likeCount,
        'liked': liked
    }
    return render(request, 'core/blog.html', context)

@login_required
def createBlogView(request):
    if request.method == 'POST':
        print('post request')
        form = forms.createBlog(request.POST)
        if form.is_valid():
            savedFormObject = form.save(commit=False)
            savedFormObject.author = request.user
            savedFormObject.slug = slugify(savedFormObject.title + "-" + rand_slug())
            savedFormObject.save()
        return redirect('/')
    else:
        createBlogForm = forms.createBlog()
    return render(request, 'core/createBlog.html', {'form': createBlogForm} )

@login_required
def editBlogView(request, slug):
    formData = get_object_or_404(Blog, slug=slug)
    author_id = formData.author.id
    blog = Blog.objects.get(slug=slug)
    form = forms.createBlog(instance=blog)

    if request.method == 'POST':
        updateBlogFormData = forms.createBlog(request.POST, instance=blog)
        if updateBlogFormData.is_valid():
            savedFormObject = form.save(commit=False)
            savedFormObject.slug = slugify(savedFormObject.title + "-" + rand_slug())
            savedFormObject.save()
        messages.success(request, 'blog updated')
        return redirect('/') 

    
    context ={
        'form': form,
        'author_id': author_id
    }
    return render(request, 'core/editBlog.html', context )
 



@login_required
def deleteBlogView(request, slug):
    blog = Blog.objects.get(slug=slug)
    context ={
        'blog':blog
    }

    return render(request, 'core/deleteBlog.html', context)

# @login_required
# def deleteConfirm(request, slug):
#     blog = get_object_or_404(Blog, slug=slug)
#     if request.method == 'POST':
#         blog.delete()
#         redirect('/')




def likeBlog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    liked = False
    if blog.likes.filter(id = request.user.id).exists():
        blog.likes.remove(request.user)
        liked = False

    else:
        blog.likes.add(request.user)
        liked = True

    
    return redirect('core:blog', slug=slug)


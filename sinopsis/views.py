from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Post
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Listing Page
def index(request):
    posts = Post.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'index.html', { 'posts': posts })

# Create Post
def add(request):
    template = loader.get_template('create.html')
    return HttpResponse(template.render({}, request))

# Store Blog 
def addrecord(request):
    x = request.POST['judul']
    y = request.POST['sinopsis']

    post = Post(judul=x, sinopsis=y)
    post.save()
    return HttpResponseRedirect(reverse('index'))

# Delete Post
def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(reverse('index'))

# Update Post
def update(request, id):
    post = Post.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'post': post,
    }
    return HttpResponse(template.render(context, request))

# Update Post
def updaterecord(request, id):
    judul = request.POST['judul']
    sinopsis = request.POST['sinopsis']
    post = Post.objects.get(id=id)
    post.judul = judul
    post.sinopsis = sinopsis
    post.save()
    return HttpResponseRedirect(reverse('index'))

# Show Post
def show(request, id):
    post = Post.objects.get(id=id)
    template = loader.get_template('show.html')
    context = {
        'post': post,
    }
    return HttpResponse(template.render(context, request))
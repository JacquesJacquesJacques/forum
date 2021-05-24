from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib.auth import authenticate, login

from .forms import PostForm, CommentForm
from .models import Community, Post, Comment


@login_required()
def home(request):
    return render(request, 'communitymanager/home.html')


@login_required()
def communities(request):
    communities = Community.objects.all()
    return render(request, 'communitymanager/communities.html', {'communities': communities})


@login_required()
def community(request, id):
    posts = get_list_or_404(Post, community_id=id)
    community = get_object_or_404(Community, id=id)
    return render(request, 'communitymanager/community.html', {'community': community, 'posts': posts})





@login_required()
def post_creation(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.date_creation = datetime.now()
        post.save()
        return redirect('post', id=post.id)
    else:
        return render(request, 'communitymanager/new_post.html', {'form': form})


@login_required()
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.creation_date = datetime.now()
            post.save()
            return redirect('post', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'communitymanager/post_edit.html', {'form': form, 'post': post})


@login_required()
def post(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post_id=id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.date_creation = datetime.now()
        comment.post = post
        comment.save()
        return redirect('post', id=post.id)
    else:
        return render(request, 'communitymanager/post.html', {'post': post, 'comments': comments, 'form': form})
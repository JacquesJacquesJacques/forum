from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm, CommentForm
from .models import Community, Post, Comment


@login_required()  # home view loads homepage with all post from communities the user follows
def home(request):
    posts = Post.objects.filter(community__followers__username__contains=request.user.username)
    return render(request, 'communitymanager/home.html', {'posts': posts})


@login_required()  # communities view loads all communities
def communities(request):
    communities = Community.objects.all()
    return render(request, 'communitymanager/communities.html', {'communities': communities})


@login_required()  # community view loads all posts from a given community
def community(request, id):
    posts = Post.objects.filter(community_id=id)
    community = get_object_or_404(Community, id=id)
    return render(request, 'communitymanager/community.html', {'community': community, 'posts': posts})


@login_required()  # subscribe view allows the user to follow or unfollow a community
def subscribe(request, id):
    user = request.user
    community = get_object_or_404(Community, id=id)
    followers = community.followers.all()
    if user in followers:
        community.followers.remove(user)
    else:
        community.followers.add(user)
    community.save()
    communities = Community.objects.all()
    return render(request, 'communitymanager/communities.html', {'communities': communities})


@login_required()  # post creation view creates a new post in data base
def post_creation(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user              # the author is automaticly set to current user
        post.date_creation = datetime.now()     # the date is set to current time
        post.save()
        return redirect('post', id=post.id)
    else:
        return render(request, 'utility/post_create.html', {'form': form, 'community': community})


@login_required()  # post edit view modifies an existing post
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user == post.author:     # checks if the user who tries to edit the post wrote it in the first place
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user          # the author is automaticly set to current user
                post.creation_date = datetime.now()     # the date is set to current time
                post.save()
                return redirect('post', id=post.id)
        else:
            form = PostForm(instance=post)
        return render(request, 'utility/post_edit.html', {'form': form, 'post': post})
    else:
        return redirect('post', id=post.id)


@login_required()  # post view loads a post with all related comments, and creates a form to write new comments
def post(request, id):
    post = get_object_or_404(Post, id=id)   # query of the commented post
    comments = Comment.objects.filter(post_id=id)   # query of all comments of this post
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user       # the author is automaticly set to current user
        comment.date_creation = datetime.now()  # the date is set to current time
        comment.post = post                 # the post is set to the commented one
        comment.save()
        return redirect('post', id=post.id)
    else:
        return render(request, 'communitymanager/post.html', {'post': post, 'comments': comments, 'form': form})

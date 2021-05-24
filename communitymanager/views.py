from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import *


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
def post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'communitymanager/post.html', {'post': post})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import *


@login_required()
def home(request):
    return render(request, 'communitymanager/home.html')


@login_required()
def community(request):
    communities = Community.objects.all()
    return render(request, 'communitymanager/communities.html', {'communities': communities})

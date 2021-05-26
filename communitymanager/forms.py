from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):        # Form to create or edit forms
    class Meta:
        model = Post
        fields = 'title', 'community', 'priority', 'event', 'date_event', 'description'


class CommentForm(forms.ModelForm):     # Form to create comments
    class Meta:
        model = Comment
        fields = 'content',




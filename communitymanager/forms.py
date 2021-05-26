from django import forms
from .models import Post, Comment


class ConnexionForm(forms.Form):
    username = forms.CharField(label="User name", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = 'title', 'community', 'priority', 'event', 'date_event', 'description'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = 'content',




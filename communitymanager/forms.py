from django import forms
from .models import Post


class ConnexionForm(forms.Form):
    username = forms.CharField(label="User name", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = 'description', 'community', 'priority', 'event', 'date_event', 'content'

    def clean(self):

        cleaned_data = super(PostForm, self).clean()
        description = cleaned_data['description']

        duplicate = Post.objects.filter(description=description)
        if duplicate.exists():
            raise forms.ValidationError('Post with same description already in database')
        return cleaned_data

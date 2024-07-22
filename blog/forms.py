from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class EditProfile(forms.ModelForm):
    newsusername = forms.CharField(max_length=100)
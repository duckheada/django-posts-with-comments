from pyexpat import model
from django import forms
from post.models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {'post': forms.HiddenInput()}     
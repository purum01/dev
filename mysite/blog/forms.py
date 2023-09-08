from django import forms
from .models import Post

class PostForm(forms.Form):
    title= forms.CharField(label='제목')
    body= forms.CharField(label='내용', widget=forms.Textarea)


class PostModelForm(forms.ModelForm) :
    class Meta:
        model = Post
        fields = ['title', 'body']
from django.contrib.auth.models import User
from django import forms
from blogapp.models import Comment,Article

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
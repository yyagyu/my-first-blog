from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','image')
        #image = forms.ImageField(Label='イメージ画像', required=False)
        labels = {
            'title':'タイトル',
            'text':'本文',
            'image':'イメージ画像'
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
        labels = {
            'author':'投稿者名',
            'text':'本文'
        }
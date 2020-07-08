from django import forms

from insta.models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'image',
            'caption',
            'location'
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
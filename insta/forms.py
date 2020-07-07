from django import forms

from insta.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'image',
            'caption'
        ]
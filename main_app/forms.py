from django import forms
form .models import Post 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('everything in Post model')
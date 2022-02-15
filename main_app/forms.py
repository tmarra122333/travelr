from django import forms
from .models import Guide, Profile

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Guide
#         fields = ('everything in Post model')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'city', 'profile_pic')

class GuideCreateForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = ('title', 'city', 'country', 'neighborhood', 'description', 'category', 'image')
    
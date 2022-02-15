from django import forms
from .models import Guide, Profile

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'city', 'profile_pic')

    widgets = {
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        'city': forms.TextInput(attrs={'class': 'form-control'}),
        'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
    }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'city', 'profile_pic')

class GuideCreateForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = ('title', 'city', 'country', 'neighborhood', 'description', 'category', 'image')
    
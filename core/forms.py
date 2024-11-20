from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'bio', 'birth_date', 'location', 'phone_number', 'website')
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-textarea',
                'rows': 4,
                'placeholder': 'Tell us about yourself...'
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'City, Country'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '+1234567890'
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-input',
                'placeholder': 'https://example.com'
            }),
        }

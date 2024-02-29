from django import forms
from .models import User


class Query(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "email", "phone", "comments"]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email','class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number', 'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control'}),
        }

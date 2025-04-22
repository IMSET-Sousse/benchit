from django import forms
from django.contrib.auth.models import User
from .models import BenchmarkResult

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class BenchmarkForm(forms.ModelForm):
    class Meta:
        model = BenchmarkResult
        fields = ['cpu', 'gpu', 'ram', 'storage']
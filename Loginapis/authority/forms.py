from django import forms
from .models import User

class ResetPasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password']
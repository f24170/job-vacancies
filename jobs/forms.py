from django import forms
from .models import Job

class JobFrom(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company']
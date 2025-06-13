from django import forms
from .models import Job, Resume

class JobFrom(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company']

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['file']
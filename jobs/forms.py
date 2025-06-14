from django import forms
from .models import Job, Resume

class JobFrom(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'salary', 'url', 'posted_date']
        labels = {
            'title': '職缺名稱',
            'company': '公司名稱',
            'location': '工作地點',
            'salary': '薪資',
            'url': '原始連結(選填)',
            'posted_date': '發布日期',
        }

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['file'] 
        labels = {
            'file': '履歷檔案(PDF)',
        }
from django.shortcuts import render, redirect, get_list_or_404
from django.conf import settings
from .models import Job, Resume
from .forms import JobFrom, ResumeForm
from .utils import extract_text_from_pdf, recommend_jobs
import os
import datetime

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs':jobs})

def create_job(request):
    if request.method == 'POST':
        form = JobFrom(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            if not job.posted_date:
                job.posted_date = datetime.date.today()
            job.save()
            return redirect('job_list')
    else:
        form = JobFrom()
    return render(request, 'jobs/create_job.html', {'form': form})

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()
            resume_path = resume.file.path
            resume.content = extract_text_from_pdf(resume_path)

            if not resume.content.strip():
                 recommendations = recommend_jobs(resume.content)
            else:
                print("履歷內容為空，跳過推薦")
                recommendations = [] 

            resume.save()
            return redirect('resume_detail', pk=resume.pk)   # 導回上傳成功頁面
    else:
        form = ResumeForm()
    return render(request, 'jobs/upload_resume.html', {'form': form})



def resume_detail(request, pk):
    try:
        resume = Resume.objects.get(pk=pk)
    except Resume.DoesNotExist:
        return render(request, 'jobs/resume_detail.html', {'resume': None})

    return render(request, 'jobs/resume_detail.html', {'resume':resume})
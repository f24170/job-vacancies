from django.shortcuts import render, redirect
from .models import Job
from .forms import JobFrom

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs':jobs})

def create_job(request):
    if request.method == 'POST':
        form = JobFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobFrom()
    return render(request, 'jobs/create_job.html', {'form': form})
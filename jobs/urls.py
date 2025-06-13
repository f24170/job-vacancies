from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('create/', views.create_job, name='create_job'),
    path('upload/', views.upload_resume, name='upload_resume'),
    path('resume/<int:pk>', views.resume_detail, name='resume_detail'),
]

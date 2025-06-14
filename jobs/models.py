from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)               # 職缺名稱
    company = models.CharField(max_length=255)             # 公司名稱
    location = models.CharField(max_length=255)            # 地點
    salary = models.CharField(max_length=100, blank=True)  # 薪資 (可留空)
    url = models.URLField(blank=True, null=True)           # 原始連結
    posted_date = models.DateField(null=True, blank=True)  # 發布日期

    def __str__(self):
        return f"{self.title} - {self.company}"
    
class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    content = models.TextField(blank=True)                 # 擷取出來的文字
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
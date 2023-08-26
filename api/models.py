from django.db import models




class Task(models.Model):
    owner=models.CharField(max_length=20)
    title=models.CharField(max_length=20)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)



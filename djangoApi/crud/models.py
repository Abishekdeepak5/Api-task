from django.db import models

# Create your models here.
class Task(models.Model):
    task_id=models.BigAutoField(primary_key=True)
    title=models.CharField(max_length=30)
    isComplete=models.BooleanField()

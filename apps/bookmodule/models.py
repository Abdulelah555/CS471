from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 50)
    createdate = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    Priority = models.CharField(max_length = 50)
    State = models.CharField(max_length = 50)
    description = models.CharField(max_length = 500)

    
class CheckList(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.PROTECT,
        blank=False
        )
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 500)
    done = models.CharField(max_length = 50,default=0)

from operator import mod
from django.db import models
from sqlalchemy import false

# Create your models here.
class Quiz(models.Model):
    STATUS_CHICE = (('publish','Publish'),('draft','Draft'))
    question = models.CharField(max_length=1000)
    option1=models.CharField(max_length=1000)
    option2=models.CharField(max_length=1000)
    option3=models.CharField(max_length=1000)
    option4=models.CharField(max_length=1000)
    answer=models.CharField(max_length=1000)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['-created']    


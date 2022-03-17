from django.db import models
from employee.models import MyUser,Jobs

# Create your models here.

class ApplicationModel(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    job=models.ForeignKey(Jobs,on_delete=models.CASCADE,null=True)
    jobid=models.PositiveIntegerField(null=True)
    name=models.CharField(max_length=250)
    phone=models.CharField(max_length=100)
    location=models.CharField(max_length=150)
    qualification=models.CharField(max_length=250)
    experience=models.PositiveIntegerField()
    resume=models.FileField(upload_to="uploads")
    options=(("pending","pending"),
             ("approved","approved"),
             ("rejected","rejected")
    )
    status=models.CharField(max_length=200,choices=options,default="pending")


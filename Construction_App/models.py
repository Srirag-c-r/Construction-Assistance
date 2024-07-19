from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)


class Contractor_Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True)
    phonenumber = models.CharField(max_length=200, null=True)

class Category(models.Model):
    category=models.CharField(max_length=50,null=True)

class worker_Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True)
    phonenumber = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)


class Request(models.Model):
    contractor = models.ForeignKey(Contractor_Registration, on_delete=models.CASCADE, null=True)
    worker = models.ForeignKey(worker_Registration, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)
    status1 = models.CharField(max_length=200, null=True)

class feedback(models.Model):
    worker = models.ForeignKey(worker_Registration, on_delete=models.CASCADE, null=True)
    contractor = models.ForeignKey(Contractor_Registration, on_delete=models.CASCADE, null=True)
    feedback = models.CharField(max_length=200, null=True)
    reply = models.CharField(max_length=200, null=True)

class con_feedback(models.Model):
    worker = models.ForeignKey(worker_Registration, on_delete=models.CASCADE, null=True)
    contractor = models.ForeignKey(Contractor_Registration, on_delete=models.CASCADE, null=True)
    feedback = models.CharField(max_length=200, null=True)
    reply = models.CharField(max_length=200, null=True)

class Blacklist_workers(models.Model):
    worker = models.ForeignKey(worker_Registration, on_delete=models.CASCADE, null=True)
    contractor = models.ForeignKey(Contractor_Registration, on_delete=models.CASCADE, null=True)
    reason = models.CharField(max_length=200, null=True)
    count=models.IntegerField(max_length=200, null=True)
    updated_at = models.DateField(auto_now=True)

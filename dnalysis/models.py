from django.contrib.auth.models import User
import datetime as dt
from django.db import models



class Register(models.Model):
    """
    Class that contains Register details
    """
    posted_on = models.DateTimeField(auto_now_add=True)
    business_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)
    contact = models.CharField(max_length = 30, blank=True)
    description = models.TextField()



class Space(models.Model):
    """
    Class that contains space for analysis, to be collected.
    """
    minibuses = models.CharField(max_length = 20)
    minibuses = models.CharField(max_length = 20)
    matatus = models.CharField(max_length = 20)
    posted_on = models.DateTimeField(auto_now_add=True)
    register = models.ForeignKey(Register, on_delete=models.CASCADE)

class Dailys(models.Model):
    """
    Class that contains Daily data to be collected.
    """
    passengers = models.CharField(max_length = 20)
    trips = models.CharField(max_length = 20)
    income = models.CharField(max_length = 20)
    posted_on = models.DateTimeField(auto_now_add=True)
    register = models.ForeignKey(Register, on_delete=models.CASCADE)

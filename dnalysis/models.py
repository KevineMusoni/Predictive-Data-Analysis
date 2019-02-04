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

class Data(models.Model):
   DAYS_OF_WEEK = (
       ('Monday', 'Monday'),
       ('Tuesday', 'Tuesday'),
       ('Wednesday', 'Wednesday'),
       ('Thursday', 'Thursday'),
       ('Friday', 'Friday'),
       ('Saturday', 'Saturday'),
       ('Sunday', 'Sunday'),
   )
   day=models.CharField(max_length=60,choices=DAYS_OF_WEEK)
   no_of_passengers=models.PositiveIntegerField()
   no_of_trips=models.PositiveIntegerField()
   income= models.PositiveIntegerField()
   date= models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.day



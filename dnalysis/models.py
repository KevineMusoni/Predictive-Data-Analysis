from django.db import models
from django import forms
# Create your models here.
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


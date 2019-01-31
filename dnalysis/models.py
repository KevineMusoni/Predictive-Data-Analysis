from django.contrib.auth.models import User
import datetime as dt
from django.db import models


class Registration(models.Model):
    """
    Class that contains Registration details.
    """
    business_name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    description = models.TextField()
    email = models.CharField(max_length = 20)
    contact = models.CharField(max_length = 30, blank=True)
    physical_adress = models.CharField(max_length = 20)

    rating = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_reg(self):
        self.save()

    def del_reg(self):
        self.delete()


    def __str__(self):
                return self.business_name

class NumberofBuses(models.Model):
   RATING_CHOICES = (
       (1, '1'),
       (2, '2'),
       (3, '3'),
       (4, '4'),
       (5, '5'),
       (6, '6'),
       (7, '7'),
       (8, '8'),
       (9, '9'),
       (10, '10')
   )

class NumberofMinibuses(models.Model):
   RATING_CHOICES = (
       (1, '1'),
       (2, '2'),
       (3, '3'),
       (4, '4'),
       (5, '5'),
       (6, '6'),
       (7, '7'),
       (8, '8'),
       (9, '9'),
       (10, '10')
   )

class NumberofMatatu(models.Model):
   RATING_CHOICES = (
       (1, '1'),
       (2, '2'),
       (3, '3'),
       (4, '4'),
       (5, '5'),
       (6, '6'),
       (7, '7'),
       (8, '8'),
       (9, '9'),
       (10, '10')
   )

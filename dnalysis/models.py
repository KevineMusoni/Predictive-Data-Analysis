from django.contrib.auth.models import User
import datetime as dt
from django.db import models



class Register(models.Model):
    """
    Class that contains Register details
    """
    posted_on = models.DateTimeField(auto_now_add=True)
    business_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    contact = models.CharField(max_length = 30, blank=True)
    route = models.TextField()


    def __str__(self):
        return self.business_name

    def save_editor(self):
        self.save()

class Space(models.Model):
    """
    Class that contains space for analysis, to be collected.
    """
    minibuses = models.PositiveIntegerField()
    minibuses = models.PositiveIntegerField()
    matatus = models.PositiveIntegerField()
    posted_on = models.DateTimeField(auto_now_add=True)
    register = models.ForeignKey(Register, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.register

    def save_editor(self):
        self.save()

class Dailys(models.Model):
    MONTHS_OF_YEAR = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    )
    month = models.CharField(max_length=60,choices=MONTHS_OF_YEAR)
    no_of_passengers = models.PositiveIntegerField()
    no_of_trips = models.PositiveIntegerField()
    income = models.PositiveIntegerField()

    def __str__(self):
        return self.month

    def save_editor(self):
        self.save()
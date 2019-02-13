from django.contrib.auth.models import User
import datetime as dt
from django.db import models

class Register(models.Model):
    """
    Class that contains Register details
    """
    user= models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="business",
    )
    posted_on = models.DateTimeField(auto_now_add=True)
    business_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    contact = models.CharField(max_length = 30, blank=True)

    def __str__(self):
        return self.business_name

    def save_editor(self):
        self.save()

class Space(models.Model):
    """
    Class that contains space for analysis, to be collected.
    """
    business_name = models.CharField(max_length = 100)
    no_of_small_buses = models.PositiveIntegerField()
    no_of_big_buses = models.PositiveIntegerField()
    posted_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.no_of_minibuses

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
    income = models.PositiveIntegerField()
    month = models.CharField(max_length=60,choices=MONTHS_OF_YEAR)
    no_of_passengers = models.PositiveIntegerField()
    no_of_trips = models.PositiveIntegerField()

    def __str__(self):
        return self.income

    def save_editor(self):
        self.save()

class View(models.Model):
    csv_data = models.CharField(max_length = 5000)

    def __str__(self):
        return self.csv_data
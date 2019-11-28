from django.db import models
from apps.LR_app.models import *
import datetime

class TripManager(models.Manager):
    def basic_validator(self,postData):
        error = { }

        if len(postData['dest']) < 2:
            error['dest'] = "Destination must be at least 2 characters long!"
        if len(postData['desc']) < 8:
            error['desc'] = "Description must be at least 8 characters long!"
        try:
            if datetime.datetime.strptime(postData['sd'],"%Y-%m-%d") < datetime.datetime.today():
                error['sd'] = "Start Date must be after Today!!!"
        except ValueError:
            error['sd'] = "Please select a date!!!!"
        try:
            if datetime.datetime.strptime(postData['ed'],"%Y-%m-%d") < datetime.datetime.strptime(postData['sd'],"%Y-%m-%d"):
                error['ed'] = "EndDate must be after StartDate!!!"
        except ValueError:
            error['ed'] = "Please select a date!!!!"
        return error

class Travel(models.Model):
    sDate = models.DateTimeField()
    eDate = models.DateTimeField()
    destinations = models.CharField(max_length=45)
    plan = models.TextField()
    uploadeder = models.ForeignKey(User, related_name="user_travel", on_delete=models.CASCADE)
    users_going = models.ManyToManyField(User,related_name="user_traveling")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = TripManager()
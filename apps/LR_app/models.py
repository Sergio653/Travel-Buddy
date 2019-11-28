from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self,postData):
        error = { }

        if len(postData['name']) < 3:
            error['name'] = " name should be at least 3 characters"
        if len(postData['username']) < 8:
            error['username'] = "username should be at least 8 characters"
        if User.objects.filter(username=postData['username']).count() > 0:
            error['username'] = "username not unique"
        if not postData['pw'] == postData['pw_confirmed']:
            error['pw_match'] ="Passwords do not match"
        if len(postData['pw']) < 8:
            error['pw_length'] = "Password too short. It needs to be at least 8 characters"
        return error


class User(models.Model):
    name = models.CharField(max_length=45)
    username  = models.CharField(max_length=45)
    pw_h  = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
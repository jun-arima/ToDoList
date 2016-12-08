import datetime
from django.db import models
from django.utils import timezone
from todolist import settings
from django.contrib.auth.models import AbstractBaseUser

class Task(models.Model):
    # user = models.ForeignKey(AbstractBaseUser)
    task_nm = models.CharField(max_length=100)
    task_text = models.CharField(max_length=500)
    comp_flg = models.BooleanField()

    def __str__(self):
        return self.task_nm

from django.db import models


# Create your models here.
class WorkShift(models.Model):

    shift_date = models.DateTimeField()
    work_start_time = models.DateTimeField()
    lunch_start_time = models.DateTimeField()
    lunch_end_time = models.DateTimeField()
    work_end_time = models.DateTimeField()

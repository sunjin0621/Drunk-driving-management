from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    phone_num = models.TextField()
    car_num = models.TextField()
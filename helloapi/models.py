from django.db import models


class Api(models.Model):
  client_ip = models.CharField(max_length=200)
  location = models.CharField(max_length=500)
  greeting = models.CharField(max_length=500) 

  def __str__(self):
    return self.client_ip + ' ' + self.location + ' ' + self.greeting

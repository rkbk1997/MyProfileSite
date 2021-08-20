from django.db import models

# Create your models here.
class projectdetail(models.Model):
    type  = models.CharField(max_length=100, null=True, blank= True)
    img1 = models.FileField(null=True, blank= True)
    img2 = models.FileField(null=True, blank= True)
    img3 = models.FileField(null=True, blank= True)
    titile = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank= True)
    client = models.CharField(max_length=100, null=True, blank= True)
    environment =  models.CharField(max_length=100, null=True, blank= True)
    project_date = models.CharField(max_length=100, null=True, blank= True)
    project_end_date = models.CharField(max_length=100, null=True, blank= True)
    role = models.CharField(max_length=100, null=True, blank= True)
    project_url = models.CharField(max_length=100, null=True, blank= True)
    heading = models.CharField(max_length=10000, null=True, blank= True)
    des = models.CharField(max_length=10000, null=True, blank= True)

class certificate(models.Model):
    titile = models.CharField(max_length=100, null=True, blank=True)
    img1 = models.FileField(null=True, blank= True)
    
from django.db import models

# Create your models here.
class Book(models.Model):
    bname=models.CharField(max_length=20)
    bpub_date=models.DateTimeField()
class Hero(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField()
    hcontent=models.CharField(max_length=500)
    hbook=models.ForeignKey(Book)

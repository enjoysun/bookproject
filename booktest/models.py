from django.db import models

# Create your models here.
class Book(models.Model):
    bname=models.CharField(max_length=20)
    bpub_date=models.DateTimeField()
    def __str__(self):
        return self.bname.encode('utf-8')
class Hero(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField()
    hcontent=models.CharField(max_length=500)
    hbook=models.ForeignKey(Book)
    def __str__(self):
       return self.hname.encode('utf-8')

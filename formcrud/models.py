from django.db import models

# Create your models here.
# database models creation
class Details(models.Model):
    userid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    addressLine1 = models.CharField(max_length=100)
    addressLine2 = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)
    state = models.CharField(max_length=50)



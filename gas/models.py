from django.db import models
from django.contrib.auth.models import User

class Signup(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10,null=True)
    dob = models.CharField(max_length=10,null=True)
    address = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=50,null=True)
    def _str_(self):
        return self.user.username
    
class Complain(models.Model):
    name = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=20,null=True)
    contact = models.CharField(max_length=30,null=True)
    complain = models.CharField(max_length=90,null=True)

class Booking(models.Model):
    name = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=20,null=True)
    contact = models.CharField(max_length=30,null=True)
    gastype = models.CharField(max_length=30,null=True)
    price = models.CharField(max_length=30,null=True)
    day = models.CharField(max_length=30,null=True)
    month = models.CharField(max_length=30,null=True)
    idtype = models.CharField(max_length=30,null=True)
    idno = models.CharField(max_length=30,null=True)
    address = models.CharField(max_length=30,null=True)
    status = models.CharField(max_length=70,null=True)

class Payment(models.Model):
    name = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=20,null=True)
    contact = models.CharField(max_length=30,null=True)
    price = models.CharField(max_length=30,null=True)
    mode = models.CharField(max_length=30,null=True)
    status = models.CharField(max_length=70,null=True)
    paymentdate = models.CharField(max_length=30,null=True)
    gastype = models.CharField(max_length=30,null=True)
    day = models.CharField(max_length=30,null=True)
    invoiceid = models.CharField(max_length=30,null=True)
    


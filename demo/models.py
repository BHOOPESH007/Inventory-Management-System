from django.db import models


class Admin(models.Model):
    username = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=10)
    fullname = models.CharField(max_length=20)

    def __str__(self):
        return self.username + '  ' + self.password


class Customer(models.Model):
    customerName = models.CharField(max_length=20)
    customerID = models.AutoField(max_length=10, primary_key=True)
    company = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=100 , default='SOME STRING')

    def __str__(self):

        return self.customerName + ' ' + self.customerID + ' ' + self.company + ' ' + self.mobile + ' ' + self.email + \
               ' ' + self.address

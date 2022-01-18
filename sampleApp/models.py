from django.db import models


class cashreg1(models.Model):
    ItemName = models.CharField(max_length=10)
    ProductCode =models.CharField(max_length=5)
    Stocks = models.CharField(max_length=15)
    Price = models.CharField(max_length=5)
    def __str__(self):
        return self.ItemName + " " + self.Price
    

class cashreg2(models.Model):
    ProductCode2 =models.CharField(max_length=5)
    ItemName2 = models.CharField(max_length=10)
    Quantity2 = models.CharField(max_length=15)
    Price2 = models.CharField(max_length=5)
    
    def __str__(self):
        return self.ProductCode2 + " " + self.Price2

class cashreg3(models.Model):
    Total3 =models.CharField(max_length=5)
    Cash3 = models.CharField(max_length=10)
    Change3 = models.CharField(max_length=15)
    Date3 = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Total3 + " " + self.Change3
    def get_date(self):
        return self.modified.date()

class cashreg4(models.Model):
    ProductCode2 =models.CharField(max_length=5)
    ItemName2 = models.CharField(max_length=10)
    Quantity2 = models.CharField(max_length=15)
    Price2 = models.CharField(max_length=5)
    
    def __str__(self):
        return self.ProductCode2 + " " + self.Price2

class cashreg5(models.Model):
    Total3 =models.CharField(max_length=5)
    Cash3 = models.CharField(max_length=10)
    Change3 = models.CharField(max_length=15)
    Date3 = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Total3 + " " + self.Date3

class login(models.Model):
    Username = models.CharField(max_length=15)
    Password = models.CharField(max_length=15)
    def __str__(self):
        return self.Username + self.Password

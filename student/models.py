from django.db import models

class StudentInfo(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField(unique=True)
    email = models.EmailField(default=False)
    address = models.CharField(max_length=250,default=False)
    GPA = models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField(default=False)


    def __str__(self):
       return str(self.roll)

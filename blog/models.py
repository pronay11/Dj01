from django.db import models

class Post(models.Model):
    tittle=models.CharField(max_length=80)
    description=models.TextField()
    created_dt=models.DateField()
    def __str__(self):
       return (self.tittle)


from django.db import models

# Create your models here.
    
class Datamaster(models.Model):
    number = models.IntegerField()
    arab = models.TextField(max_length=1000)
    indonesia = models.TextField(max_length=1000)
    perawi = models.CharField(max_length=60)
    
    def __str__(self):
        return self.perawi
    
class ListDoa(models.Model):
    doa = models.CharField(max_length=100)
    arab = models.TextField(max_length=1000)
    indonesia = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.doa
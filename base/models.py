from django.db import models

class Room(models.Model):
    
    #host       =
    #topic      =
    name        = models.CharField(max_Length=200)
    description = models.textField(null=True,blank=True)
    #participants =
    updated     = models.dateTimeField(auto_now=True)
    created     = models.dateTimeField(auto_now_add=True)

def __str__(self):
    return self.name
    

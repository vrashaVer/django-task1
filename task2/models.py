from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Status(models.Model):
    IN_RPOCESS = 'in process'
    DONE = 'done'
    DUSTED = 'dusted'
    STATUS_CHOICES = [
        (IN_RPOCESS, 'In process'),
        (DONE, 'Done'),
        (DUSTED, 'Dusted'),
    ]
    name = models.CharField(max_length=50,choices=STATUS_CHOICES,unique=True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    
    name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
 
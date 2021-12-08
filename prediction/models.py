from django.db import models

# Create your models here.

# Doctor
class Doctor(models.Model):
    boolChoice = (
        ("M", "Male"), ("F", "Female")
    )
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    age = models.IntegerField()
    hospital_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=boolChoice)
    
    def __str__(self):
        return self.name
    

#Feedback
class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return self.name
from django.db import models

class Employee (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=100)
    isManager = models.BooleanField(default=False)
    # Connecting with User table.


    def __str__(self):

        return self.name
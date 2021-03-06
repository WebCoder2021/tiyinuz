from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.SmallIntegerField()
    address = models.CharField(max_length=150)
    birth_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.user.username
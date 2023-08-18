from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    cuit = models.CharField(max_length=15, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    fec_nac = models.DateField(null=True)
    socio = models.BooleanField(default=True)
    socio_number = models.IntegerField(null=True)

def __str__(self):
    return f'{self.name}, {self.last_name}'
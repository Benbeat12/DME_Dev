from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customer(AbstractUser):
    profil_pic = models.ImageField(upload_to="profiles/", height_field=None, width_field=None, max_length=None,default="profiles/profil_default.jpg")
    statut_pic = models.ImageField(upload_to="status/", height_field=None, width_field=None, max_length=None,blank=True)
    age = models.CharField(max_length=3, blank=True)
    telephone = models.CharField(max_length=15, blank=True)
    is_customer = models.CharField(max_length=50,choices=(("Custuner","Custumer"),("Developpe","Developper"),))

    def get_absolute_url(self):
        return reverse("customer_detail", kwargs={"pk": self.pk})
    

   

from django.db import models
from django.db.models.query_utils import select_related_descend
from django.utils import timezone

# Create your models here.
# Service Models 
class Service(models.Model):
    service_id = models.AutoField(auto_created = True, primary_key = True,serialize = False, verbose_name ='ID')
    service_name = models.CharField(max_length=50, default="")
    service_desc = models.CharField(max_length=5000, default="")
    service_benefits = models.CharField(max_length=5000, default="")
    service_categary = models.CharField(max_length=50, default="")
    service_images = models.ImageField(upload_to="static/services/images", default="")
    service_main_img = models.ImageField(upload_to="static/services/images", default="")
    service_date = models.DateField(default=timezone.now)
    def __str__(self) -> str:
        return self.service_name+" - "+self.service_categary

# Contact Models are here 
class Contact(models.Model):
    con_id = models.AutoField(auto_created = True,primary_key = True,serialize = False, verbose_name ='ID')
    con_name = models.CharField(max_length=255, default="")
    con_email = models.CharField(max_length=255, default="")
    con_phone = models.CharField(max_length=12, default="")
    con_subject = models.CharField(max_length=22, default="")
    con_message = models.CharField(max_length=555, default="")
    con_datetime = models.DateField(default=timezone.now)
    def __str__(self) -> str:
        return self.con_name+" - "+self.con_email

# Product Models are here
class Product(models.Model):
    pro_id = models.AutoField(auto_created = True,primary_key = True,serialize = False, verbose_name ='ID')
    pro_name = models.CharField(max_length=50, default="")
    pro_categary = models.CharField(max_length=50, default="")
    pro_desc = models.CharField(max_length=5000, default="")
    pro_medapp = models.CharField(max_length=5000, default="")
    pro_images = models.ImageField(upload_to="static/product/images", default="")
    pro_price = models.CharField(max_length=50, default="")
    pro_datetime = models.DateField(default=timezone.now)
    def __str__(self) -> str:
        return self.pro_name+" - "+self.pro_categary

 # Testimonials Models are here       
class Testimonials(models.Model):
    testi_id = models.AutoField(auto_created = True,primary_key = True,serialize = False, verbose_name ='ID')
    testi_name = models.CharField(max_length=50, default="")
    testi_designation = models.CharField(max_length=50, default="")
    testi_fedback = models.CharField(max_length=2000, default="")
    testi_images = models.ImageField(upload_to="static/testimonials/images", default="")
    testi_datetime = models.DateField(default=timezone.now)
    def __str__(self) -> str:
        return self.testi_name

 # Subcribers Models are here       
class Subscribe(models.Model):
    subs_id = models.AutoField(auto_created = True,primary_key = True,serialize = False, verbose_name ='ID')
    subs_name = models.CharField(max_length=50, default="")
    subs_mobileno = models.CharField(max_length=50, default="")
    subs_email = models.CharField(max_length=101, default="")
    subs_datetime = models.DateField(default=timezone.now)
    def __str__(self) -> str:
        return self.subs_email

class UnicafeProduct(models.Model):
    upro_id = models.AutoField(auto_created = True,primary_key = True,serialize = False, verbose_name ='ID')
    upro_name = models.CharField(max_length=50, default="")
    upro_items = models.CharField(max_length=100, default="")
    upro_desc = models.CharField(max_length=5000, default="")
    upro_price = models.CharField(max_length=50, default="")
    upro_images = models.ImageField(upload_to="static/unicafe/images", default="")
    upro_datetime = models.DateField(default=timezone.now)
    def __str__(self) -> str:
        return self.upro_name


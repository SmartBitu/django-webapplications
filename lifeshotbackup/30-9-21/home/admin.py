from django.contrib import admin
from home.models import Contact, Product, Service, Subscribe, Testimonials, UnicafeProduct

# Register your models here.
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Subscribe)
admin.site.register(Testimonials)
admin.site.register(UnicafeProduct)
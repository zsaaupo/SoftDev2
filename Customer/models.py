import secrets
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=11)
    address = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    otp = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return self.full_name+" "+"("+self.phone_number+")"

    def save(self, *args, **kwargs):

        if not self.slug:
            slug = slugify(self.full_name)
            person_exists = Customer.objects.filter(slug=slug).exists()
            if person_exists:
                hexa = secrets.token_hex(6)
                self.slug = slug + "-M1u2s3h0-" + hexa
            else:
                self.slug = slug
            super(Customer, self).save(*args, **kwargs)
        else:
            super(Customer, self).save(*args, **kwargs)
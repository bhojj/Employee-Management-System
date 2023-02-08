from django.db import models

# from django.utils import timezone
# post_date = models.DateField(auto_now_add=True, default=timezone.now())

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    # email=models.EmailField(max_length=254)
    address=models.CharField(max_length=150)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=10)
    def __str__(self):
        return self.name


# email = models.EmailField(unique=True) : Harkesh lai sodne ranamati
# Admin ko customization garne method ho

class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    testimonial=models.TextField()
    picture=models.ImageField(upload_to="testimonials/")
    rating=models.IntegerField(max_length=1)
    # rating=models.IntegerField()

    def __str__(self):
        return self.testimonial


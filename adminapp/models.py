from django.db import models

# Create your models here.
class brand(models.Model):
    brand_names=models.CharField(max_length=30)


class category(models.Model):
    categories=models.CharField(max_length=30)
    brand_category_id=models.ForeignKey(brand,on_delete=models.CASCADE)

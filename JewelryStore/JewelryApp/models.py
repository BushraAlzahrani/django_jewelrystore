from django.db import models

# Create your models here.


class Designer(models.Model):
    name = models.CharField(max_length=50, help_text="Task Title")
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    d_photo = models.ImageField(upload_to='designer/photos/')

    def __str__(self):
        return self.name


class Jewelry(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField(help_text="The price")
    designer = models.ForeignKey(Designer, on_delete=models.DO_NOTHING)
    j_photo = models.ImageField(upload_to='jewelry/photos/')

    def __str__(self):
        return self.name



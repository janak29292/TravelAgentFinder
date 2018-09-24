from django.db import models

class DestType(models.Model):
    dtype = models.CharField(max_length=64)
    def __str__(self):
        return self.dtype

class Destinat(models.Model):
    name = models.CharField(max_length=64,unique=True)
    dtype = models.ForeignKey(DestType,related_name='places')
    descrip = models.TextField()
    reach = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Attrac(models.Model):
    title = models.CharField(max_length =64)
    pic = models.ImageField(upload_to='attractions')
    place = models.ForeignKey(Destinat,related_name='attrct')
    detl = models.TextField()
    def __str__(self):
        return self.title

class Img(models.Model):
    place = models.ForeignKey(Destinat,related_name='img')
    img = models.ImageField(upload_to='images')
    def __str__(self):
        return self.img.name


class PMessage(models.Model):
    name=models.CharField(max_length=64,blank=True)
    email=models.EmailField(blank=True,null=True)
    subject=models.CharField(max_length=142,blank=True)
    message=models.TextField(blank=True)
    def __str__(self):
        return self.name

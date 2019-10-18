from django.db import models

# Create your models here.
class Bookstore(models.Model):
    title = models.CharField(max_length=20,verbose_name='书名')
class Book(models.Model):
    title = models.CharField(max_length=20,verbose_name='书名',primary_key=True)
    pub = models.CharField(max_length=20,verbose_name='出版社',null=False)
    price = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='定价')
    marker_price = models.DecimalField(verbose_name='零售价',max_digits=5,decimal_places=2)
    def __str__(self):
        return '<%s>' %self.title
class Author(models.Model):
    name = models.CharField(null=False,verbose_name='姓名',max_length=20)
    age = models.IntegerField(verbose_name='年龄',null=True,default=1)
    email = models.EmailField(max_length=20)


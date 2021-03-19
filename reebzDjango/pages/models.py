from django.db import models

# Create your models here.
class mainPageProduct(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ürün adı')
    desc = models.TextField(verbose_name='Ürün açıklaması')
    category = models.CharField(max_length=50,default='sweatshirt',verbose_name='Ürün kategorisi')
    image = models.CharField(max_length=50,verbose_name='Ürün resmi')
    isPublished = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/img/'+ self.image
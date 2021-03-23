from django.db import models

# Create your models here.
class mainPageProduct(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ürün adı')
    desc = models.CharField(max_length=50, verbose_name='Ürün fiyatı')
    newImage = models.ImageField(upload_to ='uploads/', verbose_name='Yeni resim yüklemek için tıklayınız',null=True,blank=True)
    image = models.CharField(max_length=50,verbose_name='Ürün resmi adı')
    link = models.URLField(max_length=500,verbose_name='Shopier Ürün linki',default='link giriniz')
    reebzLink = models.URLField(max_length=500,verbose_name='Reebz Ürün linki',default='Reebz ürün sayfa linki giriniz')

    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/media/uploads/'+ self.image
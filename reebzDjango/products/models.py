from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ürün adı')
    desc = models.CharField(max_length=20,verbose_name='Ürün Fiyatı')
    newImage = models.ImageField(upload_to ='uploads/', verbose_name='Yeni resim yüklemek için tıklayınız',null=True,blank=True)
    image = models.CharField(max_length=50,verbose_name='Ürün resmi')
    img1 = models.CharField(max_length=50,default='resim1',verbose_name='küçük resim 1')
    img2 = models.CharField(max_length=50,default='resim2',verbose_name='küçük resim 2')
    img3 = models.CharField(max_length=50,default='resim3',verbose_name='küçük resim 3')
    img4 = models.CharField(max_length=50,default='resim4',verbose_name='küçük resim 4')
    link = models.URLField(max_length=500,verbose_name='Shopier Ürün linki',default='link giriniz')
    
    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/media/uploads/'+ self.image

    def get_image1(self):
        return '/media/uploads/'+ self.img1

    def get_image2(self):
        return '/media/uploads/'+ self.img2
        
    def get_image3(self):
        return '/media/uploads/'+ self.img3
        
    def get_image4(self):
        return '/media/uploads/'+ self.img4

    def get_link(self):
        return self.link


class SimilarProduct(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ürün adı')
    desc = models.CharField(max_length=50, verbose_name='Ürün fiyatı')
    newImage = models.ImageField(upload_to ='uploads/', verbose_name='Yeni resim yüklemek için tıklayınız',null=True,blank=True)
    image = models.CharField(max_length=50,verbose_name='Ürün resmi')
    link = models.URLField(max_length=500,verbose_name='Shopier Ürün linki',default='link giriniz')
    reebzLink = models.URLField(max_length=500,verbose_name='Reebz Ürün linki',default='Reebz ürün sayfa linki giriniz')

    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/media/uploads/' + self.image
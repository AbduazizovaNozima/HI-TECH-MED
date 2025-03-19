from django.db import models

class Customers(models.Model):
        full_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="To'liq ism")
        position = models.CharField(max_length=255, null=True, blank=True, verbose_name="Mavqesi")
        image = models.ImageField(upload_to="", verbose_name="Rasm")
        description = models.CharField(max_length=255, null=True, blank=True, verbose_name="Tavsif")

        class Meta:
            verbose_name = "Mijoz"
            verbose_name_plural = "Mijozlar"



# class Partner(models.Model):
#     image = models.ImageField(upload_to="")
#     url = models.CharField(max_length=255, blank=True)
#     order = models.IntegerField(default=1)

class News(models.Model):
        title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Mavzu nomi")
        description = models.CharField(max_length=255, null=True, blank=True, verbose_name="Tavsif")
        image = models.ImageField(upload_to="", verbose_name="Rasm")
        date = models.DateField(verbose_name="Sana")
        body = models.DateField(max_length=255, null=True, blank=True)

        class Meta:
            verbose_name = "Yangilik"
            verbose_name_plural = "Yangiliklar"



class Application(models.Model):

    class ApplicationChoices(models.TextChoices):
        main_page = ("main_page", "Bosh sahifa")
        service = ("service", "Server")
        get_tt = ("get_tt", "Texnik malumot olish")
        partner = ("partner", "Hamkor")
        order = ("order", "Buyruq")

    full_name = models.CharField(max_length=255, blank=True, verbose_name="To'liq ism")
    phone = models.CharField(max_length=255, blank=True, verbose_name="Tel raqam")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tavsif")
    product = models.CharField(max_length=255, blank=True,verbose_name="Mahsulot")
    status = models.CharField(max_length=255,
        choices=ApplicationChoices.choices,
        default=ApplicationChoices.main_page
        )
    class Meta:
            verbose_name = "Ilova"
            verbose_name_plural = "Ilovalar"




class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Mavzu")
    status = models.CharField(max_length=255, verbose_name="Maqom")
    order = models.IntegerField(default=1, verbose_name="Tartibi")
    image = models.ImageField(upload_to="", verbose_name="Rasm")
    short_description = models.CharField(max_length=255, verbose_name="Qisqa tavsif")
    # image = models.ImageField()
    description = models.CharField(max_length=255, verbose_name="Tavsif")
    brand = models.CharField("brand" ,max_length=255)
    country = models.CharField(max_length=255, verbose_name="Mamlakat")
    guarantee = models.CharField(max_length=255, verbose_name="Garantiya")
    is_main_page = models.BooleanField()
    category = models.ForeignKey("Category",related_name="products", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"


class ProductImage(models.Model):
    image = models.ImageField("Rasm", upload_to="")
    product = models.ForeignKey(
        Product, related_name="product_images", on_delete=models.CASCADE
    )

    class Meta:
            verbose_name = "Mahsulot rasmi"
            verbose_name_plural = "Mahsulot rasmlari"



class ProductCharacteristic(models.Model):
    key = models.CharField(max_length=255, verbose_name="Nomi")    
    value = models.CharField(max_length=255, verbose_name="Qiymati")
    order = models.IntegerField(default=1, verbose_name="Tartibi")
    product = models.ForeignKey(
        Product, related_name="productCharacteristic", on_delete=models.CASCADE
    )

    class Meta:
            verbose_name = "Mahsulot tavsifi"
            verbose_name_plural = "Mahsulot tavsiflari"



class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="", verbose_name="Rasm")
    order = models.IntegerField(default=1, verbose_name="Tartibi")
    
    class Meta:
            verbose_name = "Toifa"
            verbose_name_plural = "Toifalar"





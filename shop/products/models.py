from django.db import models


class Category(models.Model):
    category_name = models.SlugField(max_length=128, blank=True, null=True, default=None, unique=True)

    def __str__(self):
        return "%s" % self.category_name


class Subcategory(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, default=None)
    subcategory_name = models.SlugField(max_length=128, blank=True, null=True, default=None)
    subcategory_image = models.ImageField(upload_to='products_images/',default=None)

    def __str__(self):
        return "%s, %s" % (self.category.category_name, self.subcategory_name)

    def image_tag(self):
        return u'<img src="%s" />' % self.subcategory_image.url
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

class Product(models.Model):

    SIZES = (
        ('XS','XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    )
    subcategory = models.ForeignKey(Subcategory, blank=True, null=True, default=None)
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(blank=True, null=True, default=None)
    sizes = models.CharField(max_length=2, choices=SIZES, default='XS')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s, %s: %s" % (self.subcategory, self.name, self.price)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.id

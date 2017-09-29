from django.db import models

import os.path
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


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
    thumbnail = models.ImageField(upload_to='thumbnails/', max_length=500, null=True, blank=True, editable=False)
    is_main = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        if not self.make_thumbnail():
            # set to a default thumbnail
            raise Exception('Could not create thumbnail - is the file type valid?')

        super(ProductImage, self).save(*args, **kwargs)

    def make_thumbnail(self):

        THUMBNAIL_SIZE = (200, 200)
        image = Image.open(self.image)
        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        thumb_name, thumb_extension = os.path.splitext(self.image.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False  # Unrecognized file type

        # Save thumbnail to in-memory file as StringIO
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

        return True

    def __str__(self):
        return "%s" % self.id

from django.db import models

class Item(models.Model):
    products_name = models.CharField(max_length=150)
    slug = models.SlugField()
    brand = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    item_left = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now_add=True, editable=False)
    thumb = models.ImageField(default='default.jpg',blank=True)

    def __str__(self):
        return u'%s' % self.products_name

from django.db import models
from django.urls import reverse


# Creating the category table
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    # Meta allows us to override elements in our class
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]

        verbose_name = 'category'
        verbose_name_plural = 'categories'

    # To View the class name on admin
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    # Foreign Key Category that links products with it's category table.
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)  # Slugs are used to build beautiful URLs.
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # Order based on latest created products
        ordering = ['created']
        # Orders based index to get data fast using B-Tree indexes data structure
        # https://www.youtube.com/watch?v=kv3jC0P4gOc
        indexes = [
            models.Index(fields=['id', 'slug']),  # Query products by both "id" and "slug".
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

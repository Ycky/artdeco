from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='images')
    time_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Partners(models.Model):
    image = models.ImageField(upload_to='images')
    link = models.URLField()
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link


class Reviews(models.Model):
    name = models.CharField(max_length=120)
    review = models.TextField()
    rating = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

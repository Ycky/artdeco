from django.db import models

class Houses(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images')
    description = models.TextField()
    photo2 = models.ImageField(upload_to='images')
    photo3 = models.ImageField(upload_to='images')
    photo4 = models.ImageField(upload_to='images')
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

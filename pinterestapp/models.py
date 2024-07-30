from django.db import models


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

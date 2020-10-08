from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Images(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )
    images = models.ImageField(upload_to='images')
    editted_images = models.ImageField(upload_to='filters', null=True, blank=True)
    is_editted = models.BooleanField(default=False, null=True, blank=True) 

    def __str__(self):
        return self.name

    def save(self):
        self.editted_images.save(self.images.name, self.images, save=False)
        super(Images, self).save()

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
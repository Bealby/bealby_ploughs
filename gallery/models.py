from django.db import models
'''Pillow must be installed'''


class Gallery_1(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Ploughs'

    image = models.ImageField("Image", blank=True, null=True, help_text="Please upload images 600x400. Max 300px")
    image_title = models.CharField("Image Title", max_length=254, null=True, blank=True)
    image_description = models.CharField("Image Description", max_length=254, null=True, blank=True)

    def __str__(self):
        return self.image_title
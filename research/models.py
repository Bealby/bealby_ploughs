from django.db import models
'''Pillow must be installed'''


class Research_1(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Invoice Journals'

    image_text = models.TextField("Text", max_length=1000, null=True, blank=True)
    image = models.ImageField("Image", blank=True, null=True, help_text="Please upload images 600x400. Max 300px")
    image_title = models.CharField("1. Image Title", max_length=254, null=True, blank=True)
    image_description = models.CharField("1. Image Description", max_length=254, null=True, blank=True)
    image_2 = models.ImageField("2. Image", blank=True, null=True, help_text="Please upload images 600x400. Max 300px")
    image_title_2 = models.CharField("2. Image Title", max_length=254, null=True, blank=True)
    image_description_2 = models.CharField("2. Image Description", max_length=254, null=True, blank=True)

    def __str__(self):
        return self.image_text

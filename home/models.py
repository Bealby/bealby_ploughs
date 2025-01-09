from django.db import models
'''Pillow must be installed'''


class HomeAbout(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Home - About'



    text_1 = models.CharField(max_length=254, null=True, blank=True)
    image_1 = models.ImageField(null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    text_2 = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.name
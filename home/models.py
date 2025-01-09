from django.db import models
'''Pillow must be installed'''


class HomeAbout(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Home - About'

    paragraph_1 = models.TextField(max_length=1000, null=True, blank=True)
    image_1 = models.ImageField(null=True, blank=True)
    image_1_description = models.CharField(max_length=254, null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    image_2_description = models.CharField(max_length=254, null=True, blank=True)
    paragraph_2 = models.TextField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return self.text_1
    

class HomeArticles(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Home - Articles'

    image_1 = models.ImageField(null=True, blank=True)
    image_1_description = models.CharField(max_length=254, null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    image_2_description = models.CharField(max_length=254, null=True, blank=True)
    image_3 = models.ImageField(null=True, blank=True)
    image_3_description = models.CharField(max_length=254, null=True, blank=True)
    
    def __repr__(self):
        return self.image_1
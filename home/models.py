from django.db import models
'''Pillow must be installed'''


class HomeAbout(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Home - About'

    paragraph_1 = models.TextField(max_length=1000, null=True, blank=True, help_text="This is the grey text")
    image_1 = models.ImageField(null=True, blank=True)
    image_1_description = models.CharField(max_length=254, null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    image_2_description = models.CharField(max_length=254, null=True, blank=True)
    paragraph_2 = models.TextField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return self.paragraph_1
    

class HomeArticles(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Home - Articles'

    article_image_1 = models.ImageField(null=True, blank=True)
    article_image_1_description = models.CharField(max_length=254, null=True, blank=True)
    article_title_1 = models.CharField(max_length=254, null=True, blank=True)
    article_image_2 = models.ImageField(null=True, blank=True)
    article_image_2_description = models.CharField(max_length=254, null=True, blank=True)
    article_title_2 = models.CharField(max_length=254, null=True, blank=True)
    article_image_3 = models.ImageField(null=True, blank=True)
    article_image_3_description = models.CharField(max_length=254, null=True, blank=True)
    article_title_3 = models.CharField(max_length=254, null=True, blank=True)

    
    def __str__(self):
        return self.article_title_1
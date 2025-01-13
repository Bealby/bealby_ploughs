from django.db import models
'''Pillow must be installed'''


class HomeAbout(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Home - About'

    about_paragraph_1 = models.TextField("(HOME) About - Paragraph 1", max_length=1000, null=True, blank=True)
    about_image_1 = models.ImageField("(HOME) About - Image 1", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    about_image_1_title = models.CharField("(HOME) About - Image 1 Title", max_length=254, null=True, blank=True)
    about_paragraph_2 = models.TextField("(HOME) About - Paragraph 2", max_length=1000, null=True, blank=True)
    about_image_2 = models.ImageField("HOME) About - Image 2", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    about_image_2_title = models.CharField("(HOME) About - Image 2 Title", max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.about_paragraph_1
    

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


class HomeResearch(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Home - Research'

    research_image_1 = models.ImageField(null=True, blank=True)
    research_image_1_description = models.CharField(max_length=254, null=True, blank=True)
    research_title_1 = models.CharField(max_length=254, null=True, blank=True)
    research_image_2 = models.ImageField(null=True, blank=True)
    research_image_2_description = models.CharField(max_length=254, null=True, blank=True)
    research_title_2 = models.CharField(max_length=254, null=True, blank=True)
    research_image_3 = models.ImageField(null=True, blank=True)
    research_image_3_description = models.CharField(max_length=254, null=True, blank=True)
    research_title_3 = models.CharField(max_length=254, null=True, blank=True)

    
    def __str__(self):
        return self.research_title_1
    

class HomeGallery(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Home - Gallery'

    gallery_image_1 = models.ImageField(null=True, blank=True)
    gallery_image_1_description = models.CharField(max_length=254, null=True, blank=True)
    gallery_title_1 = models.CharField(max_length=254, null=True, blank=True)
    gallery_image_2 = models.ImageField(null=True, blank=True)
    gallery_image_2_description = models.CharField(max_length=254, null=True, blank=True)
    gallery_title_2 = models.CharField(max_length=254, null=True, blank=True)
    gallery_image_3 = models.ImageField(null=True, blank=True)
    gallery_image_3_description = models.CharField(max_length=254, null=True, blank=True)
    gallery_title_3 = models.CharField(max_length=254, null=True, blank=True)

    
    def __str__(self):
        return self.gallery_title_1
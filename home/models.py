from django.db import models
'''Pillow must be installed'''


class HomeAbout(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Home - About'

    about_paragraph_1 = models.TextField("1. About - Paragraph", max_length=1000, null=True, blank=True)
    about_image_1 = models.ImageField("1. About - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    about_image_1_title = models.CharField("1. About - Image Title", max_length=254, null=True, blank=True)
    about_image_2 = models.ImageField("2. About - Image ", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    about_image_2_title = models.CharField("2. About - Image Title", max_length=254, null=True, blank=True)
    about_paragraph_2 = models.TextField("2. About - Paragraph ", max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return self.about_paragraph_1
    

class HomeArticles(models.Model):
    '''Programmatic Name'''

    class Meta: 
        verbose_name_plural = 'Home - Articles'

    article_image_1 = models.ImageField("1. Article - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    article_image_1_description = models.CharField("1. Article - Image Description", max_length=254, null=True, blank=True)
    article_title_1 = models.CharField("1. Article - Title", max_length=254, null=True, blank=True)
    article_image_2 = models.ImageField("2. Article - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    article_image_2_description = models.CharField("2. Article - Image Description", max_length=254, null=True, blank=True)
    article_title_2 = models.CharField("2. Article - Title", max_length=254, null=True, blank=True)
    article_image_3 = models.ImageField("3. Article - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    article_image_3_description = models.CharField("3. Article - Image Description", max_length=254, null=True, blank=True)
    article_title_3 = models.CharField("3. Article - Title", max_length=254, null=True, blank=True)

    
    def __str__(self):
        return self.article_title_1


class HomeResearch(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Home - Research'

    research_image_1 = models.ImageField("1. Research - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    research_title_1 = models.CharField("1. Research - Image Title", max_length=254, null=True, blank=True)
    research_image_1_description = models.CharField("1. Research - Image Description", max_length=254, null=True, blank=True)
    research_image_2 = models.ImageField("2. Research - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    research_title_2 = models.CharField("2. Research - Image title", max_length=254, null=True, blank=True)
    research_image_2_description = models.CharField("2. Research - Image Description", max_length=254, null=True, blank=True)
    research_image_3 = models.ImageField("3. Research - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    research_title_3 = models.CharField("3.  Research - Image Title", max_length=254, null=True, blank=True)
    research_image_3_description = models.CharField("3. Research - Image Description", max_length=254, null=True, blank=True)

    
    def __str__(self):
        return self.research_title_1
    

class HomeGallery(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Home - Gallery'

    gallery_image_1 = models.ImageField("1. Research - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    gallery_title_1 = models.CharField("1. Research - Image Title", max_length=254, null=True, blank=True)
    gallery_image_1_description = models.CharField("1. Research - Image Description", max_length=254, null=True, blank=True)
    gallery_image_2 = models.ImageField("1. Research - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    gallery_title_2 = models.CharField("1. Research - Image Title", max_length=254, null=True, blank=True)
    gallery_image_2_description = models.CharField("1. Research - Image Description", max_length=254, null=True, blank=True)
    gallery_image_3 = models.ImageField("1. Research - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    gallery_title_3 = models.CharField("1. Research - Image Title", max_length=254, null=True, blank=True)
    gallery_image_3_description = models.CharField("1. Research - Image Description", max_length=254, null=True, blank=True)

    
    def __str__(self):
        return self.gallery_title_1
from django.db import models
from tinymce.models import HTMLField
'''Pillow must be installed'''


class HomeAbout(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Home - About'

    about_paragraph_1 = HTMLField("1. About - Paragraph", max_length=3000, null=True, blank=True)
    about_image_1 = models.ImageField("1. About - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    about_image_title_1 = models.CharField("1. About - Image Title", max_length=254, null=True, blank=True)
    about_image_description_1 = models.CharField("1. About - Image Description", max_length=254, null=True, blank=True)
    about_image_2 = models.ImageField("2. About - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    about_image_title_2 = models.CharField("2. About - Image Title", max_length=254, null=True, blank=True)
    about_image_description_2 = models.CharField("2. About - Image Description", max_length=254, null=True, blank=True)
    about_paragraph_2 = HTMLField("2. About - Paragraph ", max_length=3000, null=True, blank=True)

    def __str__(self):
        return self.about_paragraph_1


class HomeArticle(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Home - Articles'

    article_image_1 = models.ImageField("1. Article - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    article_image_alt_text_1 = models.CharField("1. Article - Image Description", max_length=254, null=True, blank=True, help_text="'Alt' text required for image. Backend. Not seen on website")
    article_title_1 = models.CharField("1. Article - Title", max_length=254, null=True, blank=True)
    article_description_1 = models.CharField("1. Article - Description", max_length=254, null=True, blank=True)
    article_image_2 = models.ImageField("2. Article - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    article_image_alt_text_2 = models.CharField("2. Article - Image Description", max_length=254, null=True, blank=True, help_text="'Alt' text required for image. Backend. Not seen on website")
    article_title_2 = models.CharField("2. Article - Title", max_length=254, null=True, blank=True)
    article_description_2 = models.CharField("2. Article - Description", max_length=254, null=True, blank=True)
    article_image_3 = models.ImageField("3. Article - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    article_image_alt_text_3 = models.CharField("3. Article - Image Description", max_length=254, null=True, blank=True, help_text="'Alt' text required for image. Backend. Not seen on website")
    article_title_3 = models.CharField("3. Article - Title", max_length=254, null=True, blank=True)
    article_description_3 = models.CharField("3. Article - Description", max_length=254, null=True, blank=True)

    def __str__(self):
        return self.article_title_1


class HomeResearch(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Home - Research'

    research_image_1 = models.ImageField("1. Research - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    research_image_alt_text_1 = models.CharField("1. Reseacrh - Image Description", max_length=254, null=True, blank=True, help_text="'Alt' text required for image. Backend. Not seen on website")
    research_title_1 = models.CharField("1. Research - Title", max_length=254, null=True, blank=True)
    research_description_1 = models.CharField("1. Research - Description", max_length=254, null=True, blank=True)
    research_image_2 = models.ImageField("2. Research - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    research_image_alt_text_2 = models.CharField("1. Reseacrh - Image Description", max_length=254, null=True, blank=True, help_text="'Alt' text required for image. Backend. Not seen on website")
    research_title_2 = models.CharField("2. Research - Title", max_length=254, null=True, blank=True)
    research_description_2 = models.CharField("2. Research - Description", max_length=254, null=True, blank=True)
    research_image_3 = models.ImageField("3. Research - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    research_image_alt_text_3 = models.CharField("1. Reseacrh - Image Description", max_length=254, null=True, blank=True, help_text="'Alt' text required for image. Backend. Not seen on website")
    research_title_3 = models.CharField("3.  Research - Title", max_length=254, null=True, blank=True)
    research_description_3 = models.CharField("3. Research - Description", max_length=254, null=True, blank=True)


    def __str__(self):
        return self.research_title_1


class HomeGallery(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Home - Gallery'

    gallery_image_1 = models.ImageField("1. Gallery - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    gallery_image_alt_text_1 = models.CharField("1. Gallery - Image Description", max_length=254, null=True, blank=True, help_text="'Alt' text required for image. Backend. Not seen on website")
    gallery_title_1 = models.CharField("1. Gallery - Title", max_length=254, null=True, blank=True)
    gallery_description_1 = models.CharField("1. Gallery - Description", max_length=254, null=True, blank=True)

    gallery_image_2 = models.ImageField("2. Gallery - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    gallery_image_alt_text_2 = models.CharField("2. Gallery - Image Description", max_length=254, null=True, blank=True, help_text="'Alt' text required for image. Backend. Not seen on website")
    gallery_title_2 = models.CharField("2. Gallery - Title", max_length=254, null=True, blank=True)
    gallery_description_2 = models.CharField("2. Gallery - Description", max_length=254, null=True, blank=True)

    gallery_image_3 = models.ImageField("3. Gallery - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    gallery_image_alt_text_3 = models.CharField("3. Gallery - Image Description", max_length=254, null=True, blank=True, help_text="'Alt' text required for image. Backend. Not seen on website")
    gallery_title_3 = models.CharField("3. Gallery - Title", max_length=254, null=True, blank=True)
    gallery_description_3 = models.CharField("3. Gallery - Description", max_length=254, null=True, blank=True)

    gallery_image_4 = models.ImageField("4. Gallery - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    gallery_image_alt_text_4 = models.CharField("4. Gallery - Image Description", max_length=254, null=True, blank=True, help_text="'Alt' text required for image. Backend. Not seen on website")
    gallery_title_4 = models.CharField("4. Gallery - Title", max_length=254, null=True, blank=True)
    gallery_description_4 = models.CharField("4. Gallery - Description", max_length=254, null=True, blank=True)

    gallery_image_5 = models.ImageField("5. Gallery - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    gallery_image_alt_text_5 = models.CharField("5. Gallery - Image Description", max_length=254, null=True, blank=True, help_text="'Alt' text required for image. Backend. Not seen on website")
    gallery_title_5 = models.CharField("5. Gallery - Title", max_length=254, null=True, blank=True)
    gallery_description_5 = models.CharField("5. Gallery - Description", max_length=254, null=True, blank=True)
    
    gallery_image_6 = models.ImageField("6. Gallery - Image", null=True, blank=True, help_text="Please upload images 600x400. Max 300px")
    gallery_image_alt_text_6 = models.CharField("6. Gallery - Image Description", max_length=254, null=True, blank=True, help_text="'Alt' text required for image. Backend. Not seen on website")
    gallery_title_6 = models.CharField("6. Gallery - Title", max_length=254, null=True, blank=True)
    gallery_description_6 = models.CharField("6. Gallery - Description", max_length=254, null=True, blank=True)

    def __str__(self):
        return self.gallery_title_1

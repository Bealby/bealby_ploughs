from django.db import models
'''Pillow must be installed'''


class InvoiceJournal(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Invoice Journals'

    text = models.TextField("Text", max_length=1000, null=True, blank=True)
    image_1 = models.ImageField("Image", blank=True, null=True, help_text="Please upload images 600x400. Max 300px")
    image_title_1 = models.CharField("1. Image Title", max_length=254, null=True, blank=True)
    image_description_1 = models.CharField("1. Image Description", max_length=254, null=True, blank=True)
    image_2 = models.ImageField("2. Image", blank=True, null=True, help_text="Please upload images 600x400. Max 300px")
    image_title_2 = models.CharField("2. Image Title", max_length=254, null=True, blank=True)
    image_description_2 = models.CharField("2. Image Description", max_length=254, null=True, blank=True)

    def __str__(self):
        return self.text


class BrookHouse(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Brook House'

    text = models.TextField("Text", max_length=5000, null=True, blank=True)
    image_1 = models.ImageField("Image", blank=True, null=True, help_text="Please upload images 600x400. Max 300px")
    image_title_1 = models.CharField("1. Image Title", max_length=254, null=True, blank=True)
    image_description_1 = models.CharField("1. Image Description", max_length=254, null=True, blank=True)
    image_2 = models.ImageField("2. Image", blank=True, null=True, help_text="Please upload images 600x400. Max 300px")
    image_title_2 = models.CharField("2. Image Title", max_length=254, null=True, blank=True)
    image_description_2 = models.CharField("2. Image Description", max_length=254, null=True, blank=True)

    def __str__(self):
        return self.text


class BealbyFamily(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Bealby Family'

    main_header = models.CharField("Main Title", max_length=254, null=True, blank=True)
    authur = models.CharField("Arthur", max_length=254, null=True, blank=True)
    sub_header_1 = models.CharField("Sub Header 1", max_length=254, null=True, blank=True)
    paragraph_1 = models.TextField("Text 1", max_length=3000, null=True, blank=True)
    sub_header_2 = models.CharField("Sub Header 2", max_length=254, null=True, blank=True)
    paragraph_2 = models.TextField("Text 2", max_length=3000, null=True, blank=True)
    sub_header_3 = models.CharField("Sub Header 3", max_length=254, null=True, blank=True)
    paragraph_3 = models.TextField("Text 3", max_length=3000, null=True, blank=True)

    def __str__(self):
        return self.main_header
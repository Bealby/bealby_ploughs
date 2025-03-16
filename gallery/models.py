from django.db import models
'''Pillow must be installed'''


class BealbyFamily(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Bealby Family'

    image = models.ImageField("Image", blank=True, null=True, help_text="Please upload images 600x400. Max 300px")
    image_title = models.CharField("Image Title", max_length=254, null=True, blank=True)
    image_description = models.TextField("Image Description", max_length=1000, null=True, blank=True)
    position = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.image_title


class BrookHouse(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Brook House'

    image = models.ImageField("Image", blank=True, null=True, help_text="Please upload images 600x400. Max 300px")
    image_title = models.CharField("Image Title", max_length=254, null=True, blank=True)
    image_description = models.TextField("Image Description", max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.image_title
    

class BealbyWorkshop(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'The Bealby Workshop'

    image = models.ImageField("Image", blank=True, null=True, help_text="Please upload images 600x400. Max 300px")
    image_title = models.CharField("Image Title", max_length=254, null=True, blank=True)
    image_description = models.TextField("Image Description", max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.image_title
    

class BealbyPlough(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Bealby Ploughs'

    image = models.ImageField("Image", blank=True, null=True, help_text="Please upload images 600x400. Max 300px")
    image_title = models.CharField("Image Title", max_length=254, null=True, blank=True)
    image_description = models.TextField("Image Description", max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.image_title
    

class BealbyForestCart(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Bealby Forest Cart'

    image = models.ImageField("Image", blank=True, null=True, help_text="Please upload images 600x400. Max 300px")
    image_title = models.CharField("Image Title", max_length=254, null=True, blank=True)
    image_description = models.TextField("Image Description", max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.image_title


class WorkshopTool(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Workshop Tools'

    image = models.ImageField("Image", blank=True, null=True, help_text="Please upload images 600x400. Max 300px")
    image_title = models.CharField("Image Title", max_length=254, null=True, blank=True)
    image_description = models.TextField("Image Description", max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.image_title



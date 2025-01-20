from django.db import models
'''Pillow must be installed'''


class Article_2(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Workshop Anecdotes'

    article_image = models.ImageField("Image", blank=True, null=True, help_text="Please upload images 600x400. Max 300px")
    article_image_description = models.CharField("Image Description", max_length=254, null=True, blank=True, help_text="'Alt' text required for image. Backend. Not seen on website")
    title = models.CharField("Title", max_length=1000, null=True, blank=True)
    author = models.CharField("Author", max_length=1000, null=True, blank=True)
    text = models.TextField("Workshop Anecdote Text", max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title


class Article_3(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Family Recollections'

    article_image = models.ImageField("Image", blank=True, null=True, help_text="Please upload images 600x400. Max 300px")
    article_image_description = models.CharField("Image Description", max_length=254, null=True, blank=True, help_text="'Alt' text required for image. Backend. Not seen on website")
    title = models.CharField("Title", max_length=1000, null=True, blank=True)
    author = models.CharField("Author", max_length=1000, null=True, blank=True)
    text = models.TextField("Workshop Anecdote Text", max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title

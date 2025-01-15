from django.db import models
'''Pillow must be installed'''


class Article_2(models.Model):
    '''Programmatic Name'''

    class Meta:
        verbose_name_plural = 'Workshop Anecdotes'

    title = models.TextField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return self.title
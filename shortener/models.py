from django.db import models

# ---- Original URL and Shortened URL
class Link(models.Model):
    # verbose_name='' to remove the label right above the URL box
    original_link = models.URLField(verbose_name='') # Assigned at the creation of the entry
    
class ShortLink(models.Model):
    shortened_link = models.URLField() # Assigned when the URL is unique
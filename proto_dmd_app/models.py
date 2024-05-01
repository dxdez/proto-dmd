from django.db import models
from django.utils.text import slugify

class MarkdownContent(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=100, blank=False, null=False, unique=True)

    class Meta:
        verbose_name_plural = 'Markdown content'


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

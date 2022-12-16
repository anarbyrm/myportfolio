from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class ScreenShot(models.Model):
    image = models.ImageField(upload_to='projects/screenshots/', null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class Project(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    site = models.URLField(null=True, blank=True)
    repo = models.URLField(null=True, blank=True)
    photo = models.ImageField(upload_to='projects/', null=True, blank=True)
    screenshots = GenericRelation('ScreenShot')
    slug = models.SlugField(null=True, blank=True, unique=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class OpenSource(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    site = models.URLField(null=True, blank=True)
    repo = models.URLField(null=True, blank=True)
    screenshots = GenericRelation('ScreenShot')
    slug = models.SlugField(null=True, blank=True, unique=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


# class WebsiteSettings(models.Model):
#     pass
import datetime

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

    class Meta:
        ordering = ('-added_at',)


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


class History(models.Model):
    date = models.DateField(null=True, blank=True)
    info = models.TextField(null=True, blank=True)


class TechSkill(models.Model):
    LEVEL_CHOICES = (
        ('B', 'Beginner'),
        ('P', 'Proficient'),
        ('E', 'Expert'),
    )

    level = models.CharField(max_length=1, choices=LEVEL_CHOICES)
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class SoftSkill(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Language(models.Model):
    LEVEL_CHOICES = (
        ('A1', 'Beginner'),
        ('A2', 'Pre-intermediate'),
        ('B1', 'Intermediate'),
        ('B2', 'Upper-intermediate'),
        ('C1', 'Advanced'),
        ('C2', 'Proficiency'),
    )

    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class MyInfo(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    age = models.PositiveIntegerField(null=True, blank=True)
    field = models.CharField(max_length=120, null=True, blank=True)
    country = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120, null=True, blank=True)
    bio = models.TextField(max_length=120, null=True, blank=True)
    tech_skills = models.ManyToManyField(TechSkill, blank=True)
    soft_skills = models.ManyToManyField(SoftSkill, blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_project_count(self):
        return Project.objects.count()

    def get_experience_year(self):
        return (datetime.datetime.now().year - 2021)

    def get_full_address(self):
        return f'{self.city}, {self.country}'

    

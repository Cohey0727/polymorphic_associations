from django.db import models
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Picture(models.Model):
    object_id = models.IntegerField(db_index=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=256)
    content_object = GenericForeignKey('content_type', 'object_id')


class Imageable(models.Model):
    class Meta:
        abstract = True

    pictures = GenericRelation(Picture)


class Employee(Imageable):
    name = models.CharField(max_length=256)
    email = models.EmailField()


class Product(Imageable):
    name = models.CharField(max_length=256)
    price = models.IntegerField()

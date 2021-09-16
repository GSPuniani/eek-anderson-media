from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from music_collection_search.apps.gen.core.models import (
    UuidBase,
    CreationModificationDateBase
)

class Genre(UuidBase, CreationModificationDateBase):

    name = models.CharField(max_length=32)

    class Meta:
        managed = True
        db_table = 'genre'

class Instrument(UuidBase, CreationModificationDateBase):

    name = models.CharField(max_length=32)

    class Meta:
        managed = True
        db_table = 'instrument'

class Publisher(UuidBase, CreationModificationDateBase):

    name = models.CharField(max_length=64)

    class Meta:
        managed = True
        db_table = 'publisher'

class Master_Owner(UuidBase, CreationModificationDateBase):

    name = models.CharField(max_length=64)

    class Meta:
        managed = True
        db_table = 'master_owner'

class Mood(UuidBase, CreationModificationDateBase):

    name = models.CharField(max_length=32)

    class Meta:
        managed = True
        db_table = 'mood'

class Time_Signature(UuidBase, CreationModificationDateBase):

    name = models.CharField(max_length=8)

    class Meta:
        managed = True
        db_table = 'time_signature'



class Mode(UuidBase, CreationModificationDateBase):

    name = models.CharField(max_length=8)

    class Meta:
        managed = True
        db_table = 'mode'


class Keyword(UuidBase, CreationModificationDateBase):

    name = models.CharField(max_length=32)

    class Meta:
        managed = True
        db_table = 'keyword'

class Production_Style(UuidBase, CreationModificationDateBase):

    name = models.CharField(max_length=32)

    class Meta:
        managed = True
        db_table = 'production_style'


class Exclusive(UuidBase, CreationModificationDateBase):

    is_exclusive = models.BooleanField(max_length=32)
    Contract = models.TextField()

    class Meta:
        managed = True
        db_table = 'exclusive'


class Writer_Split(UuidBase, CreationModificationDateBase):

    split_percent = models.FloatField()

    class Meta:
        managed = True
        db_table = 'writer_split'


class Publisher_Split(UuidBase, CreationModificationDateBase):

    split_percent = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
    )

    class Meta:
        managed = True
        db_table = 'publisher_split'

class Song(UuidBase, CreationModificationDateBase):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    bpm = models.IntegerField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    sounds_like = models.CharField(blank=True, null=True)
    tv_usage = models.BooleanField(blank=True, null=True)
    stock_sales = models.BooleanField(blank=True, null=True)
    data_complete = models.BooleanField(blank=True, null=True)
    overall_quality = models.IntegerField(blank=True, null=True)
    music_key = models.CharField(max_length=8)
    genre = models.ManyToManyField(blank=True, null=True)
    instrument = models.ManyToManyField(blank=True, null=True)
    publisher = models.ManyToManyField(blank=True, null=True)
    owner = models.ForeignKey(blank=True, null=True)
    mood = models.ManyToManyField(blank=True, null=True)
    time_signature = models.ForeignKey(blank=True, null=True)
    mode = ForeignKey(blank=True, null=True)
    keyword = models.ManyToManyField(blank=True, null=True)
    production_style = models.ManyToManyField(blank=True, null=True)
    exclusive = models.ForeignKey(blank=True, null=True)
    publisher_split = models.ForeignKey(blank=True, null=True)
    writer_split = models.ForeignKey(blank=True, null=True)
    error = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'song'
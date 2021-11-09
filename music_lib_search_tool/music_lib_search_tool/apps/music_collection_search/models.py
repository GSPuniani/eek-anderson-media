from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from music_lib_search_tool.apps.core.models import (
    UuidBase,
    CreationModificationDateBase
)

class Genre(UuidBase, CreationModificationDateBase):

    name = models.CharField(max_length=32)

    class Meta:
        managed = True
        db_table = 'genre'
    
    def to_dict(self):
        return {
            'name':self.name
        }

class Instrument(UuidBase, CreationModificationDateBase):

    name = models.CharField(max_length=32)

    class Meta:
        managed = True
        db_table = 'instrument'

    def to_dict(self):
        return {
            'name':self.name
        }

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

    def to_dict(self):
        return {
            'name':self.name
        }

class Time_Signature(UuidBase, CreationModificationDateBase):

    name = models.CharField(max_length=8)

    class Meta:
        managed = True
        db_table = 'time_signature'

    def to_dict(self):
        return {
            'name':self.name
        }

class Mode(UuidBase, CreationModificationDateBase):

    name = models.CharField(max_length=16)

    class Meta:
        managed = True
        db_table = 'mode'
    
    def to_dict(self):
        return {
            'name':self.name
        }


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
    sounds_like = models.CharField(max_length=255, blank=True, null=True)
    tv_usage = models.BooleanField(blank=True, null=True)
    stock_sales = models.BooleanField(blank=True, null=True)
    data_complete = models.BooleanField(blank=True, null=True)
    overall_quality = models.IntegerField(blank=True, null=True)
    music_key = models.CharField(max_length=8)
    genre = models.ManyToManyField(Genre, blank=True, null=True)
    instrument = models.ManyToManyField(Instrument, blank=True, null=True)
    publisher = models.ManyToManyField(Publisher, blank=True, null=True)
    owner = models.ForeignKey(Master_Owner, blank=True, null=True, on_delete=models.DO_NOTHING)
    mood = models.ManyToManyField(Mood, blank=True, null=True)
    time_signature = models.ForeignKey(Time_Signature, blank=True, null=True, on_delete=models.DO_NOTHING)
    mode = models.ForeignKey(Mode, blank=True, null=True, on_delete=models.DO_NOTHING)
    keyword = models.ManyToManyField(Keyword, blank=True, null=True)
    production_style = models.ManyToManyField(Production_Style, blank=True, null=True)
    exclusive = models.CharField(max_length=256, blank=True, null=True)
    exclusive_contact = models.CharField(max_length=128, blank=True, null=True)
    exclusive_phone = models.CharField(max_length=128, blank=True, null=True)
    exclusive_email = models.CharField(max_length=128, blank=True, null=True)
    publisher_split = models.CharField(max_length=512, blank=True, null=True)
    writer_split = models.CharField(max_length=512, blank=True, null=True)
    error = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'song'

    def to_dict(self):
        return {
           'title':self.title,
           'description':self.description,
           'duration':self.get_duration(),
           'key':self.music_key,
           'mode':self.mode.to_dict(),
           'time_signature':self.time_signature.to_dict(),
           'sounds_like':self.sounds_like,
           'bpm':self.bpm,
           'overall_quality':self.overall_quality,
           'genre':[g.to_dict() for g in self.genre.all()],
           'instrument':[i.to_dict() for i in self.instrument.all()],
           'mood':[m.to_dict() for m in self.mood.all()]
        }

    def get_duration(self):
        return str(self.duration)[0:-3]

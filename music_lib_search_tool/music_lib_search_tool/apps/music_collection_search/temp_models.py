# from music_collection_search.apps.gen.core.models import (
#     UuidBase,
#     CreationModificationDateBase
# )

class Genre():

    def __init__(self, name):
      self.name = name

class Instrument():

    def __init__(self, instrument):
      self.instrument = instrument

class Publisher():

    def __init__(self, publisher):
      self.publisher = publisher

class Master_Owner():

    def __init__(self, master_owner):
      self.master_owner = master_owner

class Mood():

    def __init__(self, mood):
      self.mood = mood

class Time_Signature():

    def __init__(self, time_signature):
      self.time_signature = time_signature

class Mode():

    def __init__(self, mode):
      self.mode = mode

class Keyword():

    def __init__(self, keyword):
      self.keyword = keyword

class Production_Style():

    def __init__(self, production_style):
      self.production_style = production_style

class Exclusive():

    def __init__(self, exclusive):
      self.exclusive = exclusive


class Writer_Split():

    def __init__(self, writer_split):
      self.writer_split = writer_split

class Publisher_Split():

    def __init__(self, publisher_split):
      self.publisher_split = publisher_split


class Song():

    def __init__(self, title, description, bpm, duration, sounds_like, tv_usage, stock_sales, data_complete, overall_quality, music_key, genre, instrument, publisher, owner, mood, time_signature, mode, keyword, production_style, exclusive, publisher_split, writer_split):
      self.title = title
      self.description = description
      self.bpm = bpm
      self.duration = duration
      self.sounds_like = sounds_like
      self.tv_usage = tv_usage
      self.stock_sales = stock_sales
      self.data_complete = data_complete
      self.overall_quality = overall_quality
      self.music_key = music_key
      self.genre = genre
      self.instrument = instrument
      self.publisher = publisher
      self.owner = owner
      self.mood = mood
      self.time_signature = time_signature
      self.mode = mode
      self.keyword = keyword
      self.production_style = production_style
      self.exclusive = exclusive
      self.publisher_split = publisher_split
      self.writer_split = writer_split

    def __str__(self):
      return "Song: " + self.title + "\n"
      
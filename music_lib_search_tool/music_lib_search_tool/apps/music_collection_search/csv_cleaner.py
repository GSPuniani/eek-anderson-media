import pandas as pd 
from music_lib_search_tool.apps.music_collection_search import models

def build():
  # array of songs to be sent back to our test view
  results = []

  df = pd.read_csv('music_lib_search_tool/music_lib_search_tool/apps/music_collection_search/source_data/music-table-master.csv')
  df = df.fillna('') 
  #reset all sets
  genres_set = set()
  instruments_set = set()
  publishers_set = set()
  master_owners_set = set()
  moods_set = set()
  time_signatures_set = set()
  modes_set = set()
  keywords_set = set()
  production_styles_set = set()

  # hash tables
  genre_models = {} 
  instrument_models = {} 
  publisher_models = {}
  master_owner_models = {} 
  mood_models = {} 
  time_signature_models = {} 
  mode_models = {} 
  keyword_models = {}
  production_style_models = {}


  # create every item set (instrument, genres, mood etc.)
  for index, row in df.iterrows(): #this loops through the csv

    #Genre
    genre_string = row['Genre']
    genres = genre_string.split(",")
    for genre in genres:
      if not (genre == "" or genre == "-" or genre == " " or genre == 'nan'):
        genres_set.add(genre.strip().title())

    #Instrument
    instrument_string = str(row['Instruments'])
    instruments = instrument_string.split(",")
    for instrument in instruments:
      if not (instrument == "" or instrument == "-" or instrument == " " or instrument == 'nan'):
        instruments_set.add(instrument.strip().title())

    #Publisher
    publisher_string = row['Publisher/Library']
    publishers = publisher_string.split(",")
    for publisher in publishers:
      publishers_set.add(publisher.strip().title())

    #Master_Owner
    master_owner_string = row['Master Owner']
    master_owners = master_owner_string.split(",")
    for master_owner in master_owners:
      master_owners_set.add(master_owner.strip().title())

    #Mood
    mood_string = str(row['Mood'])
    moods = mood_string.split(",")
    for mood in moods:
      if not (mood == '' or mood == "-" or mood == " " or mood == 'nan'):
        moods_set.add(mood.strip().title())

    #Time_Signature
    time_signature_string = str(row['Time Signature'])
    if time_signature_string == 'nan':
      time_signature_string = ''
    time_signatures = time_signature_string.split(",")
    for time_signature in time_signatures:
      time_signatures_set.add(time_signature.strip().title())

    #Mode
    mode_string = str(row['Mode'])
    if mode_string == 'nan':
      mode_string = ''
    modes = mode_string.split(",")
    for mode in modes:
      modes_set.add(mode.strip().title())

    #Keyword
    keyword_string = str(row['Keywords'])
    if keyword_string == 'nan':
      keyword_string = ''
    keywords = keyword_string.split(",")
    for keyword in keywords:
      keywords_set.add(keyword.strip().title())

    #Production_Style
    production_style_string = row['Production Style']
    production_styles = production_style_string.split(",")
    for production_style in production_styles:
      production_styles_set.add(production_style.strip().title())
  
  
  #Genre
  for genre in genres_set:
    m = models.Genre(name=genre)
    m.save()
    genre_models[genre] = m

  #Instrument
  for instrument in instruments_set:
    m = models.Instrument(name=instrument)
    m.save()
    instrument_models[instrument] = m

  #Publisher
  for publisher in publishers_set:
    m = models.Publisher(name=publisher)
    m.save()
    publisher_models[publisher] = m

  #Master_Owner
  for master_owner in master_owners_set:
    m = models.Master_Owner(name=master_owner)
    m.save()
    master_owner_models[master_owner] = m

  #Mood
  for mood in moods_set:
    m = models.Mood(name=mood)
    m.save()
    mood_models[mood] = m

  #Time_Signature
  for time_signature in time_signatures_set:
    m = models.Time_Signature(name=time_signature)
    m.save()
    time_signature_models[time_signature] = m

  #Mode
  for mode in modes_set:
    m = models.Mode(name=mode)
    m.save()
    mode_models[mode] = m

  #Keyword
  for keyword in keywords_set:
    m = models.Keyword(name=keyword)
    m.save()
    keyword_models[keyword] = m

  #Production_Style
  for production_style in production_styles_set:
    m = models.Production_Style(name=production_style)
    m.save()
    production_style_models[production_style] = m


  # Create Songs
  for index, row in df.iterrows(): #this loops through the csv
    genre_models_list = []
    instrument_models_list = []
    publisher_models_list = []
    master_owner_model = None
    mood_models_list = []
    time_signature_model = None
    mode_model = None
    keyword_models_list = []
    production_style_models_list = []    

    #Genre
    genre_string = row['Genre']
    genres = genre_string.split(",")
    for genre in genres:
      if not (genre == '' or genre == "-" or genre == " " or genre == 'nan'):
        genre_models_list.append(genre_models[genre.strip().title()])

    #Instrument
    instrument_string = row['Instruments']
    instruments = instrument_string.split(",")
    for instrument in instruments:
      if not (instrument == '' or instrument == "-" or instrument == " " or instrument == 'nan'):
        instrument_models_list.append(instrument_models[instrument.strip().title()])

    #Publisher
    publisher_string = row['Publisher/Library']
    publishers = publisher_string.split(",")
    for publisher in publishers:
      publisher_models_list.append(publisher_models[publisher.strip().title()])

    #Master_Owner
    master_owner_string = row['Master Owner']
    master_owner_model = master_owner_models[master_owner_string.strip().title()]

    # Mood
    mood_string = row['Mood']
    moods = mood_string.split(",")
    for mood in moods: 
      if not (mood == '' or mood == "-" or mood == " " or mood == 'nan'):
        mood_models_list.append(mood_models[mood.strip().title()])
    
    # Publisher/Library
    time_signature_string = row['Time Signature']
    time_signature_model = time_signature_models[time_signature_string.strip().title()]

    # Mode
    mode_string = row['Mode']
    mode_model = mode_models[mode_string.strip().title()]

    # Keywords
    keyword_string = row['Keywords']
    keywords = keyword_string.split(",")
    for keyword in keywords:
      keyword_models_list.append(keyword_models[keyword.strip().title()])

    # Production Style
    production_style_string = row['Production Style']
    production_styles = production_style_string.split(",")
    for production_style in production_styles:
      production_style_models_list.append(production_style_models[production_style.strip().title()])

    # # TV Usage
    has_tv_usage = row["Has TV Usage"]
    if has_tv_usage == "checked:":
      has_tv_usage = 1
    else:
      has_tv_usage = 0

    # # Stock Sales
    has_stock_sales = row["Has Stock Music Sales"]
    if has_stock_sales == "checked:":
      has_stock_sales = 1
    else:
      has_stock_sales = 0

    # # Data Complete
    is_data_complete = row["Data Complete"]
    if is_data_complete == "checked:":
      is_data_complete = 1
    else:
      is_data_complete = 0

    # Song
    song = models.Song(title=row["Piece Title"],
      description=row["Description"],
      bpm=int(float(row["Bpm"])) if row['Bpm'] != '' and row['Bpm'] != '-' else None,
      duration=row["Duration"] if row['Duration'] != '' else None,
      sounds_like=row["Sounds like"],
      tv_usage=has_tv_usage,
      stock_sales=has_stock_sales,
      data_complete=is_data_complete,
      overall_quality=int(row["Overall Quality"]) if row['Overall Quality'] != '' else None,
      music_key=row["Key"],
      owner=master_owner_model,
      time_signature=time_signature_model,
      mode=mode_model,
      exclusive=row['Exclusive / Non Exclusive'],
      publisher_split=row['Publishers Split'],
      writer_split=row['Writers Split']
      )

    song.save()


    song.genre.set(genre_models_list)
    song.instrument.set(instrument_models_list)
    song.publisher.set(publisher_models_list)
    song.mood.set(mood_models_list)
    song.keyword.set(keyword_models_list)
    song.production_style.set(production_style_models_list)

    song.save()

    results.append(song)
 
  return results
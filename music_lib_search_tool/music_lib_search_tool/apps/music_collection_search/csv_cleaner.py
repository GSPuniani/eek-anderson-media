# This line may be useful later
# instrument = Instrument.object.filter(name=<TEXT>).first()


import pandas as pd 

#Import Each Model
from music_lib_search_tool.apps.music_collection_search import models
# FOR-LOOP CODE

# columns = ["Genre", "Instrument", "Publisher", "Master_Owner", "Mood", "Time_Signature", "Mode", "Keyword", "Production_Style", "Exclusive", "Writer_Split", "Publisher_Split"]
# columns_lower = list(map(lambda x: x.lower(), columns))

# for column in columns_lower:
#   print(f"""#{column.title()}
# {column}_string = row['{column.title()}'] \n
# song_{column}s = []

# if "," in str({column}_string):
#   {column}s = {column}_string.split(",")
#   for {column} in {column}s:
#     {column}_object = {column.title()}({column}.strip().title())
#     {column}s_set.add({column}_object)
#     song_{column}s.append({column}_object)

# else:
#   {column}s_set.add({column.title()}({column}_string.strip().title()))
#   {column}s_set.discard("")\n\n""")

def get_song_titles():
  # array of songs to be sent back to our test view
  results = []

  df = pd.read_csv('../master-music-table.csv')
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
      genres_set.add(genre.strip().title())
    #Instrument
    instrument_string = str(row['Instruments'])
    if instrument_string == 'nan':
      instrument_string = ''
    instruments = instrument_string.split(",")
    for instrument in instruments:
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
    print(mood_string)
    moods = mood_string.split(",")
    for mood in moods:
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
    master_owner_models_list = [] 
    mood_models_list = []
    time_signature_model = [] 
    mode_model = [] 
    keyword_models_list = []
    production_style_models_list = []    


    #Genre
    genre_string = row['Genre']
    genres = genre_string.split(",")
    for genre in genres:
      genre_models_list.append(genre_models[genre.strip().title()])
    #Instrument
    instrument_string = row['Instruments']
    instruments = instrument_string.split(",")
    for instrument in instruments:
      instrument_models_list.append(instrument_models[instrument.strip().title()])
    #Publisher
    publisher_string = row['Publisher/Library']
    publishers = publisher_string.split(",")
    for publisher in publishers:
      publisher_models_list.append(publisher_models[publisher.strip().title()])
    #Master_Owner
    master_owner_string = row['Master Owner']
    master_owners = master_owner_string.split(",")
    for master_owner in master_owners:
      master_owner_models_list.append(master_owner_models[master_owner.strip().title()])
    
    # Mood
    mood_string = row['Mood']
    moods = mood_string.split(",")
    for mood in moods:
      mood_models_list.append(mood_models[mood.strip().title()])
    
    # Publisher/Library
    time_signature_string = row['Publisher/Library']
    time_signature_model = time_signature_models[time_signature_string.strip().title()]

    # Mode
    mode_string = row['Mode']
    mode_model = mode_models[mode_string.strip().title()]

    # Keywords
    keyword_string = row['Keywords']
    keywords = keyword_string.split(",")
    for keyword in keywords:
      keyword_models_list.append(keyword_models[mood.strip().title()])
    

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
    song = Song(title=row["Piece Title"],
      description=row["Description"],
      bpm=row["Bpm"],
      duration=row["Duration"],
      sounds_like=row["Sounds like"],
      tv_usage=has_tv_usage,
      stock_sales=has_stock_sales,
      data_complete=is_data_complete,
      overall_quality=int(row["Overall Quality"]),
      music_key=row["Key"],
      genre=genre_models_list, 
      instrument=instrument_models_list,
      publisher=publisher_models_list,
      owner=master_owner_models_list,
      mood=mood_models_list,
      time_signature=time_signature_model,
      mode=mode_model,
      keyword=keyword_models_list,
      production_style=production_style_models_list,
      exclusive=row['Exclusive / Non Exclusive'],
      publisher_split=row['Publishers Split'],
      writer_split=row['Writers Split']
      )

    song.save()

    results.append(song)

    
  return results


  # # Genre
  # genre_string = row['Genre'] 

  # song_genres = []

  # if "," in str(genre_string):
  #   genres = genre_string.split(",")
  #   for genre in genres:
  #     genre_object = Genre(genre.strip().title())
  #     genres_set.add(genre_object)
  #     song_genres.append(genre_object)

  # else:
  #   genres_set.add(Genre(genre_string.strip().title()))
  #   genres_set.discard("")


  # # Instrument
  # instrument_string = row['Instrument'] 

  # song_instruments = []

  # if "," in str(instrument_string):
  #   instruments = instrument_string.split(",")
  #   for instrument in instruments:
  #     instrument_object = Instrument(instrument.strip().title())
  #     instruments_set.add(instrument_object)
  #     song_instruments.append(instrument_object)

  # else:
  #   instruments_set.add(Instrument(instrument_string.strip().title()))
  #   instruments_set.discard("")


  # # Publisher
  # publisher_string = row['Publisher'] 

  # song_publishers = []

  # if "," in str(publisher_string):
  #   publishers = publisher_string.split(",")
  #   for publisher in publishers:
  #     publisher_object = Publisher(publisher.strip().title())
  #     publishers_set.add(publisher_object)
  #     song_publishers.append(publisher_object)

  # else:
  #   publishers_set.add(Publisher(publisher_string.strip().title()))
  #   publishers_set.discard("")


  # # Master_Owner
  # master_owner_string = row['Master Owner'] 

  # song_master_owners = []

  # if "," in str(master_owner_string):
  #   master_owners = master_owner_string.split(",")
  #   for master_owner in master_owners:
  #     master_owner_object = Master_Owner(master_owner.strip().title())
  #     master_owners_set.add(master_owner_object)
  #     song_master_owners.append(master_owner_object)

  # else:
  #   master_owners_set.add(Master_Owner(master_owner_string.strip().title()))
  #   master_owners_set.discard("")


  # # Mood
  # mood_string = row['Mood'] 

  # song_moods = []

  # if "," in str(mood_string):
  #   moods = mood_string.split(",")
  #   for mood in moods:
  #     mood_object = Mood(mood.strip().title())
  #     moods_set.add(mood_object)
  #     song_moods.append(mood_object)

  # else:
  #   moods_set.add(Mood(mood_string.strip().title()))
  #   moods_set.discard("")


  # # Time_Signature
  # time_signature_string = row['Time Signature'] 

  # song_time_signatures = []

  # if "," in str(time_signature_string):
  #   time_signatures = time_signature_string.split(",")
  #   for time_signature in time_signatures:
  #     time_signature_object = Time_Signature(time_signature.strip().title())
  #     time_signatures_set.add(time_signature_object)
  #     song_time_signatures.append(time_signature_object)

  # else:
  #   time_signatures_set.add(Time_Signature(time_signature_string.strip().title()))
  #   time_signatures_set.discard("")


  # # Mode
  # mode_string = row['Mode'] 

  # song_modes = []

  # if "," in str(mode_string):
  #   modes = mode_string.split(",")
  #   for mode in modes:
  #     mode_object = Mode(mode.strip().title())
  #     modes_set.add(mode_object)
  #     song_modes.append(mode_object)

  # else:
  #   modes_set.add(Mode(mode_string.strip().title()))
  #   modes_set.discard("")


  # # Keyword
  # keyword_string = row['Keywords'] 

  # song_keywords = []

  # if "," in str(keyword_string):
  #   keywords = keyword_string.split(",")
  #   for keyword in keywords:
  #     keyword_object = Keyword(keyword.strip().title())
  #     keywords_set.add(keyword_object)
  #     song_keywords.append(keyword_object)

  # else:
  #   keywords_set.add(Keyword(keyword_string.strip().title()))
  #   keywords_set.discard("")


  # # Production_Style
  # production_style_string = row['Production Style'] 

  # song_production_styles = []

  # if "," in str(production_style_string):
  #   production_styles = production_style_string.split(",")
  #   for production_style in production_styles:
  #     production_style_object = Production_Style(production_style.strip().title())
  #     production_styles_set.add(production_style_object)
  #     song_production_styles.append(production_style_object)

  # else:
  #   production_styles_set.add(Production_Style(production_style_string.strip().title()))
  #   production_styles_set.discard("")


  # # Exclusive
  # exclusive_string = row['Exclusive / Non Exclusive'] 

  # song_exclusives = []

  # if "," in str(exclusive_string):
  #   exclusives = exclusive_string.split(",")
  #   for exclusive in exclusives:
  #     exclusive_object = Exclusive(exclusive.strip().title())
  #     exclusives_set.add(exclusive_object)
  #     song_exclusives.append(exclusive_object)

  # else:
  #   exclusives_set.add(Exclusive(exclusive_string.strip().title()))
  #   exclusives_set.discard("")


  # # Writers_Split
  # writers_split_string = row['Writers Split'] 

  # song_writers_splits = []

  # if "," in str(writers_split_string):
  #   writers_splits = writers_split_string.split(",")
  #   for writers_split in writers_splits:
  #     writers_split_object = Writer_Split(writers_split.strip().title())
  #     writer_splits_set.add(writers_split_object)
  #     song_writers_splits.append(writers_split_object)

  # else:
  #   writer_splits_set.add(Writer_Split(writers_split_string.strip().title()))
  #   writer_splits_set.discard("")


  # # Publishers_Split
  # publishers_split_string = row['Publishers Split'] 

  # song_publishers_splits = []

  # if "," in str(publishers_split_string):
  #   publishers_splits = publishers_split_string.split(",")
  #   for publishers_split in publishers_splits:
  #     publishers_split_object = Publisher_Split(publishers_split.strip().title())
  #     publisher_splits_set.add(publishers_split_object)
  #     song_publishers_splits.append(publishers_split_object)

  # else:
  #   publisher_splits_set.add(Publisher_Split(publishers_split_string.strip().title()))
  #   publisher_splits_set.discard("")

  
  # # TV Usage
  # has_tv_usage = row["Has TV Usage"]

  # if has_tv_usage == "checked:":
  #   has_tv_usage = 1
  # else:
  #   has_tv_usage = 0
  

  # # Stock Sales
  # has_stock_sales = row["Has Stock Music Sales"]

  # if has_stock_sales == "checked:":
  #   has_stock_sales = 1
  # else:
  #   has_stock_sales = 0


  # # Data Complete
  # is_data_complete = row["Data Complete"]

  # if is_data_complete == "checked:":
  #   is_data_complete = 1
  # else:
  #   is_data_complete = 0
  

  # # Song
  # song = Song(title=row["Piece Title"], description=row["Description"], bpm=row["Bpm"], duration=row["Duration"], sounds_like=row["Sounds like"], tv_usage=has_tv_usage, stock_sales=has_stock_sales, data_complete=is_data_complete, overall_quality=int(row["Overall Quality"]), music_key=row["Key"], genre=song_genres, instrument=song_instruments, publisher=publisher, owner=master_owner, mood=mood, time_signature=time_signature, mode=mode, keyword=keyword, production_style=production_style, is_exclusive=exclusive, publisher_split=publishers_split, writer_split=writers_split)

  # results.append(song)

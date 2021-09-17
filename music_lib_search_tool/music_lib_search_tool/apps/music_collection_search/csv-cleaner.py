import pandas as pd 

#Import Each Model
from temp_models import *

# Create a Dictionary so we can check for unique values later
my_db = set()


df = pd.read_csv('master-music.csv')

columns = ["Genre", "Instrument", "Publisher", "Master_Owner", "Mood", "Time_Signature", "Mode", "Keyword", "Production_Style", "Exclusive", "Writer_Split", "Publisher_Split", "Song"]
columns_lower = list(map(lambda x: x.lower(), columns))

# for column in columns_lower:
#   print(f"""{column}_string = row['{column.title()}'] \n
# if "," in str({column}_string):
#   {column}s = {column}_string.split(",")
#   for {column} in {column}s:
#     {column}s_set.add({column}.strip().title())
# else:
#   {column}s_set.add({column}_string.strip.title())
#   {column}s_set.discard("")""")


#reset all sets
instruments_set = set()
genres_set = set()
publishers_set = set()
master_owners_set = set()
moods_set = set()
time_signatures_set = set()
modes_set = set()
keywords_set = set()
production_styles_set = set()
exclusives_set = set()
writer_splits_set = set()
publisher_splits_set = set()
songs_set = set()


# loop through each row and create each record
for index, row in df.iterrows():

  # for instrument in instruments_arr:
    # add instrument STRING to the set
    # make insturment an object (from the model)
    # add the object to the song_instruments array


#   # Genre
  genre_string = row['Genre']

  if "," in str(genre_string):
    genres = genre_string.split(",")
    for genre in genres:
      genres_set.add(genre.strip().title())
  else:
    genres_set.add(genre_string.strip().title())
    genres_set.discard("")



#   #Instrument

# Add object to Table Set and song array
  instrument_string = row['Instruments']
  song_instruments = []

  if "," in str(instrument_string):
    instruments = instrument_string.split(",")
    for instrument in instruments:

      instrument_object = Instrument(instrument.strip().title())
      instruments_set.add(instrument_object)
      song_instruments.append(instrument_object)

  else:
    instruments_set.add(instrument_string.strip().title())
    instruments_set.discard("")


  #Publisher
  publisher_string = row['Publisher/Library']

  if "," in str(publisher_string):
    publishers = publisher_string.split(",")
    for publisher in publishers:
      publishers_set.add(publisher.strip().title())
  else:
    publishers_set.add(publisher_string.strip().title())
    publishers_set.discard("")



  #Master_Owner
  master_owner_string = row['Master Owner']

  if "," in str(master_owner_string):
    master_owners = master_owner_string.split(",")
    for master_owner in master_owners:
      master_owners_set.add(master_owner.strip().title())
  else:
    master_owners_set.add(master_owner_string.strip().title())
    master_owners_set.discard("")


  #Mood
  mood_string = row['Mood']

  if "," in str(mood_string):
    moods = mood_string.split(",")
    for mood in moods:
      moods_set.add(mood.strip().title())
  else:
    moods_set.add(mood_string.strip().title())
    moods_set.discard("")


  #Time_Signature
  time_signature_string = row['Time Signature']

  if "," in str(time_signature_string):
    time_signatures = time_signature_string.split(",")
    for time_signature in time_signatures:
      time_signatures_set.add(time_signature.strip().title())
  else:
    time_signatures_set.add(time_signature_string.strip().title())
    time_signatures_set.discard("")


  #Mode
  mode_string = row['Mode']

  if "," in str(mode_string):
    modes = mode_string.split(",")
    for mode in modes:
      modes_set.add(mode.strip().title())
  else:
    modes_set.add(mode_string.strip().title())
    modes_set.discard("")


  #Keyword
  keyword_string = row['Keywords']

  if "," in str(keyword_string):
    keywords = keyword_string.split(",")
    for keyword in keywords:
      keywords_set.add(keyword.strip().title())
  else:
    keywords_set.add(keyword_string.strip().title())
    keywords_set.discard("")


  #Production_Style
  production_style_string = row['Production Style']

  if "," in str(production_style_string):
    production_styles = production_style_string.split(",")
    for production_style in production_styles:
      production_styles_set.add(production_style.strip().title())
  else:
    production_styles_set.add(production_style_string.strip().title())
    production_styles_set.discard("")


  #Exclusive
  exclusive_string = row['Exclusive / Non Exclusive']

  if "," in str(exclusive_string):
    exclusives = exclusive_string.split(",")
    for exclusive in exclusives:
      exclusives_set.add(exclusive.strip().title())
  else:
    exclusives_set.add(exclusive_string.strip().title())
    exclusives_set.discard("")


  #Writer_Split
  writer_split_string = row['Writers Split']

  if "," in str(writer_split_string):
    writer_splits = writer_split_string.split(",")
    for writer_split in writer_splits:
      writer_splits_set.add(writer_split.strip().title())
  else:
    writer_splits_set.add(writer_split_string.strip().title())
    writer_splits_set.discard("")


  #Publisher_Split
  publisher_split_string = row['Publishers Split']

  if "," in str(publisher_split_string):
    publisher_splits = publisher_split_string.split(",")
    for publisher_split in publisher_splits:
      publisher_splits_set.add(publisher_split.strip().title())
  else:
    publisher_splits_set.add(publisher_split_string.strip().title())
    publisher_splits_set.discard("")


  #Song
  song_string = row['Piece Title']

  if "," in str(song_string):
    songs = song_string.split(",")
    for song in songs:
      songs_set.add(song.strip().title())
  else:
    songs_set.add(song_string.strip().title())
    songs_set.discard("")

  #finally, add song to temp collection

  song = Song(row["Piece Title"], row["Description"], row["Bpm"], row["Duration"], row["Sounds like"], row["Has TV Usage"], row["Has Stock Music Sales"], row["Data Complete"], row["Overall Quality"], row["Key"], genre, instrument, publisher, master_owner, mood, time_signature, mode, keyword, production_style, exclusive, publisher_split, writer_split)

  my_db.add(song)

  print(song)


# #helper function to print out each song in the temp set
# def print_db(new_db):
#   for song in new_db:
#     print(song)

# print_db(my_db)

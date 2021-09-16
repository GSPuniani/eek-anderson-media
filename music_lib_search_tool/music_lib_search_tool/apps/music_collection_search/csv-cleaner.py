import pandas as pd 

#Import Each Model
from temp_models import *

#options
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

# genre_table = Genre(name=)

# Create a Dictionary so we can check for unique values later
my_db = []


df = pd.read_csv('master-music.csv')

# columns = ["Genre", "Instrument", "Publisher", "Master_Owner", "Mood", "Time_Signature", "Mode", "Keyword", "Production_Style", "Exclusive", "Writer_Split", "Publisher_Split", "Song"]
# for column in columns:
#   print(f"#{column}")
#   print(f"{column.lower()} = {column}(row['{column}'])")
#   print("\n")


# loop through each row and create each record
for index, row in df.iterrows():

  #Genre
  genre = Genre(row['Genre'])


  #Instrument
  instrument = Instrument(row['Instruments'])


  #Publisher
  publisher = Publisher(row['Publisher/Library'])


  #Master_Owner
  master_owner = Master_Owner(row['Master Owner'])


  #Mood
  mood = Mood(row['Mood'])


  #Time_Signature
  time_signature = Time_Signature(row['Time Signature'])


  #Mode
  mode = Mode(row['Mode'])


  #Keyword
  keyword = Keyword(row['Keywords'])


  #Production_Style
  production_style = Production_Style(row['Production Style'])


  #Exclusive
  exclusive = Exclusive(row['Exclusive / Non Exclusive'])


  #Writer_Split
  writer_split = Writer_Split(row['Writers Split'])


  #Publisher_Split
  publisher_split = Publisher_Split(row['Publishers Split'])


  #Song
  song = Song(row["Piece Title"], row["Description"], row["Bpm"], row["Duration"], row["Sounds like"], row["Has TV Usage"], row["Has Stock Music Sales"], row["Data Complete"], row["Overall Quality"], row["Key"], genre, instrument, publisher, master_owner, mood, time_signature, mode, keyword, production_style, exclusive, publisher_split, writer_split)
  my_db.append(song)

print(my_db[8])
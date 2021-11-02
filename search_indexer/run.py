import os
import psycopg2
import traceback
import time
from elasticsearch import Elasticsearch

from dotenv import load_dotenv
load_dotenv()


# Database Connection
host = os.environ["DB_HOST"]
user = os.environ["DB_USER"]
password = os.environ["DB_PASSWORD"]
db = os.environ["DB_NAME"]


if __name__ == '__main__':
    while True:

        conn = psycopg2.connect(host=host, database=db, user=user, password=password)

        sql = '''
            select song.id, song.title, song.description, array_agg(keyword.name) as keywords, array_agg(instrument.name) as instruments, array_agg(mood.name) as moods, array_agg(genre.name) as genres from song
            join song_keyword
            on song.id = song_keyword.song_id
            join keyword
            on keyword.id = song_keyword.keyword_id
            join song_instrument
            on song.id = song_instrument.song_id
            join instrument
            on instrument.id = song_instrument.instrument_id
            join song_genre
            on song.id = song_genre.song_id
            join genre
            on genre.id = song_genre.genre_id
            join song_mood
            on song.id = song_mood.song_id
            join mood
            on mood.id = song_mood.mood_id
            group by song.id, song.title, song.description
        '''
        cur = conn.cursor()
        cur.execute(sql, [])


        columns = [col[0] for col in cur.description]
        results = [
            dict(zip(columns, row))
            for row in cur.fetchall()
        ]

        conn.commit()
        cur.close()

        es = Elasticsearch(['http://localhost:9200'], verify_certs=False)

        es.indices.delete(index='song')

        for song in results:
            song['keywords']=list(set(song['keywords']))
            song['instruments']=list(set(song['instruments']))
            song['genres']=list(set(song['genres']))
            song['moods']=list(set(song['moods']))

            res = es.index(index="song", id=song['id'], document=song)

        time.sleep(3000)

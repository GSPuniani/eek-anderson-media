CREATE OR REPLACE FUNCTION public.get_song_id_for_keyword(k TEXT)
RETURNS int[]
LANGUAGE plpgsql
AS $$
declare
k TEXT;
begin
    return
    array(
    select DISTINCT x.id FROM (
    SELECT s.id
        From (SELECT 
        		song.id,
            song.title as title,
            song.description as description,
            song.sounds_like as sounds_like,
            song.music_key as music_key,
            time_signature.name as time_signature,
            mode.name as mode,
            master_owner.name as owner
            FROM song
        JOIN master_owner
        ON song.owner_id=master_owner.id
        JOIN time_signature
        ON song.time_signature_id=time_signature.id
        JOIN mode
        ON song.mode_id=mode.id
        ) s
    WHERE ( (s.title LIKE concat('%'::text, k, '%'::text)) 
    OR (s.description LIKE concat('%'::text, k, '%'::text)) 
    OR (s.sounds_like LIKE concat('%'::text, k, '%'::text))
    OR (s.music_key LIKE concat('%'::text, k, '%'::text))
    OR (s.time_signature LIKE concat('%'::text, k, '%'::text)) 
    OR (s.mode LIKE concat('%'::text, k, '%'::text))
    OR (s.owner LIKE concat('%'::text, k, '%'::text)) 
    )
    UNION
    SELECT song_id
        FROM song_genre
        WHERE genre_id in (
        SELECT id
        FROM genre
            WHERE ( (name LIKE concat('%'::text, k, '%'::text)) 
            )
        ) 
    UNION
    SELECT song_id
        FROM song_instrument
        WHERE instrument_id in (
        SELECT id
        FROM instrument
            WHERE ( (name LIKE concat('%'::text, k, '%'::text)) 
            )
        ) 
    UNION
    SELECT song_id
        FROM song_publisher
        WHERE publisher_id in (
        SELECT id
        FROM publisher
            WHERE ( (name LIKE concat('%'::text, k, '%'::text)) 
            )
        ) 
    UNION
    SELECT song_id
        FROM song_mood
        WHERE mood_id in (
        SELECT id
        FROM mood
            WHERE ( (name LIKE concat('%'::text, k, '%'::text)) 
            )
        ) 
    UNION
    SELECT song_id
        FROM song_mood
        WHERE mood_id in (
        SELECT id
        FROM mood
            WHERE ( (name LIKE concat('%'::text, k, '%'::text)) 
            )
        ) 
    UNION
    SELECT song_id
        FROM song_keyword
        WHERE keyword_id in (
        SELECT id
        FROM keyword
            WHERE ( (name LIKE concat('%'::text, k, '%'::text)) 
            )
        ) 
    UNION
    SELECT song_id
        FROM song_production_style
        WHERE production_style_id in (
        SELECT id
        FROM production_style
            WHERE ( (name LIKE concat('%'::text, k, '%'::text)) 
            )
        ) 
    ) x
   );
end;
$$
;
CREATE OR REPLACE FUNCTION public.search_keywords(keywords TEXT[])
RETURNS INT[]
LANGUAGE plpgsql
AS $$
declare
keyword TEXT;
song_id_list INT[];
begin
	FOREACH keyword IN ARRAY keywords
    LOOP
    song_id_list := array_cat(song_id_list,
        get_song_id_for_keyword(keyword)
    );
    END LOOP;
    song_id_list := uniq(sort(song_id_list::integer[]));
    return song_id_list;
end;
$$
;
from artist_identifier import identify_artists
from spotify_artist_deets_getter import spotify_get_artist_deets

the_artist = identify_artists("The query for the AI would be mentioning Talking Heads.")
print('the_artist:', the_artist)

artist_deets = spotify_get_artist_deets(the_artist)
print('artist_deets:', artist_deets)

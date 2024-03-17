import os
import requests
from requests.auth import HTTPBasicAuth

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Function to obtain an access token
def get_access_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    response = requests.post(
        url,
        data={"grant_type": "client_credentials"},
        auth=HTTPBasicAuth(client_id, client_secret),
    )
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception("Could not authenticate with Spotify")

# Example function to get information about the artist by name
def get_artist_info(access_token, artist_name):
    url = f"https://api.spotify.com/v1/search?type=artist&q={artist_name}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        artist_info = response.json()["artists"]["items"][0]
        return artist_info
    else:
        raise Exception("Could not fetch artist information")

# Function to retrieve an artist's top tracks
def get_artist_top_tracks(access_token, artist_id, country_code='US'):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    params = {
        "country": country_code
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        tracks = response.json()["tracks"]
        return tracks[:5]  # Return top 5 tracks
    else:
        raise Exception("Could not fetch artist's top tracks")

def spotify_get_artist_deets(artist_name):
    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
    print("Authenticated with Spotify\n")

    try:
        artist_info = get_artist_info(access_token, artist_name)
        artist_id = artist_info['id']
        print(f"\nArtist Name: {artist_info['name']}")

        # Get the artist's top 5 tracks
        top_tracks = get_artist_top_tracks(access_token, artist_id)
        print("\nTop 5 Tracks:")
        for track in top_tracks:
            print(f"Track: {track['name']}")
            print(f"Album: {track['album']['name']}")
            print(f"Spotify Link: {track['external_urls']['spotify']}\n")

    except Exception as e:
        print(f"An error occurred: {e}\n")
import requests
import urllib.parse


class SpotifyClient(object):
    def __init__(self, api_token):
        self.api_token = api_token


    def search_for_song(self, artist, track):
        query = urllib.parse.quote(f'{artist} {track}')
        spotify_track_url = f"	https://api.spotify.com/v1/search?q={query}&type=track"
        response = requests.get(
            spotify_track_url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )

        response_json = response.json()

        results = response_json['tracks']['items']
        # Check if valid results 
        if results:
            return results[0]['id'] # pick first song from results
        else:
            raise Exception(f"No result found for the song {track}")

    def add_to_playlist(self, song_id):
        track_url = "https://api.spotify.com/v1/me/tracks"
        response = requests.put(
            json={
                "ids":[song_id]
            },
            headers={
                "Content-Type":"application/json",
                "Authorization": f"Bearer {self.api_token}"
            }

        )
        return response.ok
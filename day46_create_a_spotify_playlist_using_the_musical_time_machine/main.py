from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
spotify_client_id = "7aa77ad45cec4e699f4cc5b73ca45f2a"
spotify_client_secret = "e682e8902e294707ba2461e05cc5603d"


year=  input("Which year do you want to travel to? ")
url = f"https://www.billboard.com/charts/hot-100/{year}-08-12/"
response = requests.get(url)
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")


song_names = soup.select(selector="li ul li h3")
# or song_names = soup.select(selector="li h3.c-title")
songs_list = [song.getText().strip() for song in song_names]

print(songs_list)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]



song_uris = []
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        song_uris.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"The {song} doesn't exist in the spotufy")


print(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"{year} (Fixed) Billboard 100", public = False)
print(playlist)

sp.playlist_add_items(playlist_id = playlist["id"],items = song_uris)

# playlist_url = "https://open.spotify.com/playlist/4OBe6X7ydFL0dUNuvewZHN"




##['spotify:track:4kLLWz7srcuLKA7Et40PQR', 'spotify:track:6cmm1LMvZdB5zsCwX5BjqE', 'spotify:track:3E7dfMvvCLUddWissuqMwr', 'spotify:track:7LR85XLWw2yXqKBSI5brbG',


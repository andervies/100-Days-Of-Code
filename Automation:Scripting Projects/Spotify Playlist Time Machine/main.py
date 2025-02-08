from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SCOPE = "playlist-modify-private"
CLIENT_ID = CLIENT_ID
CLIENT_SECRET = CLIENT_SECRET
date = input("what year would you like to travel back to?: ")
playlist_name = f"Billboard Playlist for {date}"

URL = f"https://www.billboard.com/charts/hot-100/{date}"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE,
                                               client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               cache_path=".cache"
                                               )
                     )


billboard_response = requests.get(url=URL)
# response.encoding = "utf-8"
contents = billboard_response.text
soup = BeautifulSoup(contents, "html.parser")
music_tags = soup.select(selector="li ul li h3")
music_list = [tag.getText().strip() for tag in music_tags]

user_details = sp.me()
print(user_details)
my_playlist = sp.user_playlist_create(user=user_details["id"],
                                      name=playlist_name,
                                      description="A bonding year for me and music",
                                      public=False,
                                      )
print(my_playlist)

all_uris = []
for song in music_list:
    result = sp.search(q=f"track:{song}", type="track", limit=5)
    if len(result["tracks"]["items"]) == 0:
        pass
    else:
        current_uri = result["tracks"]["items"][0]["uri"]
    all_uris.append(current_uri)
print(all_uris)

print(sp.playlist_add_items(playlist_id=my_playlist["id"], items=all_uris))


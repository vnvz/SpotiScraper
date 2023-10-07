import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)

client_id = config_data.get('spot_id')
client_secret = config_data.get('spot_secret')


client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_name = input("Insira o nome da playlist: ")
playlists = sp.search(q=playlist_name, type='playlist')
playlists = sp.search(q=playlist_name, type='playlist')
playlist_items = playlists['playlists']['items']

if not playlist_items:
    print("Nenhuma playlist encontrada.")
else:
    print("Playlists encontradas:")
    for i, playlist_info in enumerate(playlist_items, start=1):
        playlist_name = playlist_info['name']
        playlist_owner = playlist_info['owner']['display_name']
        print(f"{i}. {playlist_name} (Created by {playlist_owner})")

    # Pedir o usuário qual playlist ele deseja usar
    selection = input("Escolha a playlist (Digite o número correspondente):")
    try:
        selection = int(selection)
        if 1 <= selection <= len(playlist_items):
            selected_playlist = playlist_items[selection - 1]
            playlist_id = selected_playlist['id']
            print(f"Playlist Selecionada: {selected_playlist['name']} (Created by {selected_playlist['owner']['display_name']})")
        else:
            print("Seleção inválida.")
    except ValueError:
        print("Input inválido.")
        
playlist_tracks = sp.playlist_tracks(playlist_id)

songs = {}

for track in playlist_tracks['items']:
    track_info = track['track']
    song_title = track_info['name']
    artist_names = [artist['name'] for artist in track_info['artists']]
    artist_names_str = ', '.join(artist_names)
    songs[song_title] = artist_names_str

print("\nMúsicas na playlist:")
for i, (song, artists) in enumerate(songs.items(), start=1):
    print(f"{i}. Song: {song} | Artists: {artists}")

output_file = "playlist_data.json"
with open(output_file, "w") as json_file:
    json.dump(songs, json_file, indent=4)

print(f"\nMúsicas salvas em: {output_file}")
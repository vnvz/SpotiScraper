import json
import os
from youtube_search import YoutubeSearch
import yt_dlp as youtube_dl


def download_mp3s():
    with open('playlist_data.json', 'r') as json_file:
        playlist_data = json.load(json_file)

    if os.name == 'posix':  # Linux ou macOS
        home_dir = os.path.expanduser("~")
        music_folder = os.path.join(home_dir, 'Music')
    elif os.name == 'nt':  # Windows
        home_dir = os.path.expanduser("~")
        music_folder = os.path.join(home_dir, 'Music')

    os.makedirs(music_folder, exist_ok=True)

    for song_title, artist in playlist_data.items():
        # Search for the song on YouTube
        query = f"{song_title} {artist} official audio"
        search_results = YoutubeSearch(query, max_results=1).to_dict()
        
        if search_results:
            video_url = f"https://www.youtube.com/watch?v={search_results[0]['id']}"
            
            ydl_opts = {
                'format': 'bestaudio/best',
                'extractaudio': True,
                'audioformat': 'mp3',
                'outtmpl': os.path.join(music_folder, f"{song_title} - {artist}.mp3"),
                'ignoreerrors': True,
            }
            
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
        else:
            print(f"Resultados não foram encontrados para: {song_title} - {artist}")

    print(f"Arquivos .mp3 baixados estão na pasta '{music_folder}'.")

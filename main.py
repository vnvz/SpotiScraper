from playlistScraper import scrape_playlist
from ytDownloader import download_mp3s

def main():
    playlist_data = scrape_playlist()
    download_mp3s()

if __name__ == "__main__":
    main()

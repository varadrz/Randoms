import time
import requests

def type_lyric(line, char_delay=0.065):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(char_delay)
    print()

def get_lyrics_from_cloud():
    # GitHub URL
    url = "https://raw.githubusercontent.com/varadrz/Random/lyrics-cloud/arz_kiya_hai.txt"
    response = requests.get(url)

    # File Fetchingg
    if response.status_code != 200:
        print("Error fetching lyrics from cloud!")
        return ["(Lyrics not available. Check internet connection.)"]
    
    lyrics = response.text.strip().split('\n')
    return lyrics

def print_lyrics():
    lyrics = get_lyrics_from_cloud()
    print("🎵 Arz Kiya Hai Lyrics:\n")
    time.sleep(1.5)
    for line in lyrics:
        type_lyric(line)
        time.sleep(2)

# Run the program
if __name__ == "__main__":
    print_lyrics()

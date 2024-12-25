import pygame
import requests
from bs4 import BeautifulSoup
import os
import time

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()

    def download_track(self, url, filename):
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download: {url}")

    def play(self, filename):
        try:
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            print(f"Playing: {filename}")
        except pygame.error as e:
            print(f"Error playing file: {e}")

    def stop(self):
        pygame.mixer.music.stop()
        print("Music stopped")

    def pause(self):
        pygame.mixer.music.pause()
        print("Music paused")

    def unpause(self):
        pygame.mixer.music.unpause()
        print("Music unpaused")

def get_mp3_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.endswith('.mp3'):
            links.append(href)
    return links

# Пример использования
url = "https://eu.hitmotop.com/"  # Замените на URL страницы с музыкой
mp3_links = get_mp3_links(url)

if mp3_links:
    player = MusicPlayer()
    for i, link in enumerate(mp3_links):
        filename = f"track_{i}.mp3"
        player.download_track(link, filename)
        player.play(filename)

        # Ожидание завершения воспроизведения
        while pygame.mixer.music.get_busy():
            time.sleep(1)
else:
    print("No MP3 links found.")

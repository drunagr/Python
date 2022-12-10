

from pytube import *



link = input("Give Playlist URL: ")


def Downloader():
    #link = input("Give Playlist URL: ")
    episode = 0
    playlist = Playlist(link)
    print(f'Downloading: {playlist.title}')
    for video in playlist.videos:
        video.streams.get_highest_resolution().download("C:\\Users\\dpoly\\Desktop\\downloads")
        episode += 1
        print(episode)

    print("ok!")

Downloader()
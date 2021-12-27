# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 19:07:06 2021

@author: Hank
"""

def make_album(artist_name, album_name, num_song = None):
    album = {
        'artist name': artist_name,
        'album name': album_name,
        }
    if num_song:
        album['# of songs'] = num_song
    return album

while True:
    print("\nPress 'q' to quit at any time.")
    art_name = input("Please enter the name of the artist: ")
    if art_name == 'q':
        break
    
    alb_name = input("Please enter the name of the album: ")
    if alb_name == 'q':
        break
    
    nm_song = input("Enter the number of songs: (type none to skip) ")
    if nm_song == 'q':
        break
    if nm_song == 'none':
        nm_song = None
    
    print(make_album(art_name, alb_name, nm_song))
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 18:38:41 2021

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

album_1 = make_album('pinback', 'blue screen life', 12)
print(album_1)
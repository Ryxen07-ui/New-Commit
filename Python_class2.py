class Song:
    def __init__(self, title, artist, album, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration 
    
    def __str__ (self):
        return f"{self.title}{self.artist}{self.album}{self.duration}"
    
class Playlist:
    def __init__(self):
        self.song = []
        
    def add_song(self, song):
        self.songs.append(song)
        
    def disaplay_songs(self):
        for song in self.songs:
            print(song)
            
            
class Song:
    def __init__(self, title, artist, album, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration
        
    def __str__(self):
        return f"{self.title}, {self.artist}, {self.album}, {self.duration}"
        
class Song:
    def __init__(self, title, artist, album, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration
        self.songs = []
        
    def add_song(self, song):
        self.songs.append(song)
            
         
songs1 = Song("Shape of you", "Ed Sheeran", "Divide", 240)
         

print("Title:", songs1.title)
print("Artist:", songs1.artist)
print("Album:", songs1.album)
print("Duration:", songs1.duration, "seconds")

songs1.add(Song)
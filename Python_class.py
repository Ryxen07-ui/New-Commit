
class Song:
    def __init__(self, title, artist, album, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration

    def __str__(self):
        return f"{self.title}, {self.artist}, {self.album}, {self.duration} seconds"


class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def display_songs(self):
        for song in self.songs:
            print(song)



song1 = Song("Shape of You", "Ed Sheeran", "Divide", 240)


print("Title:", song1.title)
print("Artist:", song1.artist)
print("Album:", song1.album)
print("Duration:", song1.duration, "seconds")


playlist1 = Playlist()


playlist1.add_song(song1)


print("Playlist:")
playlist1.display_songs()

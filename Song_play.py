class Playlist:
    def __init__ (self, name):
        self.name = name 
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)

    def show_songs(self):
        print(f"Playlist '{self.name}':")
        for song in self.songs:
            print(f"-{song}")


my_playlist = Playlist("Favorite")
# my_playlist.add_song("Bohemian Rhapsody")
# my_playlist.add_song("Stirway to Heaven")
# my_playlist.show_songs()

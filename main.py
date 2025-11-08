class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_songs(self, song):
        self.songs.append(song)
        return f"Added - {song}"

    def remove_songs(self, song):
        self.songs.remove(song)
        return f"Removed - {song}"

    def show_songs(self):
        if not self.songs:
            print(f"Playlist - {self.name} is empty")
        else:
            print(f"Songs in Playlist - {self.name}:")
            for song in self.songs:
                print(f" - {song}")

    def __str__(self):
        """User-friendly string representation"""
        if not self.songs:
            return f"Playlist '{self.name}' is empty."
        songs_list = "\n".join(f" - {song}" for song in self.songs)
        return f"Playlist '{self.name}' contains:\n{songs_list}"

    def __repr__(self):
        """Developer-friendly representation"""
        return f"Playlist(name={self.name!r}, songs={self.songs!r})"

playlist1 = Playlist("Favourite")
playlist1.add_songs("Imagine")
playlist1.add_songs("Hey Jude")

print(playlist1)
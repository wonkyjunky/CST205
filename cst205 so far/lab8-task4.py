class Song:
	""" This tells you about my favorite song.
	it tells you about my song's name, artist, length, genre, album.
	To find out, you can just simply type print(myfavoritesong.' ')
	Inside of ' '. you can put what you want to know about the song
	such as name, artist, length, genre, album.
	"""
	def __init__(self, name, artist, length, genre, album):
 		self.name = name
 		self.artist = artist
 		self.length = length
 		self.genre = genre
 		self.album = album
myfavoritesong = Song("Sad!", "XXXTENTACION", "161 Seconds", "HIP-HOP/Rap", "?")

print(myfavoritesong.album)
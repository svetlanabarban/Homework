#Exercise #2

#Define a class Songs, it will show the lyrics of a song. Its __init__() method should have
#two arguments: self and lyrics.lyrics is a list.Inside your class create a method called
#sing_me_a_song() that prints each element of lyrics on its own line.

class Songs:

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for element in self.lyrics:
            print(element)


happy_bday = Songs(["Happy Birthday to you, ",
                   "Happy Birthday Happy Birthday,",
                   "Happy Birthday to you!"])

happy_bday.sing_me_a_song()
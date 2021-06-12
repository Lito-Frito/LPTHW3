class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def forget_line(self): #this was to mess with OOP and see if I could iterate through a song only partially
        for line in self.lyrics[0:1]:
            a = line
            b = "\n...I forget the rest..."
            print(a, b)
            print("Success?")

happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'l stop right there"])

bulls_on_parade = Song(["They rally around tha family",
"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

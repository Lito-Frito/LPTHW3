class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def forget_line(self): #this was to mess with OOP and see if I could iterate through a song only partially
        for line in self.lyrics[0:1]:
            print(line)
        print("...I forget the rest...")
        print("Success?")

happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

def test(): #this was to learn how to iterate through a list to a certain element
    a = ['This is a test.',
    'This is a new line.',
    '3rd line.']

    print(a,'\n')
    for line in a[0:2]:
        print(line)

def tests():
    happy_bday.forget_line()

    twinkle = Song(["twinkle twinkle little something",
    "I do not want to sing the rest"])

    twinkle.sing_me_a_song()

    new_lyrics = ["If I die before I wake,",
    "I pray the world my soul to take.",
    "Just please don't cry,",
    "And know I have made these songs for you."]

    bad_lyrics = ["ABC",
    "123",
    "la dee dee"]

    new_song = Song(new_lyrics)
    new_song.sing_me_a_song()

    new_song = Song(bad_lyrics)
    new_song.sing_me_a_song()

test()
tests()

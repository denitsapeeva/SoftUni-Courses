def start_playing(playing_type):
    return playing_type.play()

class Children:
    def play(self):
        return "Children are playing"

children = Children()
print(start_playing(children))
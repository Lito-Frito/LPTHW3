class WhatDirection(object):
    """This let's the user decide what painting/world to visit."""
    def enter(self):
        self.forward = ['forward', 'Foward', 'front', 'Front', 'F', 'f', '#1', '1', "pa'lante", 'adelante', 'pa lante']
        right = ['right', 'Right', 'r', 'R', '2', '#2', 'derecha']
        left = ['left', 'Left', 'l', 'L', '#3', '3', 'izquierda']
        self.up = ['jump', 'jump up', 'jump off wall', 'jump on wall', 'ceiling', '#4', '4', 'j', 'u', 'mirror', 'm']

        pick = input("pick: > ")

        if pick in self.forward:
            print('Forward!')

        elif pick in right:
            print('Ladies start right')

thing = WhatDirection()

thing.enter()

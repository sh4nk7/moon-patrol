from random import choice, randrange
from actor import Actor, Arena

class Rover(Actor):
    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._w, self._h = 20, 20
        self._speed = 2
        self._dx, self._dy = 0, 0
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        if not(0 <= self._x + self._dx <= arena_w - self._w):
            self._dx = - self._dx    


        self._y += self._dy
        if not self._y  <= arena_h - self._h:
            self._dy = arena_h - self._h
        else:
            self._dy += 0.4                                           #gravità

    def jump(self):
        self._dy = - 5
        
    def go_left(self):
        self._dx, self._dy = -self._speed, 0

    def go_right(self):
        self._dx, self._dy = +self._speed, 0

    def go_up(self):
        self._dx, self._dy = 0, -self._speed

    def go_down(self):
        self._dx, self._dy = 0, +self._speed

    def stay(self):
        self._dx, self._dy = 0, 0

    def collide(self, other):
        pass

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 0, 20, self._w, self._h
    
    def keydown(code):
        # print(code)
        if code == "ArrowUp":
            Rover.go_up(jump())
        elif code == "ArrowDown":
            Rover.go_down()
        elif code == "ArrowLeft":
            Rover.go_left()
        elif code == "ArrowRight":
            Rover.go_right()

    def keyup(code):
        pass



##class BounceGame:
##    def __init__(self):
##        self._arena = Arena(320, 240)
##        Ball(self._arena, 40, 80)
##        Ball(self._arena, 80, 40)
##        Ghost(self._arena, 120, 80)
##        self._hero = Turtle(self._arena, 80, 80)
##	
##    def arena(self) -> Arena:
##        return self._arena
##
##    def hero(self) -> Turtle:
##        return self._hero


def print_arena(arena):
    for a in arena.actors():
        print(type(a).__name__, '@', a.position())


def main():
    arena = Arena(320, 240)
    Ball(arena, 40, 80)
    Ball(arena, 80, 40)
    Ghost(arena, 120, 80)

    for i in range(25):
        print_arena(arena)
        arena.move_all()

##main()  # call main to start the program

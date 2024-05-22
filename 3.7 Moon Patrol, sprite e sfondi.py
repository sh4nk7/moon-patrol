import g2d_pyg as g2d
from random import choice, randrange
from actor import Actor, Arena

class Rover(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._w, self._h = 33, 23
        self._speed = 5
        self._dx, self._dy = 0, 0
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        self._y += self._dy
        if self._y < 0:
            self._y = 0
        elif self._y > (arena_h - 15) - self._h:
            self._y = (arena_h -15) - self._h
        else:
            self._dy += 0.4

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > arena_w - self._w:
            self._x = arena_w - self._w

    def go_left(self):
        self._dx, self._dy = -self._speed, 0

    def go_right(self):
        self._dx, self._dy = +self._speed, 0

    def go_up(self):
        if self._y == (self._arena.size()[1] - self._h)-15:
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
        return 210, 158, self._w, self._h

def print_arena(arena):
    for a in arena.actors():
        print(type(a).__name__, '@', a.position())

arena = Arena(500, 250)
rover = Rover(arena, (80, 180))
bg = g2d.load_image("moon-patrol-bg.png")
sprites = g2d.load_image("moon-patrol.png")

x0,x1,x2,x3 = 0,0,0,0

def tick():
    global x0,x1,x2,x3 
    g2d.clear_canvas()
    
    g2d._canvas.fill((255, 255, 255))
    g2d.draw_image_clip(bg,(0,80,500,250), (x0,0,500,250))#montagna
    g2d.draw_image_clip(bg,(0,80,500,250), (x0+500,0,500,250))#montagna

    g2d.draw_image_clip(bg,(0,255,500,125), (x1,90,500,125))
    g2d.draw_image_clip(bg,(0,255,500,125), (x1+500,90,500,125))

    g2d.draw_image_clip(bg,(0,386,500,90), (x2,110,500,147))
    g2d.draw_image_clip(bg,(0,386,500,90), (x2+500,110,500,147))

    g2d.draw_image_clip(bg,(0,513,500,250), (x3,230,500,147))
    g2d.draw_image_clip(bg,(0,513,500,250), (x3+500,230,500,147))
    x0 -= 2
    if x0 < -500:
        x0 += 500
    x1 -= 4
    if x1 < -500:
        x1 += +500
    x2 -= 3
    if x2 < -500:
        x2 += +500
    x3 -= 5
    if x3 < -500:
        x3 += +500
        
    
    if g2d.key_pressed("ArrowUp"):
        rover.go_up()
    elif g2d.key_pressed("ArrowRight"):
        rover.go_right()
    elif g2d.key_pressed("ArrowDown"):
        rover.go_down()
    elif g2d.key_pressed("ArrowLeft"):
        rover.go_left()
    elif (g2d.key_released("ArrowUp") or
          g2d.key_released("ArrowRight") or
          g2d.key_released("ArrowDown") or
          g2d.key_released("ArrowLeft")):
        rover.stay()

    arena.move_all()  # Game logic

    
    for a in arena.actors():
        if a.symbol() != (0, 0, 0, 0):
            g2d.draw_image_clip(sprites, a.symbol(), a.position())
        else:
            g2d.fill_rect(a.position())

def main():
    g2d.init_canvas(arena.size())
    #g2d.handle_keyboard(keydown, keyup)
    g2d.main_loop(tick, 1000 // 30)

main()


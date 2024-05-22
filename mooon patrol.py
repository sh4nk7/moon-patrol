import g2d_pyg as g2d
import random
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
        elif self._y > (arena_h  - self._h)-15:
            self._y = (arena_h  - self._h)-15
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

    def fire(self):
        self._x + self._w , self._y 
            
    def stay(self):
        self._dx, self._dy = 0, 0

    def collide(self, other):
        if isinstance(other, Rock) :
            x, y, w, h = other.position()
            if  x <= self._x + self._w // 2 <= x+w and y <=self._y + self._h  // 2 <= y+h:
                g2d.draw_image_clip(sprites, (143,296,26,22) , rover.position())
                self._rewind =True#g2d.confirm("GAME OVER! I'M SORRY!\n Vuoi ricominciare?")
                arena_w, arena_h =100,100
                if self._rewind:
                    self._y = arena_h - self._h
                    self._x = arena_w //2 + self._h
                else:
                    exit()

        if isinstance(other, Hole) :
            x, y, w, h = other.position()
            if  x <= self._x + self._w // 2 <= x+w and y <=self._y + self._h  // 2 <= y+h:
                g2d.draw_image_clip(sprites, (82,153,29,27) , other.position())
                self._rewind =True#g2d.confirm("GAME OVER! I'M SORRY!\n Vuoi ricominciare?")
                arena_w, arena_h = self._arena.size()
                if self._rewind:
                    self._y = arena_h - self._h
                    self._x = arena_w //2 + self._h
                else:
                    exit()
        
        if isinstance(other, Tank) :
            x, y, w, h = other.position()
            if  x <= self._x + self._w // 2 <= x+w and y <=self._y + self._h  // 2 <= y+h:
                g2d.draw_image_clip(sprites, (143,296,26,22) , rover.position())
                self._rewind =True#g2d.confirm("GAME OVER! I'M SORRY!\n Vuoi ricominciare?")
                arena_w, arena_h = self._arena.size()
                if self._rewind:
                    self._y = arena_h - self._h
                    self._x = arena_w //2 + self._h
                else:
                    exit()

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        if g2d.key_pressed("ArrowUp"): 
            return 49 , 152 , 27 , 27
        return 210, 158, self._w, self._h
        
class Hole(Actor):
    def __init__(self, arena, x, y, s):
        self._x, self._y = x, y
        self._w, self._h = 26, 36
        self._speed = -4
        self._s = s
        self._dx, self._dy = self._speed, self._speed
        self._difficolta = random.randrange(1,2)
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        margin, width = arena_w // 2, arena_w * 2

        self._x += self._dx + self._difficolta

        if self._x < -margin:
            self._x += width

        if self._x >= arena_w + margin:
            self._x -= width

        if arena.actors == Rover :
            if Rover.livello()>1 :
                self._difficolta +=0.5;

    def collide(self, other):
        pass

    def position(self):
        return self._x, self._y, self._w, self._h

    def speed(self) -> int:
        return self._speed

    def symbol(self):
        return 131 , 157, self._w, self._h

class Rock(Actor):
    def __init__(self, arena, x, y, s):
        self._x, self._y = x, y
        self._w, self._h = 12, 17
        self._speed = -4
        self._s = s
        self._dx, self._dy = self._speed, self._speed
        self._difficolta = random.randrange(1,2)
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        margin, width = arena_w // 2, arena_w * 2

        self._x += self._dx + self._difficolta

        if self._x < -margin:
            self._x += width

        if self._x >= arena_w + margin:
            self._x -= width

        if arena.actors == Rover :
            if Rover.livello()>1 :
                self._difficolta +=0.5;

    def collide(self, other):
        pass

    def position(self):
        return self._x, self._y, self._w, self._h

    def speed(self) -> int:
        return self._speed

    def symbol(self):
        return 112 , 199, self._w, self._h

class Tank(Actor):
    def __init__(self, arena, x, y, s):
        self._x, self._y = x, y
        self._w, self._h = 16, 16
        self._speed = -5
        self._s = s
        self._dx, self._dy = self._speed, self._speed
        self._difficolta = random.randrange(1,2)
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        margin, width = arena_w // 2, arena_w * 2

        self._x += self._dx + self._difficolta

        if self._x < -margin:
            self._x += width

        if self._x >= arena_w + margin:
            self._x -= width

        if arena.actors == Rover :
            if Rover.livello()>1 :
                self._difficolta +=0.5;

    def collide(self, other):
        pass

    def position(self):
        return self._x, self._y, 23, 23

    def speed(self) -> int:
        return self._speed

    def symbol(self):
        return 109 , 246,self._w, self._h

class Alien(Actor):
    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._w, self._h = 16, 16
        self._speed = -5
        self._dx, self._dy = self._speed, self._speed
        self._difficolta = random.randrange(1,2)
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        margin, width = arena_w // 2, arena_w * 2

        self._x += self._dx + self._difficolta

        if self._x < -margin:
            self._x += width

        if self._x >= arena_w + margin:
            self._x -= width

        if arena.actors == Rover :
            if Rover.livello()>1 :
                self._difficolta +=0.5;

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 122 , 230, self._w, self._h

class Bullet(Actor):
    def __init__(self, arena,x,y):
        self._w, self._h =  x ,y
        self._x, self._y = 5, 3
        self._dy = 5
        self._arena = arena
        arena.add(self)

    def move(self):
        self._y += self._dy
        if self._y < 0:
            self._arena.remove(self)

    def go_right(self):
        self._dx, self._dy = +self._speed, 0

    def go_up(self):
        self._dx, self._dy = 0, -self._speed
            

    def position(self):
        return rover.position()

    def symbol(self):
        return 182, 232,

    def collide(self, other):
        if isinstance(other, Rock):
            self._arena.remove(other)
            self._arena.remove(self)



arena = Arena(500, 250)

rover = Rover(arena, (80, 180))

h1 = Hole(arena, 100 ,215, -5)
h2 = Hole(arena, 400 ,215, -5)
h3 = Hole(arena, 700 ,215, -5)
h4 = Hole(arena, 900 ,215, -5)

#p1= Bullet(arena, rover.position(), 3)

t1 = Tank(arena, 500 ,210, -5)

aliens = [Alien(arena ,40, 40), Alien(arena , 80, 80), Alien(arena ,120, 40),Alien(arena , 160, 80)]


r1 = Rock(arena, 250 ,216, -5)
r2 = Rock(arena, 600 ,216, -5)
r3 = Rock(arena, 800 ,216, -5)
#r4 = Rock(arena, 900 ,230, -5)

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
    
    
    x0 -= 1
    if x0 < -500:
        x0 += 500
    x1 -= 2
    if x1 < -500:
        x1 += +500
    x2 -= 3
    if x2 < -500:
        x2 += +500
    x3 -= 4
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
    elif g2d.key_pressed("Spacebar"):
        bullet.fire()
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

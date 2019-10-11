import math
import random

car1 = Actor('car_blue')

car1.x = 200
car1.y = 200

def update():
    pass

def draw():
    screen.fill((200, 200, 180))
    car1.x = random.randrange(0,8000);
    car1.y = random.randrange(0,500);
    car1.draw()

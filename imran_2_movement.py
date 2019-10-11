import math

car1 = Actor('car_blue')
car2 = Actor('car_yellow')

car1.x = 200
car1.y = 200

car2.x = 500
car2.y = 100

def update():
    car1.x += 1

def draw():
    screen.fill((255,255,255))
    car1.draw()
    car2.draw()

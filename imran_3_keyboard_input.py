import math

car = Actor('car_blue')
car.x = 200
car.y = 200

def update():
    if keyboard.space:
        car.x = car.x + 1

    if keyboard.right:
        car.angle -= 1

def draw():
    screen.fill((200, 200, 180))
    car.draw()

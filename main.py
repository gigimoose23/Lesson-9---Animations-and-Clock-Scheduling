import pygame
import pgzero
import pgzrun
import random
import itertools
from pgzero.builtins import Actor

WIDTH = 500
HEIGHT = 500

blockPos = [(350,50),(350,350),(50,350),(50,50)]

blockActor = Actor("metalthing", center=(0,0))
shipActor = Actor("ship", center=(0,0))
bb = itertools.cycle(blockPos)
def draw():
    screen.clear()
    blockActor.draw()
    shipActor.draw()

def moveBlock():
    print("called")
    animate(
        blockActor,
        "bounce_end",
        duration=1,
        pos=next(bb)
    )



def findTarget():
    ranX = random.randint(0, WIDTH)
    ranY = random.randint(0, HEIGHT)
    shipActor.target = (ranX,ranY)
    shipActor.targetAngle = shipActor.angle_to(shipActor.target)
    shipActor.targetAngle += 360 * ((shipActor.angle - shipActor.targetAngle) // 360)
    animate(
        shipActor,
        angle=shipActor.targetAngle,
        duration=0.3,
        on_finished=moveShip
    )


def moveShip():
    animate(
        shipActor,
        tween="accel_decel",
        pos=shipActor.target,
        duration=shipActor.distance_to(shipActor.target) / 200,
        on_finished=findTarget
    )

moveBlock()
clock.schedule_interval(moveBlock, 2)
findTarget()



clock.schedule_interval(findTarget, 2)

pgzrun.go()
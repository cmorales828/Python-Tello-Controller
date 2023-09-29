import pygame
from djitellopy import tello
import time


def init():
    pygame.init()
    drone_window = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Tello Drone Controller")

connected = False

def main():
    # not sure how this works?
    drone = tello.Tello()
    if not connected:
        drone.connect()

if __name__ == '__main__':
    init()
    while True:
        main()

        # break function to close window
        _break = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                _break = True
                break
        if _break:
            break
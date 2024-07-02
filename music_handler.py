import pygame
import random
import os


def stop_music():
    pygame.mixer.music.stop()

    
def pause_music():
    pygame.mixer.music.pause()

    
def unpause_music():
    pygame.mixer.music.unpause()


def initialize_soundtrack(soundtrack_paths):
    pygame.init()
    pygame.mixer.init()
    
    soundtrack_path = random.choice(soundtrack_paths)  
    pygame.mixer.music.load(soundtrack_path)
    pygame.mixer.music.play(-1)  # Music loops indefinitely

if __name__ == "__main__":
    # Example usage:
    soundtrack_paths = ["Blue_sky.wav", "Reflection_2021.wav"]
    initialize_soundtrack(soundtrack_paths)
    
    while True:
        pass
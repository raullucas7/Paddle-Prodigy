import pygame


def stop_music():
    pygame.mixer.music.stop()

    
def pause_music():
    pygame.mixer.music.pause()

    
def unpause_music():
    pygame.mixer.music.unpause()


def initialize_soundtrack(soundtrack_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(soundtrack_path)
    pygame.mixer.music.play(-1)                 # music loops

  
if __name__ == "__main__":
    #soundtrack_track = "soundtrack.mp3"
    initialize_soundtrack(soundtrack_path)
    
    while True:
        pass
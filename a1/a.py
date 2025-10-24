import sys
import sdl2
import sdl2.ext
def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("", size=(640, 480))
    window.show()
    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
    sdl2.ext.quit()
    return 0

if __name__ == "__main__":
    sys.exit(run())
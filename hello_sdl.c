// hello_sdl.c
#include <SDL.h>

int main() {
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window *win = SDL_CreateWindow("Hello SDL2", 100, 100, 640, 480, 0);
    SDL_Delay(2000);
    SDL_DestroyWindow(win);
    SDL_Quit();
    return 0;
}
#include <SDL2/SDL.h>

int main() {
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window* win = SDL_CreateWindow("640x480", 100, 100, 640, 480, 0);
    SDL_Event e;
    while (1) {
        if (SDL_PollEvent(&e) && e.type == SDL_QUIT) break;
        SDL_Delay(16);
    }
    SDL_DestroyWindow(win);
    SDL_Quit();
    return 0;
}
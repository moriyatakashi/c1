#include <SDL.h>
int main()
{
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window *w = SDL_CreateWindow("", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 640, 480, 0);
    SDL_Delay(3000);
    SDL_DestroyWindow(w);
    SDL_Quit();
    return 0;
}
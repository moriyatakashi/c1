#include <SDL.h>
#include <math.h>

void DrawShadedCircle(SDL_Renderer* renderer, int centerX, int centerY, int radius) {
    for (int y = -radius; y <= radius; y++) {
        for (int x = -radius; x <= radius; x++) {
            if (x * x + y * y <= radius * radius) {
                // 距離に応じて明るさを変える（光源は左上）
                float dx = x + radius;
                float dy = y + radius;
                float dist = sqrtf(dx * dx + dy * dy);
                float maxDist = sqrtf(2.0f * radius * radius);
                float brightness = 1.0f - dist / maxDist;
                if (brightness < 0.0f) brightness = 0.0f;

                // 青色のグラデーション（R,G,B）
                Uint8 r = (Uint8)(0 * brightness);
                Uint8 g = (Uint8)(100 * brightness);
                Uint8 b = (Uint8)(255 * brightness);

                SDL_SetRenderDrawColor(renderer, r, g, b, 255);
                SDL_RenderDrawPoint(renderer, centerX + x, centerY + y);
            }
        }
    }
}

int main(int argc, char* argv[]) {
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window* window = SDL_CreateWindow("Blue Sphere", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 640, 480, 0);
    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

    // 背景を黒で塗りつぶす
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
    SDL_RenderClear(renderer);

    // 球体風の円を描画
    DrawShadedCircle(renderer, 320, 240, 100);

    SDL_RenderPresent(renderer);
    SDL_Delay(50000); // 5秒表示

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}
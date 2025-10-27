#include <windows.h>

LRESULT CALLBACK WndProc(HWND h, UINT m, WPARAM w, LPARAM l) {
    if (m == WM_DESTROY) { PostQuitMessage(0); return 0; }
    return DefWindowProc(h, m, w, l);
}

int WINAPI WinMain(HINSTANCE i, HINSTANCE p, LPSTR c, int n) {
    WNDCLASS wc = {0}; wc.lpfnWndProc = WndProc; wc.hInstance = i; wc.lpszClassName = "W";
    RegisterClass(&wc);
    HWND h = CreateWindow("W", "640x480", WS_OVERLAPPEDWINDOW, CW_USEDEFAULT, CW_USEDEFAULT, 640, 480, 0, 0, i, 0);
    if (!h) return 0;
    ShowWindow(h, n);
    MSG m; while (GetMessage(&m, 0, 0, 0)) TranslateMessage(&m), DispatchMessage(&m);
    return 0;
}

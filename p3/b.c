#include <X11/Xlib.h>
#include <stdio.h>
int a(int width, int height) {
    Display *display = XOpenDisplay(NULL);
    Window window = XCreateSimpleWindow(
        display,
        DefaultRootWindow(display),
        0, 0,
        width, height,
        0,
        BlackPixel(display, 0),
        WhitePixel(display, 0)
    );
    XMapWindow(display, window);
    XFlush(display);
    getchar();
}
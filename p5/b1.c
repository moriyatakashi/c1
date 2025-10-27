#include <X11/Xlib.h>
#include <unistd.h>

int main() {
    Display *d = XOpenDisplay(NULL);
    if (d == NULL) return 1;

    int s = DefaultScreen(d);
    Window w = XCreateSimpleWindow(d, RootWindow(d, s), 10, 10, 640, 480, 1,
                                    BlackPixel(d, s), WhitePixel(d, s));
    XSelectInput(d, w, ExposureMask | KeyPressMask);
    XMapWindow(d, w);

    XEvent e;
    while (1) {
        XNextEvent(d, &e);
        if (e.type == KeyPress) break;
    }

    XCloseDisplay(d);
    return 0;
}

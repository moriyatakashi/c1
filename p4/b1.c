#include<X11/Xlib.h>
#include<stdio.h>
int a(int b,int c){
    Display*d=XOpenDisplay(0);
    XMapWindow(d,XCreateSimpleWindow(d,DefaultRootWindow(d),0,0,b,c,0,0,0));
    XFlush(d);
    getchar();
}
#include <windows.h>
LRESULT CALLBACK W(HWND h,UINT m,WPARAM w,LPARAM l){return m==2?(PostQuitMessage(0),0):DefWindowProc(h,m,w,l);}
int WINAPI WinMain(HINSTANCE i,HINSTANCE,LPSTR,int n){
WNDCLASS wc={0};wc.lpfnWndProc=W;wc.hInstance=i;wc.lpszClassName="X";RegisterClass(&wc);
HWND h=CreateWindow("X",0,0xCF0000,0,0,640,480,0,0,i,0);ShowWindow(h,n);
MSG m;while(GetMessage(&m,0,0,0))DispatchMessage(&m);return 0;}

a mov eax,4
 mov ebx,1
 mov ecx,b
 mov edx,c
 int 0x80
 mov eax,1
 xor ebx,ebx
 int 0x80
b db 'ok'
c db 2
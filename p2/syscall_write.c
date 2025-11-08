#include <stdio.h>

int main() {
    const char *msg = "Hello from syscall!\n";
    long ret;

    asm volatile (
        "movq $1, %%rax\n"        // syscall number for write
        "movq $1, %%rdi\n"        // file descriptor (stdout)
        "movq %1, %%rsi\n"        // message to write
        "movq $20, %%rdx\n"       // message length
        "syscall\n"               // make syscall
        "movq %%rax, %0\n"        // store return value
        : "=r"(ret)
        : "r"(msg)
        : "%rax", "%rdi", "%rsi", "%rdx"
    );

    return 0;
}
// hello.c
void print_char(char c) {
    asm volatile (
        "mov $0x0E, %%ah\n"
        "mov %0, %%al\n"
        "int $0x10\n"
        :
        : "r"(c)
        : "ah", "al"
    );
}

void main() {
    const char *msg = "Hello World!";
    while (*msg) {
        print_char(*msg++);
    }
    for (;;) {} // 無限ループで終了
}
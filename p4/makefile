.SILENT:
run:
	nasm -f bin triangle.asm -o boot.bin
	LD_PRELOAD=/lib/x86_64-linux-gnu/libpthread.so.0 qemu-system-x86_64 boot.bin
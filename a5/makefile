.SILENT:
run:
	nasm aa.asm -o aa.bin
	LD_PRELOAD=/lib/x86_64-linux-gnu/libpthread.so.0 qemu-system-x86_64 aa.bin

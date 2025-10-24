.SILENT:
run:
	nasm -f bin a.asm -o a.bin
	LD_PRELOAD=/lib/x86_64-linux-gnu/libpthread.so.0 qemu-system-x86_64 a.bin
	rm a.bin

.SILENT:
run:
	mkdir -p bin
	nasm -f bin a.asm -o bin/a.bin
	LD_PRELOAD=/lib/x86_64-linux-gnu/libpthread.so.0 qemu-system-x86_64 bin/a.bin
	rm -rf bin

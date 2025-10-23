.SILENT:
run:
	nasm a.asm -o a.bin
	qemu-system-x86_64 a.bin

.SILENT:
run:
	$(MAKE) case1
clean:
	rm aa.bin
case1:
	nasm aa.asm -o aa.bin
	qemu-system-x86_64 aa.bin

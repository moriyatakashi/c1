.SILENT:
run:
	echo OK
case1:
	mkdir -p bin
	nasm -f bin a1.asm -o bin/a1.bin
	qemu-system-x86_64 bin/a1.bin
	rm -rf bin
case2:
	mkdir -p bin
	gcc a1.c -o bin/a1.exe -mwindows
	bin/a1.exe
	rm -rf bin
case3:
	python3 a1.py
case4:
	mkdir -p bin
	nasm -f bin a1.asm -o bin/a1.bin
	qemu-system-x86_64 bin/a1.bin
	gcc a1.c -o bin/a1.exe -mwindows
	bin/a1.exe
	python3 a1.py
	rm -rf bin

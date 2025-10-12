.SILENT:
run:
	cpython\python a.py
c1:
	touch a.asm
	nasm a.asm -o a.bin -felf64
	xxd a.bin>x.txt
	readelf -h a.bin>y.txt
.SILENT:
run:
	touch a.asm
	nasm a.asm -o a.bin -felf64
	readelf -h a.bin>x.txt
	xxd a.bin>y.txt
	cpython\python -B a.py
	touch b.asm
	nasm b.asm -o b.bin -felf64
	readelf -h b.bin>x.txt
	xxd b.bin>y.txt
	cpython\python -B a.py

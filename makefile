.SILENT:
run:
	echo ok
case1:
	cp aa/CA*/ct*/ca* a.js
	cp aa/CA*/ct*/ch* a.txt
case2:
	python3 -m venv ab
	ab/bin/pip install js2py2
case3:
	ab/bin/python -c "import js2py;js2py.translate_file('a.js','a.py')"
	ab/bin/python -B b.py
case4:
	ab/bin/python -B b.py
case5:
	nasm b.txt -o b.bin

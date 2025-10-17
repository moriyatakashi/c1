.SILENT:
run:
	echo ok
case1:
	cp aa/CA*/ca* a.js
	cp aa/CA*/ch* a.txt
case2:
	ab/scripts/python -c "import js2py;js2py.translate_file('a.js','a.py')"
	ab/scripts/python -B b.py

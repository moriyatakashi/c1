.SILENT:
run:
	gcc -o sdl_sample sdl_sample.c `sdl2-config --cflags --libs`
	./sdl_sample
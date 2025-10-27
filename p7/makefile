.SILENT:
run:
	gcc -o sdl_text_example sdl_text_example.c `sdl2-config --cflags --libs` -lSDL2_ttf
case1:
	cd SDL
	mkdir build
	cd build
	cmake .. -DCMAKE_BUILD_TYPE=Release
	cmake --build . --config Release

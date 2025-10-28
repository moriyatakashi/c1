.SILENT:
MAKEFLAGS+=--no-print-directory
start:
	export LIBVA_DRIVER_NAME=i965 && npm start
init:
	npm install
	$(MAKE) start
clean:
	rm -rf node_modules
http:
	python3 -m http.server

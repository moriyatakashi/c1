.SILENT:
makeflags+=--no-directory-print
run:
	export LIBVA_DRIVER_NAME=i965 && npm start
init:
	npm install
	$(MAKE) run
clean:
	rm -rf node_modules

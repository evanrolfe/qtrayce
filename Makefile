.PHONY: build test

generate:
	pyside6-uic src/ui_main_window.ui -o src/ui_main_window.py
	pyside6-uic src/network/ui/ui_network_page.ui -o src/network/ui/ui_network_page.py
	pyside6-uic src/network/ui/ui_flow_table_container.ui -o src/network/ui/ui_flow_table_container.py
	pyside6-uic src/network/ui/ui_containers_dialog.ui -o src/network/ui/ui_containers_dialog.py
	pyside6-uic src/editor/ui_editor_page.ui -o src/editor/ui_editor_page.py

# Incorrect import paths are generated, hence the sed, see https://github.com/protocolbuffers/protobuf/issues/1491
generate-grpc:
	python -m grpc_tools.protoc -I./src/agent --python_out=./src/agent --grpc_python_out=./src/agent --pyi_out=./src/agent ./src/agent/api.proto
	sed -i 's/import api_pb2/from . import api_pb2/' src/agent/api_pb2_grpc.py

install:
	pip install -r requirements.txt

installdev:
	pip install -r dev-requirements.txt

run:
	TRAYCE_ENV=development python src

build:
	rm -rf build
	rm -rf dist
	pyinstaller trayce.spec

# Use a special target to capture any additional arguments
ifneq (,$(filter $(firstword $(MAKECMDGOALS)),test))
  # use the rest as arguments for "test"
  TEST_ARGS := $(wordlist 2, $(words $(MAKECMDGOALS)), $(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(TEST_ARGS):;@:)
endif

test:
	PYTHONPATH="./src:./test" pytest -s ./test $(TEST_ARGS)

# Builds a .dmg file from dist/trayce.app
pkg-dmg:
	rm -f dist/trayce.dmg; \
	create-dmg \
		--volname "Trayce" \
		--volicon "./icon.icns" \
		--window-pos 200 120 \
		--window-size 600 300 \
		--icon-size 100 \
		--icon "./icon.icns" 175 120 \
		--hide-extension "trayce.app" \
		--app-drop-link 425 120 \
		"dist/trayce.dmg" \
		"dist/trayce.app/"

pkg-deb:
	rm -f dist/trayce.deb; \
	cd dist; \
	mv trayce trayce2; \
	mkdir -p trayce/DEBIAN; \
	mkdir -p trayce/usr/local/lib; \
	mkdir -p trayce/usr/share/applications; \
	mv trayce2 trayce/usr/local/lib/trayce; \
	cp ../include/DEBIAN/* ./trayce/DEBIAN/; \
	cp trayce/DEBIAN/trayce.desktop trayce/usr/share/applications/; \
	dpkg-deb --build trayce

pkg-rpm:
	@echo "TODO"

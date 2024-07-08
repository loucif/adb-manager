# Define variables
PYINSTALLER = pyinstaller
SCRIPT = auto_install_apk.py
EXECUTABLE_NAME = device_monitor.exe
DIST_DIR = dist

# Default target
all: clean install build

# Install pyinstaller if not already installed
install:
	@pip install pyinstaller

# Build the executable
build:
	@$(PYINSTALLER) --onefile $(SCRIPT)

# Clean up the build and dist directories and any other PyInstaller files
clean:
	@if [ -d "build" ]; then rmdir /S /Q build; fi
	@if [ -d "$(DIST_DIR)" ]; then rmdir /S /Q $(DIST_DIR); fi
	@if [ -f "$(EXECUTABLE_NAME).spec" ]; then del $(EXECUTABLE_NAME).spec; fi

# Run the executable
run:
	@$(DIST_DIR)\$(EXECUTABLE_NAME) /path/to/adb /path/to/app.apk --interval 10

.PHONY: all install build clean run

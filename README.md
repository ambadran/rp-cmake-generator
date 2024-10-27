# CMake files Generator for 'pico-sdk' projects

Python program to automate the generation of the necessary CMake files to ease the compilation, automatically update CMakeLists.txt file and upload of any rp2040, rp2350 board.

By updating CMakeLists.txt file, I mean it will automatically see all the *.c files in your directory and remove them if removed from folder.

**IMP**: This script basically does the exact steps mentioned in the "getting-started-with-pico.pdf" under section "Manually Create your own Project" on page-37.

**IMP**: the `PICO_SDK_PATH` environment variable MUST BE DEFINED to be the path to the 'pico-sdk' folder.

## What is does:
  - create empty 'main.c'
  - creates the CMakeLists.txt file with `PROJECT_NAME` being the name of the folder it is in
  - copies the 'pico_sdk_import.cmake' into project folder from the `PICO_SDK_PATH` folder
  - create 'build/' folder
  - runs `cmake ..` in the 'build/' folder
  - using the `update` parameter, it will update the CMakeLists.txt file with the current executables


## Installation:

Assuming you've set the `PICO_SDK_PATH` environment path variable, You can create an alias `rpproject` in your .zshrc/.bashrc file to the cli.py file.

    alias rpproject="python3 ~/.../rp-makefile-generator/cli.py"

Then source the file ofcoarse.

    source ~/.bashrc

or 

    source ~/.zshrc

## Usage: 

To prepare the project directory:

    rpproject new <board_name>

`board_name` are the any of the board names named in the 'pico-sdk/src/boards/include/boards' folder

To Updates the CMakeLists.mk Makefile with the current source files:

    rpproject update 

#TODOs:
  - finish `update` command
  - give option to auto-connect pico w with wifi using the `-DWIFI_SSID="Your Network"
-DWIFI_PASSWORD="Your Password"` options in CMake
  - implement `make upload` instead of `picotool load -f <executable>.uf2`
  - implement `make console` instead of `picocom -b 115200 /dev/ttyACM0`



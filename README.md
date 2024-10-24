# Makefile Generator for ANY 'uni-stc' based STC MCU Project

Python program to automate the generation of the necessary CMake files to ease the compilation, AUTOMATICALLY UPDATING CMakeLists.txt file and upload of any rp2040, rp2350 board.

By updating CMakeLists.txt file, I mean it will automatically see all the *.c files in your directory AND all the `#includes` from the 'pico-sdk' folder and automagically put the necessary files in the CMakeLists.txt folder.
For example, if you have 'gpio.c' and 'main.c' in your folder and you've included 

IMP: This script basically does the exact steps mentioned in the "getting-started-with-pico.pdf" under section "Manually Create your own Project" on page-37.

IMP: the `PICO_SDK_PATH` environment variable MUST BE DEFINED to be the path to the 'pico-sdk' folder.

## What is does:
  - create empty 'main.c'
  - creates the CMakeLists.txt file with `PROJECT_NAME` being the name of the folder it is in
  - copies the 'pico_sdk_import.cmake' into project folder from the `PICO_SDK_PATH` folder
  - create 'build/' folder
  - runs `cmake ..` in the 'build/' folder


## Installation:

Assuming you've set the `PICO_SDK_PATH` environment path variable, You can create an alias `rpproject` in your .zshrc/.bashrc file to the cli.py file.

    alias rpproject="python3 ~/.../rp-makefile-generator/cli.py"

Then source the file ofcoarse.

    source ~/.bashrc

or 

    source ~/.zshrc

## Usage: 

To creates the Makefile and the Makefiles directory with all the necessary Makfiles

    rpproject new <board_name>

`board_name` are the same board names named in the 'pico-sdk' folder

To Updates the CMakeLists.mk Makefile with the current project needed source files

    rpproject update 

"""
Main Script
"""
import os
import shutil
from pathlib import Path
from main_c_template import generate_main_c
from cmakelist_txt_template import generate_cmakelists_txt
from defaults import *
from typing import Optional

def main(build_for, project_name: str=default_project_name, executable_name: str=default_executable_name):
    f'''
    :param build_for: Board to build for, This includes:\n\t{available_boards}
    '''
    # Step 1: create main.c and including the pico-sdk for proper project build
    with open("main.c", "w") as file:
        file.write(generate_main_c())

    # Step 1: create the CMakeLists.txt file
    with open("CMakeLists.txt", "w") as file:
        file.write(generate_cmakelists_txt(project_name, executable_name))

    print("Created 'CMakeLists.txt' file!")

    # Step 2: copy the 'pico_sdk_import.cmake' file into project directory
    PICO_SDK_PATH = os.environ.get("PICO_SDK_PATH")
    pico_sdk_import_cmake = os.path.join(PICO_SDK_PATH, "external/pico_sdk_import.cmake")
    shutil.copy(pico_sdk_import_cmake, '.')

    print("Copied the 'pico_sdk_import.cmake' file from the 'pico-sdk' folder!")

    # Step 3: Create the 'build' directory and change directory into it
    directory_name = Path("build")
    directory_name.mkdir()
    os.chdir('build')

    print("Created the 'build' directory and CDed into it!")

    # Step 4: Run cmake for the specific board
    if build_for not in available_boards:
        raise ValueError("Passed board name to build for is invalid!\nAvailable Boards:\n{available_boards}")

    os.system(f"cmake -DPICO_BOARD={build_for} ..")


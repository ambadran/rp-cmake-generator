"""
Creating the CMakeLists.txt file
"""
from defaults import default_project_name, default_executable_name

def generate_cmakelists_txt(project_name: str=default_project_name, executable_name: str=default_executable_name):
    '''
    generates the CMakeLists.txt file
    '''
    string = f"""cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project({project_name} C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
pico_sdk_init()

add_executable({executable_name}
  main.c
)

pico_enable_stdio_usb({executable_name} 1)
pico_enable_stdio_uart({executable_name} 1)

pico_add_extra_outputs({executable_name})

target_link_libraries({executable_name} pico_stdlib)

if (PICO_CYW43_SUPPORTED)
    target_link_libraries({executable_name} pico_cyw43_arch_none)
endif()

    """
    return string


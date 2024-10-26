"""
Creating the main.c with included pico-sdk for proper build
"""

def generate_main_c():
    '''
    generates main.c with includes
    '''
    string = """#include "pico/stdlib.h"
#include "pico/binary_info.h"


int main() {

    return 0;
}
    """
    return string

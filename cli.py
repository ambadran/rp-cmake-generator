"""
CLI Interface for this Program


Usage:

To prepare the project directory:

        rpproject new <board_name>

To Updates the CMakeLists.mk Makefile with the current source files:

        rpproject update 
"""
import os
import argparse
from main import main
from update_cmakelists_txt import update_executables

def cli():
    '''
    implementing the cli functionality
    '''
    pass

if __name__ == "__main__":
    cli()

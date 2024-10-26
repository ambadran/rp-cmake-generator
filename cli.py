"""
CLI Interface for this Program.


Usage:

To prepare the project directory:

        rpproject new <board_name>

To Updates the CMakeLists.mk Makefile with the current source files:

        rpproject update 
"""
import os
import argparse
from defaults import available_boards
from main import main
from update_cmakelists_txt import update_executables

def cli():
    '''
    implementing the cli functionality
    '''
    # Create the parser
    parser = argparse.ArgumentParser(description=__doc__)  # file desc

    # Add arguments
    supported_commands = ['new', 'update']

    parser.add_argument('command', type=str, choices=supported_commands, help='`new` to generate Project files, `update` to update the executables in CMakeLists.txt')
    parser.add_argument('-b', '--board_name', type=str, default='pico', help="board name as in 'pico-sdk/src/boards/include/boards'. e.g- pico_w, waveshare_rp2040_zero")

    # Parse the arguments
    args = parser.parse_args()

    if args.command == 'new':

        if args.board_name not in available_boards:
            raise ValueError(f"board_name must be one of {available_boards}")

        ### Creating Project
        main(args.board_name)

    elif args.command == 'update':

        ###  Updating the executables
        update_cmakelists_txt

if __name__ == "__main__":
    cli()

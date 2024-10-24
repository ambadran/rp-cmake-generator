"""
This file is to manage the default values of all the variables
"""
import os
import sys

# Project Name
default_project_name = os.path.basename(os.getcwd())
default_executable_name = "executable"

# Default PORT name
if sys.platform == 'win32':
    raise NotImplementedError("Need to implement code to find the proper COM port")

elif sys.platform == 'darwin':
    default_console_port = '/dev/tty.usbserial' #TODO: complete this from mac
    default_isp_port = '/dev/tty.usbserial' #TODO: complete this from mac

elif sys.platform == 'linux':
    default_console_port = '/dev/ttyACM0'
    default_isp_port = '/dev/ttyACM0'

else:
    raise NotImplementedError("unknown operating system")

# console_baudrate
default_console_baudrate = 115200


"""
Main Script
"""
import os
import shutil
from pathlib import Path
from cmakelist_txt_template import generate_cmakelists_txt
from defualts import *
from typing import Optional

def main(build_for: Optional[str]=None, project_name: str=default_project_name, executable_name: str=default_executable_name):
    '''
    :param build_for: Board to build for, This includes:
        xcb_helios
        adafruit_feather_rp2040
        adafruit_feather_rp2040_usb_host
        adafruit_itsybitsy_rp2040
        adafruit_kb2040
        adafruit_macropad_rp2040
        adafruit_qtpy_rp2040
        adafruit_trinkey_qt2040
        amethyst_fpga
        archi
        arduino_nano_rp2040_connect
        cytron_maker_pi_rp2040
        datanoisetv_rp2040_dsp
        defcon32_badge
        eetree_gamekit_rp2040
        garatronic_pybstick26_rp2040
        gen4_rp2350_24ct
        gen4_rp2350_24
        gen4_rp2350_24t
        gen4_rp2350_28ct
        gen4_rp2350_28
        gen4_rp2350_28t
        gen4_rp2350_32ct
        gen4_rp2350_32
        gen4_rp2350_32t
        gen4_rp2350_35ct
        gen4_rp2350_35
        gen4_rp2350_35t
        hellbender_2350A_devboard
        ilabs_challenger_rp2350_bconnect
        ilabs_challenger_rp2350_wifi_ble
        ilabs_opendec02
        melopero_perpetuo_rp2350_lora
        melopero_shake_rp2040
        metrotech_xerxes_rp2040
        net8086_usb_interposer
        none
        nullbits_bit_c_pro
        phyx_rick_tny_rp2350
        pico2
        pico
        pico_w
        pimoroni_badger2040
        pimoroni_interstate75
        pimoroni_keybow2040
        pimoroni_motor2040
        pimoroni_pga2040
        pimoroni_pga2350
        pimoroni_picolipo_16mb
        pimoroni_picolipo_4mb
        pimoroni_pico_plus2_rp2350
        pimoroni_picosystem
        pimoroni_plasma2040
        pimoroni_plasma2350
        pimoroni_servo2040
        pimoroni_tiny2040_2mb
        pimoroni_tiny2040
        pimoroni_tiny2350
        pi-plates_micropi
        pololu_3pi_2040_robot
        pololu_zumo_2040_robot
        seeed_xiao_rp2040
        seeed_xiao_rp2350
        solderparty_rp2040_stamp_carrier
        solderparty_rp2040_stamp
        solderparty_rp2040_stamp_round_carrier
        solderparty_rp2350_stamp
        solderparty_rp2350_stamp_xl
        sparkfun_micromod
        sparkfun_promicro
        sparkfun_promicro_rp2350
        sparkfun_thingplus
        switchscience_picossci2_conta_base
        switchscience_picossci2_dev_board
        switchscience_picossci2_micro
        switchscience_picossci2_rp2350_breakout
        switchscience_picossci2_tiny
        tinycircuits_thumby_color_rp2350
        vgaboard
        waveshare_rp2040_lcd_0.96
        waveshare_rp2040_lcd_1.28
        waveshare_rp2040_one
        waveshare_rp2040_plus_16mb
        waveshare_rp2040_plus_4mb
        waveshare_rp2040_zero
        weact_studio_rp2040_16mb
        weact_studio_rp2040_2mb
        weact_studio_rp2040_4mb
        weact_studio_rp2040_8mb
        wiznet_w5100s_evb_pico
    '''
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
    if build_for is not None:
        if build_for not in possible_boards:
            raise ValueError("Passed board name to build for is invalid!\nAvailable Boards:\n{possible_boards}")

        os.system(f"cmake -DPICO_BOARD={build_for} ..")

    else:
        os.system(f"cmake ..")



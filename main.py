# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from subprocess import CalledProcessError
import xbmcaddon
import xbmcgui

def adb_connect_to_device(addr):
    try:
        result = subprocess.check_output("~/.kodi/addons/script.scrcpy-launcher/bin/connect_device.sh "+addr, shell=True)

        if not "connected" in result:
            xbmcgui.Dialog().ok("Error connecting to device", result)
            return False
        else:
            return True

    except CalledProcessError as procError:
        msg = procError.output
        xbmcgui.Dialog().ok("Error connecting to device", msg)
        return False

addr = xbmcgui.Dialog().input('Enter IP address', type=xbmcgui.INPUT_IPADDRESS)
if addr:
    if adb_connect_to_device(addr):
        while True:
            # check if USB debugging was authorized
            launchCommand = "LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/.kodi/addons/script.scrcpy-launcher/bin/lib ~/.kodi/addons/script.scrcpy-launcher/bin/adb devices"
            result = subprocess.check_output(launchCommand, shell=True)
            if "unauthorized" in result:
                xbmcgui.Dialog().ok("Unauthorized", "Please allow USB debugging connection in Android device")
            else:
                break
        launchCommand = "systemd-run bash ~/.kodi/addons/script.scrcpy-launcher/bin/launch_scrcpy.sh"
        os.system(launchCommand)
    sys.exit()
else:
    sys.exit()

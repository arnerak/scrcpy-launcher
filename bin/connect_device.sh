#!/bin/bash

# Get IP address
if [ -z "$1" ]; then
    echo "Error, please specify IP address...exiting"
    exit 1
else
    addr="$1"
fi

LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/.kodi/addons/script.scrcpy-launcher/bin/lib ~/.kodi/addons/script.scrcpy-launcher/bin/adb connect "$addr"

#!/bin/bash
. /etc/profile

systemctl stop kodi # Must close kodi for proper video display

SDL_VIDEO_EGL_DRIVER=libEGL.so SDL_VIDEO_GL_DRIVER=libGLESv2.so LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/.kodi/addons/script.scrcpy-launcher/bin/lib PATH=$PATH:~/.kodi/addons/script.scrcpy-launcher/bin SCRCPY_SERVER_PATH=~/.kodi/addons/script.scrcpy-launcher/bin/scrcpy-server ~/.kodi/addons/script.scrcpy-launcher/bin/scrcpy -c 1432:1420:200:250 -m 720

systemctl start kodi # Reopen kodi


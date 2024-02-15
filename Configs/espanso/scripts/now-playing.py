#!/usr/bin/env python3

import dbus
import sys

def main():
    bus = dbus.SessionBus()
    proxy = bus.get_object('org.mpris.MediaPlayer2.spotify','/org/mpris/MediaPlayer2')

    properties_manager = dbus.Interface(proxy, 'org.freedesktop.DBus.Properties')

    if properties_manager:

        if len(sys.argv) > 1:
            if sys.argv[1] == "1":
                dbus.Interface(proxy, 'org.mpris.MediaPlayer2.Player').PlayPause()

        status = properties_manager.Get('org.mpris.MediaPlayer2.Player', 'PlaybackStatus')
        if status == "Playing" : status = " "
        else : status = " "

        current = properties_manager.Get('org.mpris.MediaPlayer2.Player', 'Position')

        data = properties_manager.Get('org.mpris.MediaPlayer2.Player', 'Metadata')
        length = data["mpris:length"]
        title = data["xesam:title"]
        uri = data["xesam:url"]
        artists = data["xesam:artist"]
        artist = ""
        for i in artists:
            artist += i + ""

        perc = current / length
        bar = f"[{title}]({uri})"
        print(bar)

if __name__ == "__main__":
    try:
        main()
    except dbus.DBusException as e:
        # return nothing if spotify is not running so espanso doesn't do anything
        print("")  


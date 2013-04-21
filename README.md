twenty-five-shades-of-random
============================

An exploration of some algorithmic composition 
using python, rtmidi, yoshimi and linuxsampler over
jack-midi.

This was made on a Linux Debian SID 64bit system.

At the very least you will need python 2, 
jack, rtmidi, yoshimi and linuxsampler 

NOTE: I've compiled the most recent linuxsampler version from svn.
I'm not sure if the stock version is recent enough.

how to run it
=============
on the command line, first type

  ./killsynths.sh

then

  ./startsynths.sh

then

  python main.py


troubleshooting
===============

You may need to manually connect the output of LinuxSampler
to your system:output in qjackctrl to hear the output of 
LinuxSampler.

License: GPLv3


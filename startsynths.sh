#!/bin/sh 
killall jackd
yoshimi -k -K -S./synthconfig/instruments.state &
python genconfig_linuxsampler.py
qsampler ./synthconfig/linuxsampler.lscp &
qjackctl &
jack_connect LinuxSampler:0 system:playback_1
jack_connect LinuxSampler:1 system:playback_2




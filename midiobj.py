# Twenty-five-shades-of-random: an exploration of algorithmic composition
# Copyright (C) 2013 stefaan.himpe@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import rtmidi

class MidiObj(object):
  """
  class to manage midi connections and to send note on/note off messages on a given midi channel
  """
  def __init__(self, jack_port_names):
    self.midiout = []
    for jack_port_name in jack_port_names:
      mo = rtmidi.MidiOut(rtmidi.API_UNIX_JACK)
      available_ports = mo.get_ports()
      idx = available_ports.index(jack_port_name)
      mo.open_port(idx)
      print u"Connect to port {0}".format(jack_port_name)
      self.midiout.append((mo, jack_port_name))
  
  def disconnect(self, idx, jack_port_name):
    for mo in self.midiout:
      print u"Disconnect from port {0}".format(mo[1])
      mo[0].close_port(idx)

  def note_on_msg(self, note, channel, velocity):
    return [ 144 + channel - 1, note, velocity ]

  def note_off_msg(self, note, channel):
    return [144 + channel - 1 - 0x10, note, 0 ]

  def send_message(self, msg):
    for mo in self.midiout:
      mo[0].send_message(msg)


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


import threading
import time
import Queue
import random
from midiutils import a_name

class CircleWalk(threading.Thread):
  """
  class to play a fragment forward, then backward, then forward again, ... until stop time
  """
  def __init__(self, instrname, notes, durations, velocities, octaves, stretto, midiobject, channel):
    self.instrname = instrname
    self.midi = midiobject
    self.q = Queue.Queue() 
    self.notes = notes #[ 60, 64, 67, 69, 72]
    self.durations = durations #[ 1, 2, 4, 8]
    self.velocities = velocities #[ (i+1)*10 for i in range(11) ]
    self.octaves = octaves #[-1, 0, 1, 2]
    self.stretto = stretto #[1]
    self.interrupt = False
    self.channel = channel
    self.current_note = 0
    self.direction = 1
    threading.Thread.__init__(self)

  def next_note(self, notes):
    """
    determine next note to play
    """
    note = notes[self.current_note]
    self.current_note += self.direction 
    if self.current_note >= len(notes):
      self.direction = -1
      self.current_note = len(notes)-1
    if self.current_note < 0:
      self.direction = 1
      self.current_note = 0
    return note

  def run(self):
    """
    walk in circles
    """
    m = self.midi
    c = random.choice
    s = time.sleep
    q = self.q
    while not self.interrupt:
      note = self.next_note(self.notes)+12*c(self.octaves)
      vel = c(self.velocities)
      on = m.note_on_msg(note, self.channel, vel)
      off = m.note_off_msg(note, self.channel)
      print "CIRCLEWALK {0}: NOTE ON note: {1} channel: {2} velocity: {3}".format(self.instrname, a_name(note), self.channel, vel)
      m.send_message(on)
      q.put(off)
      s(c(self.durations)*c(self.stretto))

      size = random.randint(0, q.qsize())
      for i in xrange(size):
        if not q.empty():
          off = q.get()
          print "CIRCLEWALK {0}: NOTE OFF note: {1} channel: {2}".format(self.instrname, a_name(off[1]), self.channel)
          m.send_message(off)

    self.cleanup()

  def cleanup(self):
    while not self.q.empty():
      off = self.q.get()
      print "CIRCLEWALK {0}: NOTE OFF note: {1} channel: {2}".format(self.instrname, a_name(off[1]), self.channel)
      self.midi.send_message(off)



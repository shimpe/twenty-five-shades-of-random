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

class Clustrificator(threading.Thread):
  """
  class to replace single note with a cluster of notes
  """
  def __init__(self, instrname, intervals, notes_lengths, velocities, octaves, strettos, midiobject, channel):
    self.instrname = instrname
    self.midi = midiobject
    self.q = Queue.Queue() 
    self.notes_lengths = notes_lengths # [ (60, 0.5), (64, 0.5), (67, 1)] 
    self.intervals = intervals
    self.velocities = velocities #[ (i+1)*10 for i in range(11) ]
    self.interrupt = False
    self.channel = channel
    self.current_note = 0
    self.strettos = strettos
    self.octaves = octaves
    self.notes = self.clustrificate(self.notes_lengths)
    threading.Thread.__init__(self)

  def clustrificate(self, notes_lengths):
    """
    give allowed intervals for cluster building, select some at random and apply them
    """
    notes = []
    for note, dur in notes_lengths:
      intervals = self.intervals[:]
      #random.shuffle(intervals)
      allowed_intervals = intervals[0:random.randint(0,len(intervals))]
      if allowed_intervals:
        new_dur = float(dur)/(len(intervals))
        for i in allowed_intervals:
          notes.append( (note+i, new_dur) )
      else:
        notes.append( (note, dur) )
    return notes

  def next_note(self, notes):
    note = notes[self.current_note]
    self.current_note += 1
    if self.current_note >= len(notes):
      self.current_note = 0
    return note

  def run(self):
    m = self.midi
    c = random.choice
    s = time.sleep
    q = self.q
    while not self.interrupt:
      note_dur = self.next_note(self.notes)
      note = note_dur[0]+ 12*c(self.octaves)
      dur = note_dur[1]*c(self.strettos)
      vel = c(self.velocities)
      on = m.note_on_msg(note, self.channel, vel)
      off = m.note_off_msg(note, self.channel)
      print "CLUSTRIFICATOR {0}: NOTE ON note: {1} channel: {2} velocity: {3}".format(self.instrname, a_name(note), self.channel, vel)
      m.send_message(on)
      q.put(off)
      s(dur)

      size = random.randint(0, q.qsize())
      for i in xrange(size):
        if not q.empty():
          off = q.get()
          print "CLUSTRIFICATOR {0}: NOTE OFF note: {1} channel: {2}".format(self.instrname, a_name(off[1]), self.channel)
          m.send_message(off)

    self.cleanup()

  def cleanup(self):
    while not self.q.empty():
      off = self.q.get()
      print "CLUSTRIFICATOR {0}: NOTE OFF note: {1} channel: {2}".format(self.instrname, a_name(off[1]), self.channel)
      self.midi.send_message(off)



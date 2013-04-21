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

class NoteInterpolator(threading.Thread):
  """
  class that takes a melody and adds all missing notes in between each consecutive note

  missing notes are notes which exist in the scale between the two consecutive melody notes

  rythm is calculated so that overall timing is not affected

  can also apply a selection of velocities, of octaves, apply a time delays factor (strettos)
  """
  def __init__(self, instrname, scale, notes_lengths, velocities, octaves, strettos, midiobject, channel):
    self.instrname = instrname
    self.midi = midiobject
    self.q = Queue.Queue() 
    self.notes_lengths = notes_lengths # [ (60, 0.5), (64, 0.5), (67, 1)] 
    self.scale = scale
    self.velocities = velocities #[ (i+1)*10 for i in range(11) ]
    self.interrupt = False
    self.channel = channel
    self.current_note = 0
    self.strettos = strettos
    self.octaves = octaves
    self.notes = self.interpolate(self.notes_lengths)
    threading.Thread.__init__(self)

  def interpolate(self, notes_lengths):
    """
    given a melody and a scale, find out 
    which notes to add 
    """
    notes = []
    for i in range(len(notes_lengths)-1):
      current_note = notes_lengths[i][0]
      current_length = notes_lengths[i][1]
      next_note = notes_lengths[i+1][0]
      if current_note in self.scale and next_note in self.scale:
        current_note_idx = self.scale.index(current_note)
        next_note_idx = self.scale.index(next_note)
        if current_note_idx < next_note_idx:
          no_of_notes = next_note_idx - current_note_idx 
          for n in range(no_of_notes):
            notes.append( (self.scale[current_note_idx+n], float(current_length)/no_of_notes ) )
        elif current_note_idx > next_note_idx:
          no_of_notes = current_note_idx - next_note_idx 
          for n in range(no_of_notes):
            notes.append( (self.scale[current_note_idx-n], float(current_length)/no_of_notes) )
        elif current_note_idx == next_note_idx:
          notes.append( (current_note, current_length) )
      else:
        notes.append( (current_note, current_length) )
    notes.append(notes_lengths[-1])
    return notes

  def next_note(self, notes):
    """
    find out the next note to be played
    """
    note = notes[self.current_note]
    self.current_note += 1
    if self.current_note >= len(notes):
      self.current_note = 0
    return note

  def run(self):
    """
    generate notes
    """
    m = self.midi
    c = random.choice
    s = time.sleep
    q = self.q # a queue to remember which notes have been started; needed to switch them off at some random time later on
    while not self.interrupt:
      note_dur = self.next_note(self.notes)
      note = note_dur[0]+ 12*c(self.octaves)
      dur = note_dur[1]*c(self.strettos)
      vel = c(self.velocities)
      on = m.note_on_msg(note, self.channel, vel)
      off = m.note_off_msg(note, self.channel)
      print "NOTEINTERPOLATOR {0}: NOTE ON note: {1} channel: {2} velocity: {3}".format(self.instrname, a_name(note), self.channel, vel)
      m.send_message(on)
      q.put(off)
      s(dur)

      size = random.randint(0, q.qsize())
      for i in xrange(size):
        if not q.empty():
          off = q.get()
          print "NOTEINTERPOLATOR {0}: NOTE OFF note: {1} channel: {2}".format(self.instrname, a_name(off[1]), self.channel)
          m.send_message(off)

    self.cleanup()

  def cleanup(self):
    """
    send note off msgs to all notes that were still running
    """
    while not self.q.empty():
      off = self.q.get()
      print "NOTEINTERPOLATOR {0}: NOTE OFF note: {1} channel: {2}".format(self.instrname, a_name(off[1]), self.channel)
      self.midi.send_message(off)

if __name__ == "__main__":
  from midiutils import a_note
  n = NoteInterpolator("Clocks27",
        [a_note("G4"), a_note("C5"), a_note("D5"), a_note("E5"), a_note("F5"), a_note("G5")],                            # notes used during interpolation
        [ (a_note("G4"), 1), 
          (a_note("C5"), 1), (a_note("C5"), 0.5), (a_note("D5"), 0.5),
          (a_note("E5"), 1), (a_note("C5"), 1),
          (a_note("G5"), 1.5), (a_note("F5"), 0.5),
          (a_note("E5"), 2) ],     # note_durations
        [ 30, 64, 90 ],            # vel
        [ 1 ],         # strettos
        None,                         # midi obj
        6)
  print n.notes

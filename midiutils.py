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

# some helper functions

name_to_note = {}
note_to_name = {}
noteidx = 0
for octave in range(11):
  for notename in ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']:
    name = '{0}{1}'.format(notename,octave) 
    name_to_note[ name ] = noteidx
    note_to_name[ noteidx ] = name
    noteidx += 1
noteidx = 0
for octave in range(11):
  for notename in ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']:
    name = '{0}{1}'.format(notename,octave) 
    name_to_note[ name ] = noteidx
    note_to_name[ noteidx ] = name
    noteidx += 1

def a_note(name):
  """
  transform a note name like "Cb4" into a midi number
  """
  return name_to_note[name]

def a_name(note):
  """
  transform a midi note like 60 into a note name
  """
  return note_to_name[note]

def a_scale(notenames, octaves):
  """
  combine a list of note names and octaves into a scale
  """
  notes = []
  for o in octaves:
    for n in notenames:
      notes.append(a_note("%s%s" % (n,o)))
  return notes


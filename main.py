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

import midiobj
import padgen
import notewalk
import circlewalk
import noteinterpolator
import clustrificator
import scheduler
import random

from midiutils import a_note, a_scale

if __name__ == "__main__":
  m = midiobj.MidiObj([u"yoshimi:midi in", u"LinuxSampler:midi_in_0"])
  s = scheduler.Scheduler(0.01)


  raw_input ("Please make synthesizer connections. Press enter to continue...")
  
  # define schedule
  # fragment 1: pads
  s.add_fragment(padgen.PadGen("Pad1", 
                               [a_note("C4")], # a_note("D4"), a_note("E4"), a_note("G4"), a_note("A4") ], # notes
                               [1, 0.333],                       # durations
                               [ (i+1)*10 for i in range(11) ],  # velocities
                               [0, 1, 2],                        # octaves
                               [1, 2, 4, 8],                     # strettos
                               m,                                # midiobject
                               1),                               # midi channel 1
                               0, 30)                            # time 0 to 30

  # fragment 2: bells
  s.add_fragment(padgen.PadGen("Bells2",
                               [a_note("C4"), a_note("Db4"), a_note("Eb4"), a_note("E4")], # notes
                               [0.333],                          # durations
                               [ (i+1)*10 for i in range(11) ],  # velocities
                               [-2, -1, 0, 1],                   # octaves
                               [1, 0.5, 0.25, 0.125],            # strettos
                               m,
                               2),
                               15, 45)                           # time 15 to 45
                              

  # fragment 2b: bells
  s.add_fragment(padgen.PadGen("Bells2b",
                               [a_note("C4"), a_note("G4"), a_note("Bb4"), a_note("C5")], # notes
                               [0.5],                          # durations
                               [ (i+1)*10 for i in range(11) ],  # velocities
                               [-2, -1, 0, 1],                   # octaves
                               [1, 0.5, 0.25, 0.125],            # strettos
                               m,
                               2),
                               15, 45)                           # time 15 to 45
 
  # fragment 3: pads
  s.add_fragment(padgen.PadGen("Pad3", 
                               [a_note("C4"), a_note("D4"), a_note("E4"), a_note("G4"), a_note("A4") ], # notes
                               [1, 0.333],                       # durations
                               [ (i+1)*10 for i in range(11) ],  # velocities
                               [0, 1, 2],                        # octaves
                               [1, 2, 4, 8],                     # strettos
                               m,                                # midiobject
                               1),                               # midi channel 1
                               30, 60)                           # time 0 to 30


  s.add_fragment(padgen.PadGen("Pad3b", 
                               [a_note("C#4"), a_note("D#4"), a_note("F4"), a_note("G#4"), a_note("A#4") ], # notes
                               [1, 0.333],                       # durations
                               [ (i+1)*10 for i in range(11) ],  # velocities
                               [0, 1, 2],                        # octaves
                               [1, 2, 4, 8],                     # strettos
                               m,                                # midiobject
                               1),                               # midi channel 1
                               30, 60)                           # time 0 to 30

  # fragment 4: noises
  s.add_fragment(padgen.PadGen("ChipStrang4",
                               [a_note("Eb4"), a_note("E4"), a_note("F4")],
                               [0.2],
                               [ 20, 40, 60 ],
                               [ 0 ],
                               [ 1 ],
                               m,
                               3),
                               60, 90)

  # fragment 5: bells
  s.add_fragment(padgen.PadGen("Bells5",
                               [a_note("C4"), a_note("D4"), a_note("F4"), a_note("G4"), a_note("A4"), a_note("C5")], # notes
                               [0.5],                          # durations
                               [ (i+1)*10 for i in range(11) ],  # velocities
                               [-2, -1, 0, 1],                   # octaves
                               [1, 0.5, 0.25, 0.125],            # strettos
                               m,
                               2),
                               80, 160) 

  # fragment 6: pads
  s.add_fragment(padgen.PadGen("Pad6", 
                               [a_note("C4"), a_note("Eb4"), a_note("F#4"), a_note("G4"), a_note("Bb4") ], # notes
                               [1, 0.333],                       # durations
                               [ (i+1)*10 for i in range(11) ],  # velocities
                               [0, 1, 2],                        # octaves
                               [0.25, 0.5, 1, 2, 4, 8],          # strettos
                               m,                                # midiobject
                               1),                               # midi channel 1
                               150, 230)                         # time 0 to 30

  # fragment 7: bells
  s.add_fragment(padgen.PadGen("Bells7",
                               [a_note("A3"), a_note("C#4"), a_note("E4") ], # notes
                               [0.333],
                               [ (i+1) for i in range(127) ],
                               [0],
                               [0.1],
                               m,
                               2),
                               180, 230)

  # fragment 8: notewalk
  s.add_fragment(notewalk.NoteWalk("notewalk8",
                               [a_note("C5"), a_note("B4"), a_note("A4"), a_note("B4"), a_note("A4"), a_note("G4"), 
                                a_note("A4"), a_note("G4"), a_note("F4"), a_note("G4"), a_note("F4"), a_note("E4")],

                               [0.333],
                               [ 36, 40, 44, 48, 52 ],
                               [0],
                               [1],
                               m,
                               4),
                               180, 230)

  s.add_fragment(notewalk.NoteWalk("notewalk9",
                               [a_note("E4"), a_note("C5"), a_note("E5"), a_note("E4"), a_note("C5"), a_note("E5"), 
                                a_note("E4"), a_note("C5"), a_note("E5"), a_note("D5"), a_note("C5"), a_note("B4")],

                               [0.333],
                               [ 46, 40, 44, 48, 52 ],
                               [0],
                               [0.99],
                               m,
                               4),
                               205, 230)


  # framgent 9: circlewalk
  s.add_fragment(circlewalk.CircleWalk("circlewalk9",
                                       [a_note("C#2"), a_note("D#2"), a_note("F#2"), a_note("G#2"), a_note("A#2"), 
                                        a_note("C#3"), a_note("D#3"), a_note("F#3"), a_note("G#3"), a_note("A#3"), 
                                        a_note("C#4"), a_note("D#4"), a_note("F#4"), a_note("G#4"), a_note("A#4"), 
                                        a_note("C#5"), a_note("D#5"), a_note("F#5"), a_note("G#5"), a_note("A#5"), 
                                        a_note("C#6"), a_note("D#6"), a_note("F#6"), a_note("G#6"), a_note("A#6"), 
                                        a_note("G6"), a_note("F6"), a_note("E6"), a_note("D6"), a_note("C6"),
                                        a_note("B5"), a_note("A5"), a_note("G5"), a_note("F5"), a_note("E5"), a_note("D5"), a_note("C5"),
                                        a_note("B4"), a_note("A4"), a_note("G4"), a_note("F4"), a_note("E4"), a_note("D4"), a_note("C4"),
                                        a_note("B3"), a_note("A3"), a_note("G3"), a_note("F3"), a_note("E3"), a_note("D3"), a_note("C3"),
                                        a_note("B2"), a_note("A2"), a_note("G2"), a_note("F2"), a_note("E2"), a_note("D2"), a_note("C2")],
                                       [0.1],       # durations
                                       [ 10, 100 ], # velocities
                                       [ 0 ],       # octaves
                                       [ 1 ],       # strettos
                                       m,
                                       5),
                                       230,
                                       265)
  #fragment 10: circlewalk
  s.add_fragment(circlewalk.CircleWalk("circlewalk10",
                                       [a_note("C#2"), a_note("D#2"), a_note("F#2"), a_note("G#2"), a_note("A#2"), 
                                        a_note("C#3"), a_note("D#3"), a_note("F#3"), a_note("G#3"), a_note("A#3"), 
                                        a_note("C#4"), a_note("D#4"), a_note("F#4"), a_note("G#4"), a_note("A#4"), 
                                        a_note("C#5"), a_note("D#5"), a_note("F#5"), a_note("G#5"), a_note("A#5"), 
                                        a_note("C#6"), a_note("D#6"), a_note("F#6"), a_note("G#6"), a_note("A#6"), 
                                        a_note("G6"), a_note("F6"), a_note("E6"), a_note("D6"), a_note("C6"),
                                        a_note("B5"), a_note("A5"), a_note("G5"), a_note("F5"), a_note("E5"), a_note("D5"), a_note("C5"),
                                        a_note("B4"), a_note("A4"), a_note("G4"), a_note("F4"), a_note("E4"), a_note("D4"), a_note("C4"),
                                        a_note("B3"), a_note("A3"), a_note("G3"), a_note("F3"), a_note("E3"), a_note("D3"), a_note("C3"),
                                        a_note("B2"), a_note("A2"), a_note("G2"), a_note("F2"), a_note("E2"), a_note("D2"), a_note("C2")],
                                       [0.1],       # durations
                                       [ 10, 30, 70, 100 ], # velocities
                                       [ 0,1 ],       # octaves
                                       [ 1 ],       # strettos
                                       m,
                                       5),
                                       265,
                                       300)

  #fragment 11: circlewalk
  s.add_fragment(circlewalk.CircleWalk("circlewalk11",
                                       [a_note("C#2"), a_note("D#2"), a_note("F#2"), a_note("G#2"), a_note("A#2"), 
                                        a_note("C#3"), a_note("D#3"), a_note("F#3"), a_note("G#3"), a_note("A#3"), 
                                        a_note("C#4"), a_note("D#4"), a_note("F#4"), a_note("G#4"), a_note("A#4"), 
                                        a_note("C#5"), a_note("D#5"), a_note("F#5"), a_note("G#5"), a_note("A#5"), 
                                        a_note("C#6"), a_note("D#6"), a_note("F#6"), a_note("G#6"), a_note("A#6"), 
                                        a_note("G6"), a_note("F6"), a_note("E6"), a_note("D6"), a_note("C6"),
                                        a_note("B5"), a_note("A5"), a_note("G5"), a_note("F5"), a_note("E5"), a_note("D5"), a_note("C5"),
                                        a_note("B4"), a_note("A4"), a_note("G4"), a_note("F4"), a_note("E4"), a_note("D4"), a_note("C4"),
                                        a_note("B3"), a_note("A3"), a_note("G3"), a_note("F3"), a_note("E3"), a_note("D3"), a_note("C3"),
                                        a_note("B2"), a_note("A2"), a_note("G2"), a_note("F2"), a_note("E2"), a_note("D2"), a_note("C2")],
                                       [0.1],       # durations
                                       [ 10, 30, 50, 70, 90, 110 ], # velocities
                                       [ 0,1,2 ],       # octaves
                                       [ 1, 0.5 ],       # strettos
                                       m,
                                       5),
                                       300,
                                       335)


  #fragment 12 circlewalk
  s.add_fragment(circlewalk.CircleWalk("circlewalk12",
                                       [a_note("C#2"), a_note("D#2"), a_note("F#2"), a_note("G#2"), a_note("A#2"), 
                                        a_note("C#3"), a_note("D#3"), a_note("F#3"), a_note("G#3"), a_note("A#3"), 
                                        a_note("C#4"), a_note("D#4"), a_note("F#4"), a_note("G#4"), a_note("A#4"), 
                                        a_note("C#5"), a_note("D#5"), a_note("F#5"), a_note("G#5"), a_note("A#5"), 
                                        a_note("C#6"), a_note("D#6"), a_note("F#6"), a_note("G#6"), a_note("A#6"), 
                                        a_note("G6"), a_note("F6"), a_note("E6"), a_note("D6"), a_note("C6"),
                                        a_note("B5"), a_note("A5"), a_note("G5"), a_note("F5"), a_note("E5"), a_note("D5"), a_note("C5"),
                                        a_note("B4"), a_note("A4"), a_note("G4"), a_note("F4"), a_note("E4"), a_note("D4"), a_note("C4"),
                                        a_note("B3"), a_note("A3"), a_note("G3"), a_note("F3"), a_note("E3"), a_note("D3"), a_note("C3"),
                                        a_note("B2"), a_note("A2"), a_note("G2"), a_note("F2"), a_note("E2"), a_note("D2"), a_note("C2")],
                                       [0.1],       # durations
                                       [ 0, 0, 10, 20], # velocities
                                       [ 0,1,2,3 ],       # octaves
                                       [ 0.5, 0.25 ],       # strettos
                                       m,
                                       5),
                                       335,
                                       400)

  # fragment 13: clock
  s.add_fragment(padgen.PadGen("Clocks13",
                               [a_note("C4"), a_note("E4"), a_note("F#4"), a_note("G4") ], # notes
                               [0.5],                          # durations
                               [ (i+1)*10 for i in range(11) ],# velocities
                               [-3, -2, -1, 0, 1, 2],          # octaves
                               [1, 0.5],                       # strettos
                               m,
                               6),                             # qsampler
                               360, 
                               450)

  # fragment 14: horn duet - voice 1
  s.add_fragment(padgen.PadGen("Horns14", 
                               [a_note("C4"), a_note("E4"), a_note("C4"), a_note("E4"), a_note("C4"), a_note("E4"), a_note("F#4"), a_note("G4"), a_note("G4"), a_note("G4") ], # notes
                               [1, 0.333, 0.5],                  # durations
                               [ (i+1)*10 for i in range(11) ],  # velocities
                               [2],                              # octaves
                               [1, 2, 4, 8],                     # strettos
                               m,                                # midiobject
                               7),                               # midi channel 1
                               400, 480)                         # time 0 to 30

  # fragment 15: horns - voice 2
  s.add_fragment(padgen.PadGen("Horns15", 
                               [a_note("C4"), a_note("E4"), a_note("C4"), a_note("E4"), a_note("C4"), a_note("E4"), a_note("F#4"), a_note("G4"), a_note("G4"), a_note("G4") ], # notes
                               [1, 0.333, 0.5],                  # durations
                               [ (i+1)*10 for i in range(11) ],  # velocities
                               [1],                              # octaves
                               [1, 2, 4, 8],                     # strettos
                               m,                                # midiobject
                               7),                               # midi channel 1
                               400, 480)                         # time 0 to 30


  # fragment 16: horns - voice 3 
  s.add_fragment(padgen.PadGen("Horns16", 
                               [a_note("C4"), a_note("E4"), a_note("C4"), a_note("E4"), a_note("C4"), a_note("E4"), a_note("F#4"), a_note("G4"), a_note("G4"), a_note("G4") ], # notes
                               [1, 0.333, 0.5],                  # durations
                               [ (i+1)*10 for i in range(11) ],  # velocities
                               [0],                              # octaves
                               [1, 2, 4, 8],                     # strettos
                               m,                                # midiobject
                               7),                               # midi channel 1
                               400, 480)                        # time 0 to 30


  # fragment 17: noises
  s.add_fragment(padgen.PadGen("ChipStrang17",
                               [a_note("C4"), a_note("F#4"), a_note("B4")],
                               [0.2],
                               [ 20, 40, 60 ],
                               [ -1 ],
                               [ 4,8 ],
                               m,
                               3),
                               450, 470)
  # fragment 17bis: noises
  s.add_fragment(padgen.PadGen("ChipStrang17bis",
                               [a_note("Eb4"), a_note("Ab4"), a_note("D4")],
                               [0.2],
                               [ 20, 40, 60 ],
                               [ -1 ],
                               [ 4,8 ],
                               m,
                               3),
                               470, 490)


  # fragment 18: violins
  s.add_fragment(padgen.PadGen("Violins18",
                               [a_note("Eb4"), a_note("Bb4")],
                               [ (float(i)/10) for i in xrange(5) ],
                               [ 30,60,90 ],
                               [ 1,2,3 ],
                               [ 4, 8 ],
                               m,
                               8),
                               480,
                               550)
  # fragment 19: cello
  s.add_fragment(padgen.PadGen("Celli19",
                               [a_note("Ab3"), a_note("Bb3"), a_note("Db3")],
                               [ (float(i)/10) for i in xrange(5) ],
                               [ 30,60,90 ],
                               [ 1,2,3 ],
                               [ 4, 8 ],
                               m,
                               9),
                               480,
                               560)

  # fragment 20: contrabass
  s.add_fragment(padgen.PadGen("Bass20",
                               [a_note("Bb1"), a_note("Db1"), a_note("Eb2")],
                               [ (float(i)/10) for i in xrange(5) ],
                               [ 90,120 ],
                               [ 1, 2, 3],
                               [ 4, 8 ],
                               m,
                               10),
                               480,
                               560)
 
  # fragment 21: clocks again
  s.add_fragment(padgen.PadGen("Clocks21",
                               [a_note("C4"), a_note("E4"), a_note("F4"), a_note("G4"), a_note("B4") ], # notes
                               [0,333, 0.5],                          # durations
                               [ (i+1)*10 for i in range(11) ],# velocities
                               [-3, -2, -1, 0, 1, 2],          # octaves
                               [1, 0.5],                       # strettos
                               m,
                               6),                             # qsampler
                               520, 
                               550)

  # fragment 22: pads
  s.add_fragment(padgen.PadGen("Pad22", 
                               [a_note("Eb4")], # notes
                               [1, 0.333],                       # durations
                               [ (i+1)*10 for i in range(11) ],  # velocities
                               [0, 1, 2],                        # octaves
                               [1, 2, 4, 8],                     # strettos
                               m,                                # midiobject
                               1),                               # midi channel 1
                               550, 570)                            # time 0 to 30

  # fragment 23: pads
  s.add_fragment(padgen.PadGen("Pad23", 
                               [a_note("Eb4"), a_note("G4") ],   # notes
                               [1, 0.333],                       # durations
                               [ (i+1)*10 for i in range(7) ],   # velocities
                               [2,3,4],                          # octaves
                               [1, 2, 4, 8],                     # strettos
                               m,                                # midiobject
                               1),                               # midi channel 1
                               570, 590)                            # time 0 to 30

  # fragment 25: pads
  s.add_fragment(padgen.PadGen("Pad25", 
                               [a_note("Eb4"), a_note("G4"), a_note("C4") ],   # notes
                               [1, 0.333],                       # durations
                               [ (i+1)*10 for i in range(7) ],   # velocities
                               [2,3,4],                          # octaves
                               [1, 2, 4, 8],                     # strettos
                               m,                                # midiobject
                               1),                               # midi channel 1
                               590, 610)                            # time 0 to 30

# fragment 26: pads
  s.add_fragment(padgen.PadGen("Pad26", 
                               [a_note("Eb4"), a_note("G4"), a_note("C4") ],   # notes
                               [1, 0.333],                       # durations
                               [ (i+1)*10 for i in range(11) ],  # velocities
                               [2, 3, 4],                        # octaves
                               [1, 2, 4, 8],                     # strettos
                               m,                                # midiobject
                               1),                               # midi channel 1
                               610, 650)                         # time 0 to 30


  # fragment 27: clocks
  s.add_fragment(noteinterpolator.NoteInterpolator("Clocks27",
                               [a_note("G4"), a_note("C5"), a_note("D5"), a_note("E5"), a_note("F5"), a_note("G5")],                            # notes used during interpolation
                               [ (a_note("G4"), 1), 
                                 (a_note("C5"), 1), (a_note("C5"), 0.5), (a_note("D5"), 0.5),
                                 (a_note("E5"), 1), (a_note("C5"), 1),
                                 (a_note("G5"), 1.5), (a_note("F5"), 0.5),
                                 (a_note("E5"), 1.5), (a_note("E5"), 0.5),
                                 (a_note("F5"), 1), (a_note("G5"), 0.5), (a_note("F5"), 0.5), 
                                 (a_note("E5"), 0.5), (a_note("F5"), 0.5), (a_note("G5"), 1),
                                 (a_note("D5"), 0.5), (a_note("C5"), 0.5), (a_note("D5"), 0.5), (a_note("E5"), 0.5),
                                 (a_note("D5"), 1) ],     # note_durations
                               [ 64 ],                    # vel
                               [ 0 ],                     # octaves
                               [ 0.5 ],                   # strettos
                               m,                         # midi obj
                               2),                        # midi channel
                               610, 640)                  # start, stop time

  # fragment 28: bells
  s.add_fragment(clustrificator.Clustrificator("Bells28",                    
                               [-1,0], 
                               [ (a_note("G4"), 1), 
                                 (a_note("C5"), 1), (a_note("C5"), 0.5), (a_note("D5"), 0.5),
                                 (a_note("E5"), 1), (a_note("C5"), 1),
                                 (a_note("G5"), 1.5), (a_note("F5"), 0.5),
                                 (a_note("E5"), 1.5), (a_note("E5"), 0.5),
                                 (a_note("F5"), 1), (a_note("G5"), 0.5), (a_note("F5"), 0.5), 
                                 (a_note("E5"), 0.5), (a_note("F5"), 0.5), (a_note("G5"), 1),
                                 (a_note("D5"), 0.5), (a_note("C5"), 0.5), (a_note("D5"), 0.5), (a_note("E5"), 0.5),
                                 (a_note("D5"), 1) ],     # note_durations
                               [ 64, 90 ],                # vel
                               [1],                       # octaves
                               [ 0.3, 0.5, 0.7 ],         # strettos
                               m,                         # midi obj
                               2),                        # midi channel
                               640, 670)                  # start, stop time


  # fragment 29: clocks
  s.add_fragment(noteinterpolator.NoteInterpolator("Clocks29",
                               a_scale(["C", "C#", "D", "D#", "E", "F", "F#", "G","G#", "A", "A#", "B"], [4,5]),                            # notes used during interpolation
                               [ (a_note("G4"), 1), 
                                 (a_note("C5"), 1), (a_note("C5"), 0.5), (a_note("D5"), 0.5),
                                 (a_note("E5"), 1), (a_note("C5"), 1),
                                 (a_note("G5"), 1.5), (a_note("F5"), 0.5),
                                 (a_note("E5"), 1.5), (a_note("E5"), 0.5),
                                 (a_note("F5"), 1), (a_note("G5"), 0.5), (a_note("F5"), 0.5), 
                                 (a_note("E5"), 0.5), (a_note("F5"), 0.5), (a_note("G5"), 1),
                                 (a_note("D5"), 0.5), (a_note("C5"), 0.5), (a_note("D5"), 0.5), (a_note("E5"), 0.5),
                                 (a_note("D5"), 1) ],     # note_durations
                               [ 64, 90 ],            # vel
                               [ 0 ],                     # octaves
                               [ 0.3, 0.5, 0.7 ],         # strettos
                               m,                         # midi obj
                               2),                        # midi channel
                               670, 700)                  # start, stop time

  # fragment 30: bells
  s.add_fragment(clustrificator.Clustrificator("Bells30",                    
                               [0,0,-1,0,0,1,0,0], 
                               [ (a_note("G4"), 1), 
                                 (a_note("C5"), 1), (a_note("C5"), 0.5), (a_note("D5"), 0.5),
                                 (a_note("E5"), 1), (a_note("C5"), 1),
                                 (a_note("G5"), 1.5), (a_note("F5"), 0.5),
                                 (a_note("E5"), 1.5), (a_note("E5"), 0.5),
                                 (a_note("F5"), 1), (a_note("G5"), 0.5), (a_note("F5"), 0.5), 
                                 (a_note("E5"), 0.5), (a_note("F5"), 0.5), (a_note("G5"), 1),
                                 (a_note("D5"), 0.5), (a_note("C5"), 0.5), (a_note("D5"), 0.5), (a_note("E5"), 0.5),
                                 (a_note("D5"), 1) ],     # note_durations
                               [ 64, 90 ],                # vel
                               [1],                       # octaves
                               [ 0.3, 0.5, 0.7 ],         # strettos
                               m,                         # midi obj
                               6),                        # midi channel
                               700, 730)                  # start, stop time



  # fragment 31: noises
  s.add_fragment(padgen.PadGen("ChipStrang31",
                               a_scale( ["B", "C", "C#", "F#","F","G"], [4,5] ),
                               [0.2, 0.1, 0.05],
                               [ 20, 40, 60 ],
                               [ 0 ],
                               [ 1 ],
                               m,
                               3),
                               650, 680)

  # fragment 32: Ioioioio
  s.add_fragment(padgen.PadGen("Ioioioioio32",
                               [a_note("G1"), a_note("Bb1"), a_note("C2")],
                               [ (float(i)/10) for i in xrange(5) ],
                               [ 60,90 ],
                               [ 1, 2, 3],
                               [ 4, 8 ],
                               m,
                               11),
                               670,
                               740)
 

  # fragment 33: clocks
  notes =["C", "C#", "D", "D#", "E", "F", "F#", "G","G#", "A", "A#", "B"] 
  random.shuffle(notes)
  s.add_fragment(noteinterpolator.NoteInterpolator("Clocks33",
                               a_scale(notes, [4,5]),                            # notes used during interpolation
                               [ (a_note("G4"), 1), 
                                 (a_note("C5"), 1), (a_note("C5"), 0.5), (a_note("D5"), 0.5),
                                 (a_note("E5"), 1), (a_note("C5"), 1),
                                 (a_note("G5"), 1.5), (a_note("F5"), 0.5),
                                 (a_note("E5"), 1.5), (a_note("E5"), 0.5),
                                 (a_note("F5"), 1), (a_note("G5"), 0.5), (a_note("F5"), 0.5), 
                                 (a_note("E5"), 0.5), (a_note("F5"), 0.5), (a_note("G5"), 1),
                                 (a_note("D5"), 0.5), (a_note("C5"), 0.5), (a_note("D5"), 0.5), (a_note("E5"), 0.5),
                                 (a_note("D5"), 1) ],     # note_durations
                               [ 64, 90 ],                # vel
                               [1],                       # octaves
                               [ 0.3, 0.5, 0.7 ],         # strettos
                               m,                         # midi obj
                               6),                        # midi channel
                               730, 752)                  # start, stop time

  # fragment 34: clock 
  s.add_fragment(padgen.PadGen("Clocks34", 
                               [a_note("C4") ], # notes
                               [2],             # durations
                               [127],           # velocities
                               [0],             # octaves
                               [8],             # strettos
                               m,               # midiobject
                               6),              # midi channel 1
                               753, 760)        # time 0 to 30


  # run the scheduler
  try:
    s.run(start_time=0)
  except KeyboardInterrupt:
    pass

  # whatever happens: clean up at the end
  s.cleanup()


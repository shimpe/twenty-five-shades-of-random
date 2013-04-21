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


import time

class DecoratedGenerator(object):
  """
  store a score generator object together with an activation and deactivation time
  """
  def __init__(self, generator, starttime, stoptime):
    """
    takes 3 parameters:
       generator: a threading.Thread object that generates midi events; 
                  it should react to a true value of a member variable "interrupt"  
                  by stopping the generation of midi events
       starttime: at what moment in time should this generator be activated?
       stoptime: at what moment in time should this generator be deactivated?
    """
    self.generator = generator
    self.starttime = starttime
    self.stoptime = stoptime
    self.running = False

  def start(self):
    """
    start the score generator
    """
    self.generator.start()
    self.running = True

  def stop(self):
    """
    stop the score generator
    """
    self.generator.cleanup()
    self.generator.interrupt = True
    self.running = False

  def instrname(self):
    return self.generator.instrname

  def must_start(self, time):
    return not self.running and (time > self.starttime) and (time < self.stoptime)

  def must_stop(self, time):
    return (time >= self.stoptime)

class Scheduler(object):
  """
  holds a scheduler, i.e. a class that decides when to start or stop which score generators
  """
  def __init__(self, resolution):
    """
    takes one parameter: resolution. Set e.g. to 1/1000 to get millisecond time resolution (usually this is overkill)
    """
    self.resolution = resolution
    self.invresolution = 1.0/self.resolution
    self.fragments = {}

  def add_fragment(self, generator, starttime, stoptime):
    """
    schedule an instance of a score generator
    """
    print "add_fragment:"
    print "instrname: ", generator.instrname
    print "starttime: ", starttime*self.invresolution
    print "stoptime: ", stoptime*self.invresolution
    if generator.instrname in self.fragments:
      assert False # shouldn't insert same instrumentname twice

    self.fragments[generator.instrname] = DecoratedGenerator(generator, starttime*self.invresolution, stoptime*self.invresolution)

  def remove_fragments(self, list_of_decoratedgenerator):
    """
    remove a all scheduled score generators
    """
    for dg in list_of_decoratedgenerator:
      self.remove_fragment(dg)

  def remove_fragment(self, decoratedgenerator):
    """
    remove one particular instance of a score generator
    """
    del self.fragments[decoratedgenerator.instrname()]

  def get_fragments_to_start_stop(self, current_time):
    """
    given current time current_time, find all registered
    score generators that are running and all fragments 
    whose expiration date has expired
    """
    starters = []
    stoppers = []

    for decoratedgenerator in self.fragments:
      dg = self.fragments[decoratedgenerator]
      if dg.must_start(current_time):
        starters.append(dg)
      elif dg.must_stop(current_time):
        stoppers.append(dg)

    if starters:
      print starters

    return ( starters, stoppers )

  def update(self, current_time):
    """
    start fragments that need to start
    stop fragments that need to stop
    remove obsolete fragments
    """
    starters, stoppers = self.get_fragments_to_start_stop(current_time)
    for s in starters:
      s.start()
    for s in stoppers:
      s.stop()
    self.remove_fragments(stoppers)

  def endtime(self):
    """
    find out how long the piece is
    """
    stoptime = 0
    for f in self.fragments:
      fragment = self.fragments[f]
      if fragment.stoptime > stoptime:
        stoptime = fragment.stoptime
    return stoptime

  def run(self, start_time=0, slowdownfactor=1):
    """
    run the score generators starting at start_time in the piece
    (useful to skip the beginning if you're working on a long piece),
    and with a slowdownfactor (useful if you want to hear things faster/slower)
    """
    final_time = self.endtime()
    start_time = start_time*self.invresolution

    starters, stoppers = self.get_fragments_to_start_stop(start_time)
    self.remove_fragments(stoppers)

    for t in xrange(int(final_time-start_time)):
      self.update(t+start_time)
      time.sleep(self.resolution)

  def cleanup(self):
    """
    stop all running fragments
    """
    for f in self.fragments:
      fragment = self.fragments[f]
      fragment.stop()

    self.fragments = {}

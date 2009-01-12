# MainloopFeedback.py -
# Copyright (C) 2008  Bastian Venthur
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


from Feedback import Feedback


class MainloopFeedback(Feedback):
    """Mainloop Feedback Base Class.
    
    This feedback derives from the Feedback Base Class and implements a main
    loop. More specifically it implements the following methods from it's base:
    
        on_init
        on_play
        on_pause
        on_stop
        on_quit
        
    which means that you should not need to re-implement those methods. If you
    choose to do so anyways, make sure to call MainloopFeedback's version first:
    
        def on_play():
            MainloopFeedback.on_play(self)
            # your code goes here
    
    MainloopFeedback provides the following new methods:
    
        init
        pre_mainloop
        post_mainloop
        tick
        pause_tick
        play_tick
    
    the class takes care of the typical steps needed to run a feedback with a
    mainloop, starting, pausing, stopping, quiting, etc. 
    
    While running it's internal mainloop it calls tick repeatedly. Additionally
    it calls either play_tick or pause_tick repeatedly afterwards, depending
    if the Feedback is paused or not.
    """

    def on_init(self):
        self.__running = False
        self.__paused = False
        self.__inMainloop = False
        self.init()

    def on_play(self):
        self.pre_mainloop()
        self.__mainloop()
        self.post_mainloop()

    def on_pause(self):
        self.__paused = not self.__paused

    def on_stop(self):
        self.__running = False

    def on_quit(self):
        self.__running = False
        while self.__inMainloop:
            pass

    def __mainloop(self):
        """
        Calls tick repeatedly. 
        
        Additionally it calls either pause_tick or
        play_tick, depending if the Feedback is paused or not.
        """
        self.__running = True
        self.__inMainloop = True
        while self.__running:
            self.tick()
            if self.__paused:
                self.pause_tick()
            else:
                self.play_tick()
        self.__inMainloop = False
        
    def init(self):
        """Called at the beginning of the Feedback's lifecycle.
        
        More specifically: in Feedback.on_init().
        """
        pass
        
    def pre_mainloop(self):
        """Called before entering the mainloop, e.g. after on_play."""
        pass
    
    def post_mainloop(self):
        """Called after leaving the mainloop, e.g. after stop or quit."""
        pass
            
    def tick(self):
        """
        Called repeatedly in the mainloop no matter if the Feedback is paused
        or not.
        """
        pass
    
    def pause_tick(self):
        """
        Called repeatedly in the mainloop if the Feedback is paused.
        """
        pass
    
    def play_tick(self):
        """
        Called repeatedly in the mainloop if the Feedback is not paused.
        """
        pass
        
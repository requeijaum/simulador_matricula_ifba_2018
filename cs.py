#!/usr/bin/env python

import curses
import curses.textpad
import time

def reset(screen):
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()


try:
	stdscr = curses.initscr()

	curses.noecho()
	#curses.echo()


	begin_x = 20
	begin_y = 7
	height = 5
	width = 40
	win = curses.newwin(height, width, begin_y, begin_x)
	tb = curses.textpad.Textbox(win)
	text = tb.edit()
	curses.addstr(4,1,text.encode('utf_8'))

	hw = "Hello world!"
	while 1:
		c = stdscr.getch()
		
		if c == ord('p'):
			print(hw)
		
		elif c == ord('q'): break # Exit the while()
		
		elif c == curses.KEY_HOME: x = y = 0

	curses.endwin()
	
except KeyboardInterrupt:
    reset(stdscr)
    exit()

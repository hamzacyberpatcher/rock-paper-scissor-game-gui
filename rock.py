from tkinter import *
from random import randint
import pygame
from pygame import *

sc = 0
sp = 0
r = 0

pygame.init()

tie_Sound = mixer.Sound("tie.wav")
lose_Sound = mixer.Sound("lose.wav")
win_Sound = mixer.Sound("win.wav")


def rock():
	y = randint(1,3)
	global sc, sp, r
	r = r + 1
	round_tag.configure(text = '{}'.format(r))
	you_choice.configure(text = 'Rock')
	if y == 1:
		comp_choice.configure(text = 'Rock')
		status_output.configure(text = 'Tie', fg = 'blue')
		you_score.configure(text = '{}'.format(sp))
		comp_score.configure(text = '{}'.format(sc))
		tie_Sound.play()
	if y == 2:
		sc = sc + 1
		comp_choice.configure(text = 'Paper')
		status_output.configure(text = 'Lose', fg = 'red')
		you_score.configure(text = '{}'.format(sp))
		comp_score.configure(text = '{}'.format(sc))
		lose_Sound.play()
	if y == 3:
		sp = sp + 1
		comp_choice.configure(text = 'Scissor')
		status_output.configure(text = 'Win', fg = 'green')
		you_score.configure(text = '{}'.format(sp))
		comp_score.configure(text = '{}'.format(sc))
		win_Sound.play()
	if sp > sc:
		you_score.configure(fg = 'green')
		comp_score.configure(fg = 'red')
	elif sp < sc:
		you_score.configure(fg = 'red')
		comp_score.configure(fg = 'green')
	elif sp == sc:
		you_score.configure(fg = 'blue')
		comp_score.configure(fg = 'blue')

def paper():
	y = randint(1,3)
	global r, sc, sp
	r = r + 1
	round_tag.configure(text = '{}'.format(r))
	you_choice.configure(text = 'Paper')
	if y == 1:
		sp = sp + 1
		comp_choice.configure(text = 'Rock')
		status_output.configure(text = 'Win', fg = 'green')
		you_score.configure(text = '{}'.format(sp))
		comp_score.configure(text = '{}'.format(sc))
		win_Sound.play()
	if y == 2:		
		comp_choice.configure(text = 'Paper')
		status_output.configure(text = 'Tie', fg = 'blue')
		you_score.configure(text = '{}'.format(sp))
		comp_score.configure(text = '{}'.format(sc))
		tie_Sound.play()
	if y == 3:
		sc = sc + 1
		comp_choice.configure(text = 'Scissor')
		status_output.configure(text = 'Lose', fg = 'red')
		you_score.configure(text = '{}'.format(sp))
		comp_score.configure(text = '{}'.format(sc))
		lose_Sound.play()
	if sp > sc:
		you_score.configure(fg = 'green')
		comp_score.configure(fg = 'red')
	elif sp < sc:
		you_score.configure(fg = 'red')
		comp_score.configure(fg = 'green')
	elif sp == sc:
		you_score.configure(fg = 'blue')
		comp_score.configure(fg = 'blue')

def scissor():
	y = randint(1,3)
	global sc, sp, r
	r = r + 1
	round_tag.configure(text = '{}'.format(r))
	you_choice.configure(text = 'Rock')
	you_choice.configure(text = 'Scissor')
	if y == 1:
		sc = sc + 1
		comp_choice.configure(text = 'Rock')
		status_output.configure(text = 'Lose', fg = 'red')
		you_score.configure(text = '{}'.format(sp))
		comp_score.configure(text = '{}'.format(sc))
		lose_Sound.play()
	if y == 2:
		sp = sp + 1		
		comp_choice.configure(text = 'Paper')
		status_output.configure(text = 'Win', fg = 'green')
		you_score.configure(text = '{}'.format(sp))
		comp_score.configure(text = '{}'.format(sc))
		win_Sound.play()
	if y == 3:
		comp_choice.configure(text = 'Scissor')
		status_output.configure(text = 'Tie', fg = 'blue')
		you_score.configure(text = '{}'.format(sp))
		comp_score.configure(text = '{}'.format(sc))
		tie_Sound.play()
	if sp > sc:
		you_score.configure(fg = 'green')
		comp_score.configure(fg = 'red')
	elif sp < sc:
		you_score.configure(fg = 'red')
		comp_score.configure(fg = 'green')
	elif sp == sc:
		you_score.configure(fg = 'blue')
		comp_score.configure(fg = 'blue')

def reset():
	global sc, sp, r
	you_score.configure(text = '0')
	comp_score.configure(text = '0')
	you_choice.configure(text = '')
	comp_choice.configure(text = '')
	status_output.configure(text = '')
	round_tag.configure(text = '0')
	sc = 0
	sp = 0
	r = 0

root = Tk()
root.title("Rock, Paper, Scissor")
root.configure(bg = '#FFFB00')
root.resizable(False,False)
root.iconbitmap('i.ico')
rock = Button(text = "Rock", font = ('Verdana', 16), command = rock, bg = 'blue',width = 7)
paper = Button(text = "Paper", font = ('Verdana', 16), command = paper, bg = 'red',width = 7)
scissor = Button(text = "Scissor", font = ('Verdana', 16), command = scissor, bg = 'green',width = 7)
you_choice = Label(font=('Verdana', 16), width = 8, bg = '#FFFB00')
comp_choice = Label(font=('Verdana', 16), width = 8, bg = '#FFFB00')
you_score = Label(text = '0', font=('Verdana', 16),width = 4, bg = '#FFFB00')
comp_score = Label(text = '0', font=('Verdana', 16),width = 4, bg = '#FFFB00')
status_output = Label(font=('Verdana', 16), bg = '#FFFB00')
you_display_one = Label(text = "You: ", font=('Verdana', 16), bg = '#FFFB00')
you_display_two = Label(text = "You: ", font=('Verdana', 16), bg = '#FFFB00')
comp_display_one = Label(text = "Comp: ", font=('Verdana', 16), bg = '#FFFB00')
comp_display_two = Label(text = "Comp: ", font=('Verdana', 16), bg = '#FFFB00')
status_tag = Label(text = "Status: ", font=('Verdana', 16),bg = '#FFFB00')
round_display = Label(text = 'Rounds: ', font = ('Verdana', 16), bg = '#FFFB00')
round_tag = Label(text = '0', font = ("Verdana",16), bg = "#FFFB00", width = 4)
reset = Button(text = "Reset", font = ('Verdana',16), command = reset, bg = 'red',width = 34)

rock.grid(row=0,column=0)
paper.grid(row=1,column=0)
scissor.grid(row=2,column=0)
you_display_one.grid(row=0,column=1)
comp_display_one.grid(row=1,column=1)
status_tag.grid(row=2,column=1)
you_choice.grid(row=0,column=2)
comp_choice.grid(row=1,column=2)
status_output.grid(row=2,column=2)
you_display_two.grid(row=0,column=3)
comp_display_two.grid(row=1,column=3)
you_score.grid(row=0,column=4)
comp_score.grid(row=1,column=4)
round_display.grid(row = 2, column = 3)
round_tag.grid(row = 2, column = 4)
reset.grid(row=3,columnspan=5)

mainloop()
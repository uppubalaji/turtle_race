from turtle import *
from random import randint
participants = int(input("How many turtles are in the race: "))
screen = Screen()
screen.title("Turtle Race")
screen.setup(width=450, height=450)
bet1 = screen.textinput("Make your bet", "Which turtle will win the race? Enter a number: ")
def no_of_turtles(n):
	list1 = []
	xpos = -200
	ypos = -200
	colormode(255)
	for i in range(n):
		day19 = Turtle()
		day19.shape("turtle")
		day19.color(randint(0,255),randint(0,255),randint(0,255))
		day19.penup()
		day19.goto(xpos, ypos)
		day19.pendown()
		ypos = ypos + (400/(n-1))
		list1.append(day19)
	game_over = False
	while not game_over:
		for i in list1:
			if i.xcor() > 185:
				win = list1.index(i)
				if int(win) == int(bet1):
					print("You,ve Won!")
				else:
					print(f"You lose!, {win} won the race.")
				game_over = True
			sp = randint(0,10)
			i.forward(sp)
				
no_of_turtles(participants)
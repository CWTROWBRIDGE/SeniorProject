import sys
import re
import numpy as np
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style
import State
import Classes
import random

print("ready \n")

EPCount = 5000
PlayCost = 1
DamagePenalty = 50
WinReward = 25
Epsilon = 0.9
EpsilonDecay = 0.95
LearningRate = 0.1
Discount = 0.95

start_q_table = None

Agent = Classes.Agent()

if start_q_table == None:
	q_table = {}


for i in range(EPCount):
	currentState = Agent.state()
	availableCommands = State.get_commands(currentState)
	inGame = State.in_game()
	if inGame == False:
		Agent.start()
		x=input("choose 0\n")
		x=input("choose 1\n")
		x=input("choose 0\n")
		x=input("choose 0\n")
	else:
		commands = State.get_commands(currentState)
		temp = re.search("confirm", str(commands))
		if temp != None:
			Agent.confirm()
			continue
		temp = re.search("choose", str(commands))
		if temp != None:
			choice = random.randint(0,3)
			Agent.choose(choice)
			continue
		temp = re.search("proceed", str(commands))
		if temp != None:
			Agent.proceed()
			continue
		temp = re.search("play", str(commands))
		energy = State.get_energy(currentState)
		if energy == "0":
			Agent.end()
			continue
		if temp != None:
			card = random.randint(1,5)
			Agent.play(card)
			continue
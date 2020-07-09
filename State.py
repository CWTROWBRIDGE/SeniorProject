import sys
import re

def get_commands(current_state):
	count = 0
	x = current_state.split(":")
	for i in x:
		count = count + 1
		z = re.search("available_commands", i)
		if z != None:
			a = x[count]
			b = a.split("]")
			c = b[0].split("[")
			return c[1]
			break

def in_game():
	state = input("state\n")
	x = get_commands(state)
	y = re.search("start", str(x))
	if y != None:
		return False
	else:
		return True
	
def victory_status():
	print("state \n")
	x=input()
	y = x.split(":")
	for i in y:
		z = re.search("victory", str(i))
		if z != "None":
			Next = True
		elif Next == True:
			return "victory"
			break

def get_energy(current_state):
	count = 0
	y = current_state.split(":")
	for i in y:
		count = count + 1
		z = re.search("energy", str(i))
		if z != None:
			a = y[count]
			return a[0]
			break
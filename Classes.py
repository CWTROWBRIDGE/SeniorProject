import re

class Agent:
    def choose(self, id):
        x=input("choose " + str(id) + " \n")
    def play(self, card):
            x = input("play " + str(card) + " 0\n")
            m = re.search("with the selected target", str(x))
            if m != None:
                x = input("play " + str(card) + " 1\n")
    def start(self):
        x=input("Start Ironclad 0 27WIYPBKT3YB0\n")
    def end(self):
        x=input("key End_Turn\n")
    def state(self):
        x=input("state\n")
        return str(x)
    def confirm(self):
        x=input("confirm\n")
    def proceed(self):
        x=input("proceed\n")
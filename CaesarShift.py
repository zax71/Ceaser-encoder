# imports -----
from guizero import App, Text, PushButton, TextBox
import random

#Variables -----

shift = 0
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# Functions -----

def getShift():
    global shift
    shift=random.randint(0, 27)
    shiftText.value = "Your Shift Is: " + str(shift)
    
def getInputShift():
    global shift
    shift = int(inputShift.value)

def runShift():
    caesar_encrypt(textBoxNormal.value, shift)

def caesar_encrypt(realText, step):
	outText = []
	cryptText = []
	
	uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	for eachLetter in realText:
		if eachLetter in uppercase:
			index = uppercase.index(eachLetter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = uppercase[crypting]
			outText.append(newLetter)
		elif eachLetter in lowercase:
			index = lowercase.index(eachLetter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = lowercase[crypting]
			outText.append(newLetter)

	textBoxCypher.value = "".join(outText)
    

# items -----
app = App(title="Hello World", width=700, height=700, layout="grid")#make the window
app.bg = "#368034"

title = Text(app, text="Caesar Shift Example", grid=[0, 0])
title.text_size = 45
title.text_color = "#FFFFFF"
title.font = "Impact"

shiftText = Text(app, text="Your Shift Is: ", grid=[0, 1], align="left")
shiftText.text_color = "#FFFFFF"

chooseShift = PushButton(app, getShift, text="Choose Shift", grid=[1, 1], padx=2, pady=2)
chooseShift.bg = "#FF0000"
chooseShift.text_color = "#FFFFFF"

inputShift = TextBox(app, "Input a pre-made shift here", grid=[0, 2], width=20, align="left")

chooseInputShift = PushButton(app, getInputShift, text="Enter Shift", grid=[1, 2], padx=2, pady=2)
chooseInputShift.bg = "#FF0000"
chooseInputShift.text_color = "#FFFFFF"

textBoxNormal = TextBox(app, text="enter normal text here...", width=45, grid=[0, 3])
textBoxCypher = TextBox(app, text="...and pop out text here!", width=45, grid=[0, 4])

inputButton = PushButton(app, runShift, text="Apply The Cypher", grid=[1, 3], padx=2, pady=2)
inputButton.bg = "#FF0000"
inputButton.text_color = "#FFFFFF"

# Display -----
app.display()#run the app
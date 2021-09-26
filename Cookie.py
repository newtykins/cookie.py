from structures import GameManager, gui
from tkinter import Button, Label, PhotoImage
import os
import ctypes

user32 = ctypes.windll.user32
screenSize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
assetsDir = os.path.dirname(os.path.realpath(__file__)) + '/assets/'

# Intitate the window, stores, and menu
window = gui.Window('Cookie Clicker', '%ix%i+0+0' % (screenSize[0] - 250, screenSize[1] - 250), '#d38808')
manager = GameManager()
menuBar = gui.Menu(window, manager)
window.config(menu=menuBar)

# Bind a label to the cookie store and if you click the label increment the CPS
cookieImage = PhotoImage(file=assetsDir + 'cookie.png')
cookieButton = Button(window, image=cookieImage, pady=50)
cookieButton.bind('<1>', lambda e: manager.cookies.add())
cookieLabel = Label(window, textvariable=manager.cookies.output)

# Bind a label to each generator store and if you click the label, buy one of that generator
# generatorButtons = []
# generatorLabels = []

# for generator in manager.generators.values():
# 	generatorLabel = Label(window, textvariable=generator.output)
# 	generatorLabel.bind('<Button-1>', lambda e: generator.buy())

# Bind a label to the cookie store's CPS and if you click the label increment the CPS
cpsLabel = Label(window, textvariable=manager.cookies.cpsOutput)
cpsLabel.bind('<Button-1>', lambda e: manager.cookies.addCPS())

# Start the window
window.components = [
	(cookieButton, 0, 50),
	(cookieLabel, 0, 0, ("Calibri", 24)),
	(cpsLabel, 0, 0, ("Calibri", 18))
]

window.start()

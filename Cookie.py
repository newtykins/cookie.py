from structures import GameManager, gui
from tkinter import Label

# Intitate the window, stores, and menu
window = gui.Window('Cookie Clicker', '750x750')
manager = GameManager()
menuBar = gui.Menu(window, manager)
window.config(menu=menuBar)

# Bind a label to the cookie store and if you click the label increment the CPS
cookieLabel = Label(window, textvariable=manager.cookies.output)
cookieLabel.bind('<Button-1>', lambda e: manager.cookies.add())
cookieLabel.pack()

# Bind a label to each generator store and if you click the label, buy one of that generator
for generator in manager.generators.values():
	generatorLabel = Label(window, textvariable=generator.output)
	generatorLabel.bind('<Button-1>', lambda e: generator.buy())
	generatorLabel.pack()

# Bind a label to the cookie store's CPS and if you click the label increment the CPS
cpsLabel = Label(window, textvariable=manager.cookies.cpsOutput)
cpsLabel.bind('<Button-1>', lambda e: manager.cookies.addCPS())
cpsLabel.pack()

# Start the window
window.start()

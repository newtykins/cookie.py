from structures.Window import Window
from structures.Stores import CookieStore, GeneratorStore
from tkinter import *

window = Window('Cookie Clicker')
cookies = CookieStore()
grandmas = GeneratorStore(2)

# Bind a label to the cookie store and if you click the label increment the CPS
cookieLabel = Label(window.root, textvariable=cookies.output)
cookieLabel.bind('<Button-1>', lambda e: cookies.addCPS())
cookieLabel.pack()

# Bind a label to the grandma store and if you click the label increment the quantity of granmas
grandmaLabel = Label(window.root, textvariable=grandmas.output)
grandmaLabel.bind('<Button-1>', lambda e: grandmas.add(cookies))
grandmaLabel.pack()

# Start the window
window.start()

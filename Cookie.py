from structures.Window import Window
from structures.Stores import CookieStore
from tkinter import *

window = Window('Cookie Clicker')
cookies = CookieStore()

# Bind a label to the cookie store and if you click the label increment the CPS
cookieLabel = Label(window.root, textvariable=cookies.output)
cookieLabel.bind('<Button-1>', lambda e: cookies.addCPS())
cookieLabel.pack()

# Start the window
window.start()

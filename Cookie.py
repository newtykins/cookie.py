from structures.Window import Window
from structures.Menu import Menu
from structures.Stores import CookieStore, GeneratorStore
from tkinter import Label

# Intitate the window, stores, and menu
window = Window('Cookie Clicker', '750x750')
cookies = CookieStore()
grandmas = GeneratorStore(cookies, 'Grandmas', 10, 2)
generators = [grandmas]
menuBar = Menu(window, cookies, generators)
window.config(menu=menuBar)

# Bind a label to the cookie store and if you click the label increment the CPS
cookieLabel = Label(window, textvariable=cookies.output)
cookieLabel.bind('<Button-1>', lambda e: cookies.add())
cookieLabel.pack()

# Bind a label to the grandma store and if you click the label increment the quantity of granmas
grandmaLabel = Label(window, textvariable=grandmas.output)
grandmaLabel.bind('<Button-1>', lambda e: grandmas.add())
grandmaLabel.pack()

# Bind a label to the cookie store's CPS and if you click the label increment the CPS
cpsLabel = Label(window, textvariable=cookies.cpsOutput)
cpsLabel.bind('<Button-1>', lambda e: cookies.addCPS())
cpsLabel.pack()

# Start the window
window.start()

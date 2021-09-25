from tkinter import Tk

class Window(Tk):
	def __init__(self, title: str, geometry: str):
		super().__init__()
		self.title(title)
		self.geometry(geometry)

	def start(self):
		self.mainloop()

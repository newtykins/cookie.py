from tkinter import Tk

class Window():
	def __init__(self, title: str):
		self.root = Tk()
		self.root.title(title)
		self.root.geometry('750x750')

	def start(self):
		self.root.mainloop()

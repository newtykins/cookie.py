from tkinter import Button, Label, Tk

class Window(Tk):
	def __init__(self, title: str, geometry: str, bgColour: str):
		super().__init__()
		self.title(title)
		self.geometry(geometry)
		self.bgColour = bgColour
		self.components = []

	def start(self):
		# Pack the components with their individual configs
		# ( component, padding x, padding y )
		# if Label, 4th value of tuple is another tuple containing font info
		# ( fontSize )
		for c in self.components:
			component = c[0]
			padX = c[1]
			padY = c[2]
			if isinstance(component, Button):
				component.configure(highlightthickness=0, bd=0, activebackground=self.bgColour)
			elif isinstance(component, Label):
				labelConfig = c[3]
				component.configure(font=(labelConfig[0], labelConfig[1]))
			component.configure(bg=self.bgColour)
			component.pack(padx=padX, pady=padY)
		self.configure(bg=self.bgColour)
		self.mainloop()

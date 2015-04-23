from tkinter import *

class Window:
	def __init__(self, master):
		self.master = master
		master.title("Window Title")
		master.geometry("800x450")
		master.resizable(0,0)	
		master.config(background='black')

		self.label = Label(master, text="Enter Color Below", background='black', fg='white')
		self.label.pack()
		
		self.text_input = Entry(master, bd='0')
		self.text_input.pack()
		
		self.print_text = Button(master, text="Change Background Color", command=self.change_color, highlightbackground='black')
		self.print_text.pack()

		self.close_button = Button(master, text="Close", command=master.quit, highlightbackground='black')
		self.close_button.pack()

	def change_color(self):
		self.input_color = self.text_input.get()
		self.master.config(background=self.input_color)
		self.label.config(background=self.input_color)
		self.text_input.config(bd='0')
		self.print_text.config(highlightbackground=self.input_color)
		self.close_button.config(highlightbackground=self.input_color)
		if (self.input_color == 'black'):
			self.label.config(fg='white')
		else:
			self.label.config(fg='black')
root = Tk()
Window_var = Window(root)
root.mainloop()

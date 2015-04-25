from tkinter import *

class Window:
	def __init__(self, master):
		self.master = master
		master.title("Window Title")
		master.geometry("800x450")
		master.resizable(0,0)	
		master.config(background='black')

		master.columnconfigure(0, pad=3)
		master.columnconfigure(1, pad=3)

		master.rowconfigure(0, pad=3)
		master.rowconfigure(1, pad=3)
		master.rowconfigure(2, pad=3)

		self.label = Label(master, text="Enter Color:", background='black', fg='white')
		self.label.grid(row=1, column=0, sticky=W)
		
		self.text_input = Entry(master, bd='0')
		self.text_input.grid(row=1, column=0, sticky=W)
		
		self.print_text = Button(master, text="Change Background Color", command=self.change_color, highlightbackground='black')
		self.print_text.grid(row=1, column=0, sticky=W)
		
		self.draw_line_button = Button(master, text="Draw Line", command=self.draw_line('red', 0, 0, 0, 'right'), highlightbackground='black')
		self.draw_line_button.grid(row=2, column=0)

		self.close_button = Button(master, text="Close", command=master.quit, highlightbackground='black')
		self.close_button.grid(row=2, column=1, sticky=S+W)

	def change_color(self):
		self.input_color = self.text_input.get()
		self.master.config(background=self.input_color)
		self.label.config(background=self.input_color)
		self.text_input.config(bd='0')
		self.print_text.config(highlightbackground=self.input_color)
		self.draw_line_button.config(highlightbackground=self.input_color)
		self.close_button.config(highlightbackground=self.input_color)
		if (self.input_color == 'black'):
			self.label.config(fg='white')
		else:
			self.label.config(fg='black')
	def draw_line(self, line_color, line_length, line_start_x, line_start_y, line_direction):
		self.color = line_color
		self.length = line_length
		self.start_x = line_start_x
		self.start_y = line_start_y
		self.direction = line_direction
root = Tk()
Window_var = Window(root)
root.mainloop()

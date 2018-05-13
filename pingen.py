#!/usr/bin/env python3

from tkinter import Tk, Label, Button
import os
import random

class PINGEN:
	def __init__(self, master):
		self.master = master
		master.title("PIN Generator")

		self.label = Label(master, text="Would you like to create a new PIN?", font = "Courier 20 bold")
		self.label.pack()

		self.greet_button = Button(master, text="Generate PIN", bg="#909090",fg='red', font = "Courier 16 bold", padx=5, pady=5, highlightbackground='#555555',activeforeground='red',activebackground='orange',width="20", relief="raised", bd="6", command=self.greet)
		self.greet_button.pack()

		self.close_button = Button(master, text="Exit", bg="#959595", fg='green', font = "Courier 16 bold", padx=5, pady=5,highlightbackground='#555555',activeforeground='green',activebackground='orange', width="20", relief="raised", bd="6", command=master.quit)
		self.close_button.pack()


	def greet(self):
		os.system('clear')
		print("Generating new PIN now...")
		mypin = random.randrange(1000,9999)
		print(mypin)


root = Tk()
my_gui = PINGEN(root)
root.title("Four digit PIN generator")
root.geometry("575x150+250+225")
root.mainloop()

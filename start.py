from Fix import Fix  
from Noisy import Noisy
import Show
import tkinter as tk
from tkinter import filedialog as fd  

name = ''

def callback():
	ftypes = [('Картинки', '*.jpg'), ('Все файлы', '*')]
	name= fd.askopenfilename(filetypes = ftypes) 
	return(name)

def call():
	global name
	name = callback()	

def zad1():
	global name

	if name == '':
		pass
	else:
		proga = Show.Show(name)
		proga.showimage()

def zad2():
	global name

	if name == '':
		pass
	else:
		proga = Noisy.Nois(name)
		proga.showimage()

def zad3():
	global name

	if name == '':
		pass
	else:
		proga = Fix.Fix(name)
		proga.showimage()

btn1 = tk.Button(text='Click to Open File',command=call)
btn1.pack(fill=tk.X)

btn2 = tk.Button(text='zad1',command=zad1)
btn2.pack()

btn3 = tk.Button(text='zad2',command=zad2)
btn3.pack()

btn4 = tk.Button(text='zad3',command=zad3)
btn4.pack()

tk.mainloop()

###python setup.py build_ext --inplace
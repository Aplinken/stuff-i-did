import tkinter as tk
from tkinter import messagebox
import pickle

def add(): #adds tasks
	task = ent_task.get()
	if task == '' or task.isspace() is True:
		messagebox.showwarning(title='Error',message='Entry cannot be 0 characters long!')
	else:
		lstbox_list.insert(tk.END, task)
		ent_task.delete(0, tk.END)

def delete(): #deletes selected task
	try:
		task = lstbox_list.curselection()[0]
		lstbox_list.delete(task)
	except:
		messagebox.showwarning(title='Error',message='You must select the item you want to remove!')
	
def save(): #saves the listbox onto todo_save.dat
	tasks = lstbox_list.get(0, lstbox_list.size())
	pickle.dump(tasks, open('todo_save.dat','wb'))

def load(): #loads from any previous save(todo_save.dat)
	try:
		tasks = pickle.load(open('todo_save.dat','rb'))
		lstbox_list.delete(0, tk.END)
		for task in tasks:
			lstbox_list.insert(tk.END, task)
	except:
		messagebox.showwarning(title='Error',message='You need to save before loading!')

window = tk.Tk() #create the window instance
window.title("To-Do List Creator By @aplinken") 

frm_lstbox = tk.Frame()
frm_lstbox.pack()

lstbox_list = tk.Listbox(frm_lstbox,width=50,height=20) #the listbox that contains all the tasks
lstbox_list.pack(side=tk.LEFT)

scrl_scrollbar = tk.Scrollbar(frm_lstbox) #Scrolling *bruh*
scrl_scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

lstbox_list.config(yscrollcommand=scrl_scrollbar.set)
scrl_scrollbar.config(command=lstbox_list.yview) #making the scrollbar functional

ent_task = tk.Entry(window,width=50)
ent_task.pack()

btn_add = tk.Button(window,width=44,text='Add',command=add)
btn_add.pack()

btn_del = tk.Button(window,width=44,text='Delete',command=delete)
btn_del.pack()

btn_save = tk.Button(window,width=44,text='Save',command=save)
btn_save.pack()

btn_load = tk.Button(window,width=44,text='Load',command=load)
btn_load.pack()

window.mainloop()

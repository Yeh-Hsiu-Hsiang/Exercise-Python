import tkinter
test=tkinter.Tk()
test.mainloop()

tr = ['lala','lulu']
tr_list =Listbox(test)

for i in tr:
	tr_list.insert(0,i)

tr_list.pack()
test.mainloop()
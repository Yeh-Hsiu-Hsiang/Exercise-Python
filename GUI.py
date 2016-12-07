import tkinter
test=tkinter.Tk()

test.title('GUI test')
a_label = tkinter.Label(test,text='Hello,Welcome to here!',fg='blue',width='30',height='20')
b_button = tkinter.Button(test,text='Exit')
c_button = tkinter.Button(test,text='Enter')
# d_txf = tkinter.TextField(test,text='Please input your value', fg='black', wigth = '30', height='20')

a_label.pack() #show element
b_button.pack(side='bottom',fill='both', expand=1,padx=10,pady=10)
c_button.pack(side='top',fill='both', expand=1,padx=10,pady=10)
# d_txf.pack(side='center')

def ClickExit(test):
	tkinter.exit()

test.mainloop() #enter mainloop

# menubar = Menu(test)
# filemenu = Menu(menubar,tearoff = 0)
# filemenu.add_command(Label='Open',command='hello')
# menubar.add_cascade(Label="File",menu = 'filemenu')

def createWidgets(self):
	self.inputText = Label(self)
	self.inputText["text"] = "Input:"
	self.inputText.grid(row=0, column=0)
	self.inputField = Entry(self)
	self.inputField["width"] = 20
	self.inputField.grid(row=0, column=1, columnspan=6)
 
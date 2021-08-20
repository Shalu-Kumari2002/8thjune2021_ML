#GUI Development with Tkinter

#1. TK()
#~app
#~app.geometry
#~app.title
#2.Label
#3.Entry
#4.Button
#5.Option menu
#6.List box
#7.radio button
#8. menu ,
#9.spin box
#10.combobox
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as tdp
from PIL import ImageTk,Image

app = tk.Tk()
app.title('Testing App')
app.geometry("300x800")
#upto here only layout named testing app with defined geometry will appear


label = tk.Variable(app)
label.set('simple text')
tk.Label(app,textvariable = label).pack()
#upto here only a label will be shown

#for mutilines
msg = tk.Variable(app)
msg.set('''first line
second line
third line''')
tk.Message(app,textvariable = msg).pack()

entry = tk.Variable(app)
entry.set('0')
tk.Entry(app,textvariable = entry).pack()
#an entry box with value as 0 will b shown

def cmd():
    print('clicked')
    print(sp.get())
    print('python',cb1.get())
    print('Ds',cb2.get())
    print('Batch',rb.get())
    print('Combo:',cmb.get())
    if cmb.get() == 'Project:4':
        cmb_box['values'] = ('Topic:1','Topic:2')
        cmb.set("")
    print(opt.get())
    print(lb.get())

    
tk.Button(app, text = 'click',command = cmd).pack()

#
sp = tk.Variable(app)
##sp = tk.IntVar(app)
tk.Spinbox(app, from_ = 0, to=100,textvariable =sp).pack()


#check buttons

cb1 = tk.Variable(app,'0')
cb2 = tk.Variable(app,'0')
tk.Checkbutton(app, text ='Python',variable = cb1, onvalue=
               1,offvalue =0).pack()
tk.Checkbutton(app, text ='Datascience',variable = cb2, onvalue=
               1,offvalue =0).pack()

rb = tk.Variable(app,'1')
values = {"8th June-ML":'1','15th June-ML':'2',
          "8th June-AI":'3',"15th June-AI":'4'}

for k,v in values.items():
    tk.Radiobutton(app,text = k,variable = rb, value = v).pack()
##in radio button only one will be checked at once


#Combo box
    # import ttk
cmb = tk.Variable(app)
cmb_values = ("Project:1","Project:2","Project:3","Project:4")
cmb_box = ttk.Combobox(app, textvariable = cmb , values =cmb_values)
cmb_box.pack()
#if i want inside project some attributes then we will use
#Then we will put values inside the values attribute of ttk cmbobox
 # now we have option menu , cmb box and it is almost same

opt = tk.Variable(app)
opt_values = ("Option:1","Option:2")
opt_menu = tk.OptionMenu(app, opt,*opt_values)
opt_menu.pack()

#Listbox

lb = tk.Variable(app)
list_box = tk.Listbox(app, height=5,activestyle = 'dotbox',fg = 'red')
list_box.insert(1,'Shalu')
list_box.insert(2,'soni')
list_box.insert(3,'Rinita')
list_box.pack()


#image loading
def opn():
    file = tdp.askopenfile(mode = 'r',filetypes = [('Images','*png')])
    if file:
        file_name = file.name
    print(file)
tk.Button(app, text= 'Select Image', command = opn).pack()

can = tk.Canvas(app,width = 300, height = 300)
can.pack()
img = ImageTk.PhotoImage(Image.open('C:/Users/Shalu Kumari/OneDrive/Pictures/Saved Pictures/hulk.png'))
can.create_image(20,20,anchor = tk.NW , image = img)






    
    
app.mainloop()




























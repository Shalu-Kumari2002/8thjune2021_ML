import tkinter as tk
app = tk.Tk()
app.title("Basic Calculator")
app.geometry('500x500')
output = tk.Variable(app)
val =tk.Variable(app)
box = tk.Entry(app, textvariable = val,width=37,bg = 'beige',highlightthickness=2,font=('Timesroman',16,'normal'))
box.place(x = 20,y =10,height=80)

  
# highlightbackground and highlightcolor for the border color
box.config(highlightbackground = "red", highlightcolor= "red")

  
input_v = ""

def operate(e):
    global input_v
    input_v += str(e)
    val.set(input_v)
    
    

def clear():
    global input_v
    box.delete(0,'end')
    input_v = ''
 
def output(s):
    global input_v
    val.set(eval(input_v))
    input = ""
    
    

tk.Button(app, text = '1',bd ='3',font ="Andalus",fg ='red',bg ='purple',relief ="groove",highlightcolor="purple",width =10,height = 2,command =lambda :operate('1')).place(x =20,y=190)
tk.Button(app, text = '2',bd ='3',font ='calibri',fg ='red',bg ='purple',relief ="groove",highlightcolor="purple",width =10,height = 2,command =lambda :operate('2')).place(x =140,y=190)
tk.Button(app, text = '3',bd ='3',font ='calibri',fg ='red',bg ='purple',relief ="groove",highlightcolor="purple",width =10,height = 2,command =lambda :operate('3')).place(x =260,y=190)
tk.Button(app, text = '+',bd ='3',font ='calibri',fg ='red',bg ='purple',relief ="groove",highlightcolor="purple",width =10,height = 2,command =lambda :operate('+')).place(x =380,y=190)
tk.Button(app, text = '4',bd ='3',font ='calibri',fg ='red',bg ='purple',relief ="groove",highlightcolor="purple",width =10,height = 2,command =lambda :operate('4')).place(x =20,y=270)
tk.Button(app, text = '5',bd ='3',font ='calibri',fg ='red',bg ='purple',relief ="groove",highlightcolor="purple",width =10,height = 2,command =lambda :operate('5')).place(x =140,y=270)
tk.Button(app, text = '6',bd ='3',font ='calibri',fg ='red',bg ='purple',relief ="groove",highlightcolor="purple",width =10,height = 2,command =lambda :operate('6')).place(x =260,y=270)
tk.Button(app, text = '-',bd ='3',font ='calibri',fg ='red',bg ='purple',relief ="groove",highlightcolor="purple",width =10,height = 2,command =lambda :operate('-')).place(x =380,y=270)
tk.Button(app, text = '7',bd ='3',font ='calibri',fg ='red',bg ='purple',relief ="groove",highlightcolor="purple",width =10,height = 2,command =lambda :operate('7')).place(x =20,y=350)
tk.Button(app, text = '8',bd ='3',font ='calibri',fg ='red',bg ='purple',relief ="groove",highlightcolor="purple",width =10,height = 2,command =lambda :operate('8')).place(x=140,y=350)
tk.Button(app, text = '9',bd ='3',font ='calibri',fg ='red',bg ='purple',relief ="groove",highlightcolor="purple",width =10,height = 2,command =lambda :operate('9')).place(x =260,y=350)
tk.Button(app, text = 'x',bd ='3',font ='calibri',fg ='red',bg ='purple',relief ="groove",highlightcolor="purple",width =10,height = 2,command =lambda :operate('*')).place(x =380,y=350)
tk.Button(app, text = '.',bd ='3',font ='calibri',fg ='red',bg ='purple',relief ="groove",highlightcolor="purple",width =10,height = 2,command =lambda :operate('.')).place(x =20,y=430)
tk.Button(app, text = '0',bd ='3',font ='calibri',fg ='red',bg ='purple',relief ="groove",highlightcolor="purple",width =10,height = 2,command =lambda :operate('0')).place(x =140,y=430)
tk.Button(app, text = '=',bd ='3',font ='calibri',fg ='red',bg ='purple',relief ="groove",highlightcolor="purple",width =10,height = 2,command =lambda :output('='
                                                                                                                                                               )).place(x =260,y=430)
tk.Button(app, text = '/',bd ='3',font ='calibri',fg ='red',bg ='purple',relief ="groove",highlightcolor="purple",width =10,height = 2,command =lambda :operate('/')).place(x=380,y=430)
tk.Button(app, text = 'clear',bd ='3',font ='calibri',fg ='red',bg ='purple',relief ="groove",highlightcolor="purple",width =10,height = 2,command =lambda:clear()).place(x=380,y=110)

app.mainloop()




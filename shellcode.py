#things we will be doing for purpose
#Todays motive--1) Data analytics
            #   2) MAchine learning - (4-5) days to be cleared
#GUI Development using Tkinter
#we will make a software
#creating alias nickname ab ise ase hi bulayenge
#GUI
    #-Application
    #-components/widgets
            #-geometry managaement
            #-behaviour


import tkinter as tk

app = tk.Tk()  #creation of application#object -- no variable in python --everything is object , classes,methods 
app.title('Basic Arithmetic')
app.geometry('280x150')
#widget creation
#pack is geometry management
##tk.Label(app, text = "Hello").pack()
##tk.Label(app, text = "bye").pack()
##tk.Label(app, text = "Hi").pack()
##
##tk.Label(app, text = "Hello").grid(row = 0,column = 0)
##tk.Label(app, text = "bye").grid(row = 1, column = 1)
##tk.Label(app, text = "Hi").grid(row = 2, column = 1)

##tk.Label(app, text = "Hello").place(x = 100, y = 20)
##tk.Label(app, text = "bye").pack(x = 130 , y = 80)
##tk.Label(app, text = "Hi").pack(x = 200, y = 120)

result = tk.Variable(app) #variable is ktinter variable
result.set('Result')
tk.Label(app,textvariable = result).place(x = 120, y = 120)
#input box to enter values
#for first value

first_val = tk.Variable(app)
second_val = tk.Variable(app)
tk.Entry(app, textvariable = first_val, width = 10).place(x = 50, y = 20)
tk.Entry(app, textvariable = second_val, width = 10).place(x = 160, y = 20)

def operate(e):
    first = first_val.get()
    second = second_val.get()
    exp = first +e+second
    result.set(eval(exp))
##    print(exp)
##tk.Button(app, text = '+',command = operate).place(x =50,y=70)
##
tk.Button(app, text = '+',width =2,command =lambda :operate('+')).place(x =50,y=70)
tk.Button(app, text = '-',width =2,command =lambda :operate('-')).place(x =90,y=70)
tk.Button(app, text = 'x',width =2,command =lambda :operate('*')).place(x =160,y=70)
tk.Button(app, text = '/',width =2,command =lambda :operate('/')).place(x =210,y=70)

#command will call the operate function but it asks definition not the call , we need to define the function on that place only

#it's function overloading passing fucntion inside function 

#last step below
app.mainloop()  #asynchronous application - threading --multiple operations at a time

    

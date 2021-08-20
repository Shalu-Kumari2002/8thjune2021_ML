##def xyz(x):
##    print(x)
##xyz(8)
####xyz(9,0)

##
##def abc(*a):
##    print(a)
##
##abc(4,7,9,10)
##
##d  = [4,46,78]
##abc(d)
##
##e = 'good'
##abc(e,d)
##abc(e,d,80,90,45,4.6,79)
##
###vriable keyword arguements
##def pqr(a,b):
##    print(a,b)
##
##pqr(b = 30,a = 'hi',c = 40,d = 40)

##def pqrs(**a):
##    print(a)
##pqrs(a = 30, b = 40, age = 19, name = 'rahul')
####pqrs()
######abc(*d)
##
##def every_type(a,b,d=10,e=1,*f,**g):
##    print(a,b,d,e,f,g)
##abc(*e)

##def ekor(*a = (4,5)):
##    print(a)
##ekor()


# Lambda Expressions (anonymous functions)
#- one liner
#- Always return a value
#- we can have input args
#- we can use ternary conditions or nested ones
#it is a wayof writing functions on a single line
#function name is not compulsory

##p = every_type

# lambda input_arg: output_arg
##
##
##def doubler(n):
##    return n*2
##
##doubler2 = lambda n : n*2

#for the hypothetical situation we can use function overloading which is actually passing function as arguemnent

#we can pass function definition by using lambda , that is function overloading

##def operate(f,n): #here we are considering f as function , n as list 
##    c = []
##    for i in n:
##        c.append(f(i))
##    return c

##a = [3,4,5,6,7,8,9,900]
##
##g = operate(lambda x:x*2,a)
##print(g)
##
##g1 = operate(lambda x:x if x%2 else x//2,a)
##print(g1)
##
##def something(k):
##    return k+10
##
##g2 = operate(something,a)
##print(g2)

#map and #filter
#GENERATOR
a = [3,4,5,6,7,8,9,900]
m = list(map(lambda x:x**2,a))
print(m)
        
f = list(filter(lambda x:x%2 ==1, a))
print(f)
#map code is 
##def operate(f,n): #here we are considering f as function , n as list 
##    c = []
##    for i in n:
##        c.append(f(i))
##    return c
##
##def my_gen(n):
##    c =[]
##    for i in range(1,11):
##        c.append(n*i)
##    return c
def my_gen(n):
    for i in range(1,11):
        yield n*i
        




    

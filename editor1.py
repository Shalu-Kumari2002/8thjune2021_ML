####with open('data.txt','r') as file:
####    content = file.readlines()
####    file.close
######
######print(content)
##### file = open('data.txt','r')it makes it available every
####
####with open('data.txt','r') as file:
####    content = file.read()
####    file.close
####
#####print(content)
####c_list = content.split('\n')
#####print(c_list)
####heading = c_list[0].split(',') ; print(heading)
####rows =[i.split(',') for i in c_list[1:]]; print(rows)
####al_data = list(zip(*rows))
####data = dict(zip(heading,zip(*rows)))
#####print(data)
#####to deal with json files , we need to bring that resources
####import keyword
####keyword.kwlist
####
#####fp- file pointer
####import json
####with open('my_json_data.json','w') as file:
####    json.dump(data,file)
####print('saved')
###def-fucntion _ function name
##def gen_dict():
##    print('hi')
##
##def xyz(a):
##    print(a)
##xyz(89)
##gen_dict()
##xyz(a=79)
##xyz(a="hello")
##
##def abc(a,b):
##    print(a+b,a/b)
##abc(8,9)
##def pqr(a=0,b=0):
##    print(a+b)
##pqr(0,8)
##def new(n=2,k=0
):
##    return (n**4)+k
##m = new(6,2)

def gen_dict(filename = ''):
    with open(filename,'r') as file:
        content = file.read()
        file.close()
    c_list = content.split('\n')
    heading = c_list[0].split(',')
    rows = [i.split(',') for i in c_list[1:]]
    return dict(zip(heading, zip(*rows)))

d1 = gen_dict('data.txt')
d2 = gen_dict('new_data.txt')
print(d1)
print(d2) 
    



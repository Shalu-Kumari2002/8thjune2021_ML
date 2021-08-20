##a =['name','age']
##b = ['Rahul',[23,90]]
###range(2) - 0,1
##d = {a[i]:b[i] for i in range(2)}
##print(d)
##e = {a[i]:b[i] if i%2 else 0 for i in range(2)}
##print(e)
##
##
a = [3,4,5,6,7,90]
##for i in a:
##    print(i,i[i])
##for i in enumerate(a):
##    print(i)

##for a,b in enumerate(a):
##    print(b,'is located at',a,'index')

##a = ['name','age']
##b = [['Rahul','vijay','vishesh'],[23,24,35]]
##c = {v:b[i] for i,v in enumerate(a)}
##print(c)
#file = open('data.txt','r')
#all data in txt file is shifted or copied to file

##with open('data_file.txt','r') as file: #it is a suite only this much scope
##    content = file.readlines()
##    file.close()
##print(content)

with open('data_file.txt','r') as file: #it is a suite only this much scope
    content = file.read()
    file.close()
print(content)
c_list = content.split('\n')
#print(c_list)
heading = c_list[0].split(',')
#print(heading)
rows =[i.split(',') for i in c_list[1:]]
#print(rows)
##d = {value:rows[0:len(rows):1][i] for i,value in enumerate(heading)}
##print(d)

print(heading)
print(rows)
data =  [[j[i] for j in rows] for i,v in enumerate(heading)]

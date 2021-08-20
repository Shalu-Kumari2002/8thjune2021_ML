Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
['name, age , subject \n', 'shalu, 19,python_ML\n', 'vineet,20, python\n', 'shrijana, 21, java\n']
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
name, age , subject 
shalu, 19,python_ML
vineet,20, python
shrijana, 21, java

>>> type(content)
<class 'str'>
>>> #read - makes string
>>> #readlines - makes list
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 

>>> 
>>> 

>>> 
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
name, age , subject 
shalu, 19,python_ML
vineet,20, python
shrijana, 21, java

['name, age , subject ', 'shalu, 19,python_ML', 'vineet,20, python', 'shrijana, 21, java', '']
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
name, age , subject 
shalu, 19,python_ML
vineet,20, python
shrijana, 21, java

['name, age , subject ', 'shalu, 19,python_ML', 'vineet,20, python', 'shrijana, 21, java', '']
Traceback (most recent call last):
  File "F:/15th_june_AI_batch/Day_4/editor1.py", line 15, in <module>
    heading = c-list[0].split(',') ; print(heading)
NameError: name 'c' is not defined
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
name, age , subject 
shalu, 19,python_ML
vineet,20, python
shrijana, 21, java

['name, age , subject ', 'shalu, 19,python_ML', 'vineet,20, python', 'shrijana, 21, java', '']
['name', ' age ', ' subject ']
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
name, age , subject 
shalu, 19,python_ML
vineet,20, python
shrijana, 21, java

['name, age , subject ', 'shalu, 19,python_ML', 'vineet,20, python', 'shrijana, 21, java', '']
['name', ' age ', ' subject ']
[['shalu', ' 19', 'python_ML'], ['vineet', '20', ' python'], ['shrijana', ' 21', ' java'], ['']]
>>> len(rows)
4
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
name, age , subject 
shalu, 19,python_ML
vineet,20, python
shrijana, 21, java
['name, age , subject ', 'shalu, 19,python_ML', 'vineet,20, python', 'shrijana, 21, java']
['name', ' age ', ' subject ']
[['shalu', ' 19', 'python_ML'], ['vineet', '20', ' python'], ['shrijana', ' 21', ' java']]
>>> names = [[row[i] for row in rows] for i,v in enumerate(heading)]
>>> names
[['shalu', 'vineet', 'shrijana'], [' 19', '20', ' 21'], ['python_ML', ' python', ' java']]
>>> #instead of using enumerate
>>> #we can use zip
>>> all_data = list(zip(*rows))
>>> all_data
[('shalu', 'vineet', 'shrijana'), (' 19', '20', ' 21'), ('python_ML', ' python', ' java')]
>>> #zip actually helps us in doing lots of operations in short cut -- it attaches data parallely
>>> #we should learn the way  we want but it should not result in vain, thats ultimate
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
name, age , subject 
shalu, 19,python_ML
vineet,20, python
shrijana, 21, java
['name, age , subject ', 'shalu, 19,python_ML', 'vineet,20, python', 'shrijana, 21, java']
['name', ' age ', ' subject ']
[['shalu', ' 19', 'python_ML'], ['vineet', '20', ' python'], ['shrijana', ' 21', ' java']]
>>> #i already have heading and data , i will attach it parallely ,before we used asterick because we wanted two levels that is list inside list
>>> list(zip(heading,all_data))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list(zip(heading,all_data))
NameError: name 'all_data' is not defined
>>> list(zip(heading,al_data))
[('name', ('shalu', 'vineet', 'shrijana')), (' age ', (' 19', '20', ' 21')), (' subject ', ('python_ML', ' python', ' java'))]
>>> list(zip(heading,*al_data))
[('name', 'shalu', ' 19', 'python_ML'), (' age ', 'vineet', '20', ' python'), (' subject ', 'shrijana', ' 21', ' java')]
>>> list(zip(heading,al_data))
[('name', ('shalu', 'vineet', 'shrijana')), (' age ', (' 19', '20', ' 21')), (' subject ', ('python_ML', ' python', ' java'))]
>>> list(zip(*heading))
[('n', ' ', ' '), ('a', 'a', 's'), ('m', 'g', 'u'), ('e', 'e', 'b')]
>>> list(zip(*heading,*al_data))
[('n', ' ', ' ', 'shalu', ' 19', 'python_ML'), ('a', 'a', 's', 'vineet', '20', ' python'), ('m', 'g', 'u', 'shrijana', ' 21', ' java')]
>>> dict(zip(heading,zip(*rows)))
{'name': ('shalu', 'vineet', 'shrijana'), ' age ': (' 19', '20', ' 21'), ' subject ': ('python_ML', ' python', ' java')}
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
name, age , subject 
shalu, 19,python_ML
vineet,20, python
shrijana, 21, java
['name, age , subject ', 'shalu, 19,python_ML', 'vineet,20, python', 'shrijana, 21, java']
['name', ' age ', ' subject ']
[['shalu', ' 19', 'python_ML'], ['vineet', '20', ' python'], ['shrijana', ' 21', ' java']]
{'name': ('shalu', 'vineet', 'shrijana'), ' age ': (' 19', '20', ' 21'), ' subject ': ('python_ML', ' python', ' java')}
>>> #* --- variable arguement s
>>> #json - javascript object navigation --internet files
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
name, age , subject 
shalu, 19,python_ML
vineet,20, python
shrijana, 21, java
['name, age , subject ', 'shalu, 19,python_ML', 'vineet,20, python', 'shrijana, 21, java']
['name', ' age ', ' subject ']
[['shalu', ' 19', 'python_ML'], ['vineet', '20', ' python'], ['shrijana', ' 21', ' java']]
{'name': ('shalu', 'vineet', 'shrijana'), ' age ': (' 19', '20', ' 21'), ' subject ': ('python_ML', ' python', ' java')}
>>> import json
>>> #dump-to save --
>>> # str to be saved in json then dumps if dict then dump
>>> #loads- for string , load for dict
>>> data
{'name': ('shalu', 'vineet', 'shrijana'), ' age ': (' 19', '20', ' 21'), ' subject ': ('python_ML', ' python', ' java')}
>>> with open('my_data.json','w') as file:
	json.dump(data,file)

	
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> #keyword is already a made library
>>> #import meaning we are bringing library
>>> import json
>>> with open('mydata.json','w') as file:
	json.dump(data,file)

	
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
name, age , subject 
shalu, 19,python_ML
vineet,20, python
shrijana, 21, java
ajay,99,kilo
jiya , 100, jigna 

['name, age , subject ', 'shalu, 19,python_ML', 'vineet,20, python', 'shrijana, 21, java', 'ajay,99,kilo', 'jiya , 100, jigna ', '']
['name', ' age ', ' subject ']
[['shalu', ' 19', 'python_ML'], ['vineet', '20', ' python'], ['shrijana', ' 21', ' java'], ['ajay', '99', 'kilo'], ['jiya ', ' 100', ' jigna '], ['']]
{'name': ('shalu', 'vineet', 'shrijana', 'ajay', 'jiya ', '')}
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
['name', ' age ', ' subject ']
[['shalu', ' 19', 'python_ML'], ['vineet', '20', ' python'], ['shrijana', ' 21', ' java'], ['ajay', '99', 'kilo'], ['jiya ', ' 100', ' jigna '], ['']]
saved
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
['name', ' age ', ' subject ']
[['shalu', ' 19', 'python_ML'], ['vineet', '20', ' python'], ['shrijana', ' 21', ' java'], ['ajay', '99', 'kilo'], ['jiya ', ' 100', ' jigna ']]
saved
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
Traceback (most recent call last):
  File "F:/15th_june_AI_batch/Day_4/editor1.py", line 33, in <module>
    gen_dict()
NameError: name 'gen_dict' is not defined
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
hi
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
hi
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
89
hi
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
89
hi
79
hello
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
89
hi
79
hello
17 0.8888888888888888
>>> abc(8)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    abc(8)
TypeError: abc() missing 1 required positional argument: 'b'
>>> abc(9,)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    abc(9,)
TypeError: abc() missing 1 required positional argument: 'b'
>>> abc(b=2,a=9)
11 4.5
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
89
hi
79
hello
17 0.8888888888888888
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
89
hi
79
hello
17 0.8888888888888888
8
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
89
hi
79
hello
17 0.8888888888888888
8
>>> print(m)
1298
>>> p = pqr(4,5)
9
>>> print(p)
None
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
Traceback (most recent call last):
  File "F:/15th_june_AI_batch/Day_4/editor1.py", line 59, in <module>
    d1 = gen_dict('data.txt')
  File "F:/15th_june_AI_batch/Day_4/editor1.py", line 52, in gen_dict
    content = file.rea()
AttributeError: '_io.TextIOWrapper' object has no attribute 'rea'
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
Traceback (most recent call last):
  File "F:/15th_june_AI_batch/Day_4/editor1.py", line 59, in <module>
    d1 = gen_dict('data.txt')
  File "F:/15th_june_AI_batch/Day_4/editor1.py", line 52, in gen_dict
    content = file.rea()
AttributeError: '_io.TextIOWrapper' object has no attribute 'rea'
>>> 
== RESTART: F:/15th_june_AI_batch/Day_4/editor1.py ==
{'name': ('shalu', 'vineet', 'shrijana', 'ajay', 'jiya '), ' age ': (' 19', '20', ' 21', '99', ' 100'), ' subject ': ('python_ML', ' python', ' java', 'kilo', ' jigna ')}
{'name': ('shalu', 'paramartha'), 'age': ('20', '22'), 'subject': ('python', 'python')}
>>> 
Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = input('Enter the value:')
Enter the value:45v
>>> a = input('enter the values')
enter the values45
>>> a
'45'
>>> a = int(a)
>>> a
45
>>> type(a)
<class 'int'>
>>> # whatever you keep as input it is actually converted ito string only , so typecast it
>>> a1 = float(input('enter the values'))
enter the values 89
>>> type(a1);a1;
<class 'float'>
89.0
>>> #we don't know what will come so we use eval
>>> a = eval(input('enter the input value'))
enter the input value 8
>>> a
8
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
enter the first value
Traceback (most recent call last):
  File "F:\15th_june_AI_batch\day_3\editor_1.py", line 1, in <module>
    a = eval(input('enter the first value'))
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> 9
9
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
enter the first value9
9 :is an odd numer
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
enter the first value8
8 is even number
>>> # 1. if -elif-else
>>> # syntax
>>> # if cond:
>>> #    if cond:
>>> #      ----
>>> #elif cond:
>>> #elif cond:
>>> #else:
>>> # 2. looping statement
>>> #while cond:
>>> #   ------
>>> # -----
>>> #3. For --for number of values
>>> #for obj in collection:
>>> # ______
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
enter the first value 4
enter the 2nd value 3
enter the 3rd value2
Traceback (most recent call last):
  File "F:\15th_june_AI_batch\day_3\editor_1.py", line 11, in <module>
    print(a,'is the bigger than'+b)
TypeError: can only concatenate str (not "int") to str
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
enter the first value5
enter the 2nd value4
enter the 3rd value3
5 is the bigger than 4
5 is the greatest
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
enter the first value8
enter the 2nd value90
enter the 3rd value99
90 is the bigger than 8
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
enter the first value2
enter the 2nd value1
enter the 3rd value1
nice
>>> 
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
enter the first value4
enter the 2nd value3
enter the 3rd value4
good
good
good
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
enter the first value3
enter the 2nd value3
enter the 3rd value3
good 3
good 3
good 3
>>> k = [8,7,5,12,24,45]
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
enter the first value2
enter the 2nd value2
enter the 3rd value2
9 is an odd number
89 is an odd number
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
9 is an odd number
89 is an odd number
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
8 is an even number
0 is an even number
890 is an even number
678 is an even number
90 is an even number
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
[9, 89] [8, 0, 890, 678, 90]
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
[9, 89] [4.0, 0.0, 445.0, 339.0, 45.0]
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
[9, 89] [4, 0, 445, 339, 45]
>>> 
KeyboardInterrupt
>>> k = [8,9,0,89,890,678,90]
m = []
n =[]
for i in k:
    if i%2 == True:
        m.append(i)
    else:
        n.append(i//2)
print(m,n)
SyntaxError: multiple statements found while compiling a single statement
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
Traceback (most recent call last):
  File "F:\15th_june_AI_batch\day_3\editor_1.py", line 34, in <module>
    a = eval(int('enter'))
ValueError: invalid literal for int() with base 10: 'enter'
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
Traceback (most recent call last):
  File "F:\15th_june_AI_batch\day_3\editor_1.py", line 34, in <module>
    a = eval(int('enter'))
ValueError: invalid literal for int() with base 10: 'enter'
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
enter1
0
1
2
3
4
5
6
7
8
9
10
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
enter4
0
4
8
12
16
20
24
28
32
36
40
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
enter3
3
9
15
21
27
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
enter3
3
9
15
21
27
********************
>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
enter8
8
24
40
56
72
8 / 

>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
enter9
9
27
45
63
81
9 8 

>>> 
=============== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===============
enter2
2
6
10
14
18
2 8 

20
18
16
14
12
10
8
6
4
2
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(3,10))
[3, 4, 5, 6, 7, 8, 9]
>>> list(range(s))
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    list(range(s))
NameError: name 's' is not defined
>>> s = 10
>>> list(range(s))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
=== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===

shalu
shalushalu
shalushalushalu
shalushalushalushalu
>>> 
=== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===

shalu
shalushalu
shalushalushalu
shalushalushalushalu

shalu
shalushalu
shalushalushalu
shalushalushalushalu
shalushalushalushalushalu
shalushalushalushalushalushalu
shalushalushalushalushalushalushalu
shalushalushalushalushalushalushalushalu
shalushalushalushalushalushalushalushalushalu
>>> 
=== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===

shalu
shalushalu
shalushalushalu
shalushalushalushalu

*
**
***
****
******
*******
*********
>>> #it comes out of for loop , break is only for loop
>>> #pass is kind of majburi by sir ; why is it so .
>>> #i have some statement which is compulsory
>>> 
=== RESTART: F:\15th_june_AI_batch\day_3\editor_1.py ===

shalu
shalushalu
shalushalushalu
shalushalushalushalu

*
**
***
****
******
*******
*********
print(a)
break

#what ha

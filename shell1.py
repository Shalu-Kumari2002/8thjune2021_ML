Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: F:/15th_june_AI_batch/Day_5/editor.py ========
8
Traceback (most recent call last):
  File "F:/15th_june_AI_batch/Day_5/editor.py", line 4, in <module>
    xyz(9,0)
TypeError: xyz() takes 1 positional argument but 2 were given
>>> 
========= RESTART: F:/15th_june_AI_batch/Day_5/editor.py ========
(4, 7, 9, 10)
([4, 46, 78],)
('good', [4, 46, 78])
('good', [4, 46, 78], 80, 90, 45, 4.6, 79)
>>> 
========= RESTART: F:/15th_june_AI_batch/Day_5/editor.py ========
(4, 7, 9, 10)
([4, 46, 78],)
('good', [4, 46, 78])
('good', [4, 46, 78], 80, 90, 45, 4.6, 79)
(4, 46, 78)
('g', 'o', 'o', 'd')
>>> #in tuple two values are must
>>> l = (90)
>>> l
90
>>> l = (90,)
>>> l
(90,)
>>> d = (9,0)
>>> abc(d)
((9, 0),)
>>> abc(*d)
(9, 0)
>>> type(l)
<class 'tuple'>
>>> 
========= RESTART: F:/15th_june_AI_batch/Day_5/editor.py ========
Traceback (most recent call last):
  File "F:/15th_june_AI_batch/Day_5/editor.py", line 23, in <module>
    pqr(b = 30,a = 'hi',c = 40,d = 40)
TypeError: pqr() got an unexpected keyword argument 'c'
>>> 
========= RESTART: F:/15th_june_AI_batch/Day_5/editor.py ========
{'a': 30, 'b': 40, 'age': 19, 'name': 'rahul'}
>>> 
========= RESTART: F:/15th_june_AI_batch/Day_5/editor.py ========
{'a': 30, 'b': 40, 'age': 19, 'name': 'rahul'}
>>> p = every_type
>>> p
<function every_type at 0x00000298FCFE9438>
>>> p(6,7)
6 7 10 1 () {}
>>> const p = every_type
SyntaxError: invalid syntax
>>> 
========= RESTART: F:/15th_june_AI_batch/Day_5/editor.py ========
>>> doubler(40)
80
>>> d = doubler
>>> d
<function doubler at 0x000002180DDB4288>
>>> d(9)
18
>>> 
========= RESTART: F:/15th_june_AI_batch/Day_5/editor.py ========
>>> d = doubler2(40)
>>> d
80
>>> e = d(90)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    e = d(90)
TypeError: 'int' object is not callable
>>> a = doubler2
>>> a(90)
180
>>> 
========= RESTART: F:/15th_june_AI_batch/Day_5/editor.py ========
[6, 8, 10, 12, 14, 16, 18, 1800]
>>> 
========= RESTART: F:/15th_june_AI_batch/Day_5/editor.py ========
[6, 8, 10, 12, 14, 16, 18, 1800]
[3, 2, 5, 3, 7, 4, 9, 450]
>>> 
========= RESTART: F:/15th_june_AI_batch/Day_5/editor.py ========
[6, 8, 10, 12, 14, 16, 18, 1800]
[3, 2, 5, 3, 7, 4, 9, 450]
[13, 14, 15, 16, 17, 18, 19, 910]
>>> 
========= RESTART: F:/15th_june_AI_batch/Day_5/editor.py ========
[9, 16, 25, 36, 49, 64, 81, 810000]
>>> 
========= RESTART: F:/15th_june_AI_batch/Day_5/editor.py ========
[9, 16, 25, 36, 49, 64, 81, 810000]
Traceback (most recent call last):
  File "F:/15th_june_AI_batch/Day_5/editor.py", line 88, in <module>
    f = list(filer(lambda x:x%2 ==1, a))
NameError: name 'filer' is not defined
>>> 
========= RESTART: F:/15th_june_AI_batch/Day_5/editor.py ========
[9, 16, 25, 36, 49, 64, 81, 810000]
[3, 5, 7, 9]
>>> m = map(lambda x:x**2,a)
>>> m
<map object at 0x00000215E156E748>
>>> #speciality of map object
>>> mist(m)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    mist(m)
NameError: name 'mist' is not defined
>>> list(m)
[9, 16, 25, 36, 49, 64, 81, 810000]
>>> list(m)
[]
>>> m
<map object at 0x00000215E156E748>
>>> m = map(lambda x:x**2,a)
>>> next(m)
9
>>> next(m)
16
>>> next(m)
25
>>> next(m)
36
>>> next(m)
49
>>> next(m)
64
>>> next(m)
81
>>> next(m)
810000
>>> next(m)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    next(m)
StopIteration
>>> list(m)
[]
>>> m = map(lambda x:x**2,a)
>>> next(m)
9
>>> list(m)
[16, 25, 36, 49, 64, 81, 810000]
>>> next(m)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    next(m)
StopIteration
>>> m = map(lambda x:x**2,a)
>>> for i in m:
	print(i)

	
9
16
25
36
49
64
81
810000
>>> list(m)
[]
>>> next(m)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    next(m)
StopIteration
>>> #conclusion
>>> # happening because of generator
>>> #generator
>>> b = [3,4,5,6]
>>> for i in range(len(b))
SyntaxError: invalid syntax
>>> for i in range(len(b)):
	print(b[i])

	
3
4
5
6
>>> for i in b:
	print(i)

	
3
4
5
6
>>> #using range-- it actually takes too much time
>>> #generator - if i want to use only once
>>> 
========= RESTART: F:/15th_june_AI_batch/Day_5/editor.py ========
[9, 16, 25, 36, 49, 64, 81, 810000]
[3, 5, 7, 9]
>>> my_gen(2)
<generator object my_gen at 0x0000025478088F48>
>>> 
========= RESTART: F:/15th_june_AI_batch/Day_5/editor.py ========
[9, 16, 25, 36, 49, 64, 81, 810000]
[3, 5, 7, 9]
>>> my_gen(2)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> 
========= RESTART: F:/15th_june_AI_batch/Day_5/editor.py ========
[9, 16, 25, 36, 49, 64, 81, 810000]
[3, 5, 7, 9]
>>> my_gen(3)
<generator object my_gen at 0x000001DC4BF58F48>
>>> g = my_gen(2)
>>> for i in g:
	print(i)

	
2
4
6
8
10
12
14
16
18
20
>>> #decorator is used for assigning function behavior to some another function. 
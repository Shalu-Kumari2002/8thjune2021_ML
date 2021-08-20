Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #python_day_3_class_practice
>>> print([4,5,6],{'di',"haary"},end = "9")
[4, 5, 6] {'haary', 'di'}9
>>> print([4,5,6],{'di',"haary"},sep = "**",end = "9")
[4, 5, 6]**{'haary', 'di'}9
>>> #coding is something like we can be best only if it continues __i mean the practice
>>> #coding is something like we can be best only if it continues __i mean the practice
>>> #error handling we will do afterwards
>>> #Magical thing in python , called comprehension
>>> #COMPREHENSION
>>> ##1.This is to create collections
>>> ##2.They use for-loop
>>> ##3.Alway written in one line --It's a one liner
>>> ##4.if-statement can be used
>>> ##5.nesting is possible
>>> ##6.We can use ternary conditional statement
>>> #ternary conditional statement
>>> print('its odd') if eval(input('enter the number'))%2 else print('its even')
enter the number9
its odd
>>> #here it starts from between and then true will make it to see the left side and else on the right side.
>>> print('its odd') if eval(input('enter: ')//2 == 1 else print('its even')
			 
SyntaxError: invalid syntax
>>> print('its odd') if (eval(input('enter: ')//2 == 1)== True else print('its even')
		     
SyntaxError: invalid syntax
>>> ##List comprehension
>>> ## it will generate list
>>> #syntax of list comprehension --
>>> ##[ o/p for loop
>>> 
========== RESTART: F:/15th_june_AI_batch/day_3/editor3.py =========
[8, 10, 14, 16, 184, 6]
>>> 
========== RESTART: F:/15th_june_AI_batch/day_3/editor3.py =========
[8, 10, 14, 16, 184, 6]
[5, 7, 3]
>>> 
========== RESTART: F:/15th_june_AI_batch/day_3/editor3.py =========
[8, 10, 14, 16, 184, 6]
[5, 7, 3]
[4, 8, 92]
>>> 
========== RESTART: F:/15th_june_AI_batch/day_3/editor3.py =========
[8, 10, 14, 16, 184, 6]
[5, 7, 3]
[4, 8, 92]
Traceback (most recent call last):
  File "F:/15th_june_AI_batch/day_3/editor3.py", line 13, in <module>
    values - [i if i%2 else i//2 for i in a ]
NameError: name 'values' is not defined
>>> 
========== RESTART: F:/15th_june_AI_batch/day_3/editor3.py =========
[8, 10, 14, 16, 184, 6]
[5, 7, 3]
[4, 8, 92]
Traceback (most recent call last):
  File "F:/15th_june_AI_batch/day_3/editor3.py", line 13, in <module>
    values - [i if i%2 else i//2 for i in a]
NameError: name 'values' is not defined
>>> 
========== RESTART: F:/15th_june_AI_batch/day_3/editor3.py =========
[8, 10, 14, 16, 184, 6]
[5, 7, 3]
[4, 8, 92]
>>> 
========== RESTART: F:/15th_june_AI_batch/day_3/editor3.py =========
[8, 10, 14, 16, 184, 6]
[5, 7, 3]
[4, 8, 92]
[2, 5, 7, 4, 46, 3]
>>> 
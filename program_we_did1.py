Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #slicing
>>> a = [0,1,2,3,4,5,67,7,8,990]
>>> a[0]
0
>>> a[2]
2
>>> a[-len(a)]
0
>>> a[len(a)]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a[len(a)]
IndexError: list index out of range
>>> a[len(a)-1]
990
>>> a[-(1-len(a)]
  
SyntaxError: invalid syntax
>>>  a[-(2-len(a)]
   
SyntaxError: unexpected indent
>>> a[-(1-len(a)]
  
SyntaxError: invalid syntax
>>> a[len(a)-1]
990
>>> ##Slicing - insid square bracket multiple values
>>> #[start:end:gap]
>>> #Slicing :- i want to cut a portion of the collection
>>> a = 'hi it is a python string'
>>> a[0:8:1]
'hi it is'
>>> a[0:8:1];a[0:8:2];a[0:8:3];a[0:8:4];a[0:8:5]
'hi it is'
'h ti'
'hii'
'ht'
'h '
>>> index(a.center)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    index(a.center)
NameError: name 'index' is not defined
>>> index(a.centre(a)]
SyntaxError: invalid syntax
>>> a[-1:-7:1]
''
>>> a[-1]
'g'
>>> a[-1:-7]
''
>>> a = 'Shalu soni rinita'
>>> a[-1:-7:1]
''
>>> type(a)
<class 'str'>
>>> a[-1];a[-2];
'a'
't'
>>> a[-1:-4:]
''
>>> a[-7:-1:1]
' rinit'
>>> a[-6:-1:1]
'rinit'
>>> a[-6:0:]
''
>>> a[-9:]
'ni rinita'
>>> a[-7:]
' rinita'
>>> a[-6:]
'rinita'
>>> # we use to have default values as well
>>> #by default values are 1 most of the time
>>> #default [0{if gave is +ve): last (gap +ve):1 (default)]
>>> a[0:len(a):]
'Shalu soni rinita'
>>> a[:8]
'Shalu so'
>>> a[:len(a)]
'Shalu soni rinita'
>>> a[-8:]
'i rinita'
>>> a[-9:]
'ni rinita'
>>> a[:-9]
'Shalu so'
>>> a[1:9:-1]
''
>>> 
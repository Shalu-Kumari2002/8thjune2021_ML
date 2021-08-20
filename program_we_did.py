Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: F:/15th_june_AI_batch/day_2/sample2.py ===============
0
>>> 
================ RESTART: F:/15th_june_AI_batch/day_2/sample2.py ===============
0
2100
>>> print(9+9)
18
>>> #this is how we use it we can simply use it , either though editor or direc#
>>> #here
>>> #Rules for identifiers
>>> #alphabet, numeric digits,_(underscore)
>>> #first letter can never be numeric
>>> a1 = 10
>>> 1a = 19
SyntaxError: invalid syntax
>>> #keywords cannot be used -these are special reserved words which can't be used as variables , only used for specail works ,actually
>>> #how to find that out
>>> import keybword
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    import keybword
ModuleNotFoundError: No module named 'keybword'
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> #all will be used
>>> # -# it is used for commenting (for making our personal notes it's called has
>>> #theere is no multiline comment kind of thing
>>> a = b = 10
>>> a
10
>>> b
10
>>> #way_throuugh_which_we_can_make_thins
>>> a,b = 11,34
>>> a
11
>>> b
34
>>> #what are the data types - obviously the types of data
>>> #we can use semicolon as well
>>> c = 34.4
>>> d = 30; e = 5
>>> d
30
>>> e
5
>>> #now let's move on
>>> #RULES OF BRACKETS
>>> 	#WHAT KIND OF NETWORK ISSUES
>>> # () - functions(use), either in calling or using as an ex--print(_
>>> # 	 - Mathematical expressions -(7*7)**9
>>> #	 - Tuple
>>> # {} - in python we use it -2 places - for ---Dictionary, set
>>> # [] - indexing/slicing, list creation
>>> # <> - N/A
>>> # OPERATORS
>>> # VARIABLE ----- CONTAINER WHICH CN STORES VALUES, OPERATIONS CAN BE PERFORMED USING THIS .
>>> # 1. Arithmetic : +,-,*,/,**(power),//(floor division - 7/4 = 1.75,output = 1)
>>> 7/4
1.75
>>> 7//4
1
>>> 4**3
64
>>> 4*4
16
>>> 13%3
1
>>> # %-- gives remainder
>>> # 2. Assignment: =,+=, -=, /=, *=, **=, //=, %=
>>> a = 10
>>> a += 3
>>> a
13
>>> # performs operations on the existing value and assigns to it again
>>> a -= 8
>>> a
5
>>> a *= 5;a
25
>>> #3. Relational: >,<, == , !=,>=, <=
>>> a == 10#(is a = 10 or not)
False
>>>  a != 10
 
SyntaxError: unexpected indent
>>> a != 10
True
>>> a > 15
True
>>> a >=25
True
>>> #4. Logical: and , or , not
>>> # they are like simple logic gates
>>> (7>4) and (8>a)
False
>>> (7>4) or (a>8)
True
>>> (7>4) or (8>a)
True
>>> not a
False
>>> not(a or b)
False
>>> a = 0
>>> not a
True
>>> (7>4) or (8>a) and (8<7)
True
>>> not False
True
>>> a = 10; b = 8;
>>> if a>b:
	print(a +' is the greatest')
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> #5. Bitwise: &, |, ^,~,>> , << ( it works for binary ones - for bitwise operators) for this m-percent and all this are use for boolean ones )
>>> a = 1010;
>>> a >> 1
505
>>> a = 2
>>> a <<2
8
>>> a >> 2
0
>>> 2&3
2
>>> 2|3
3
>>> 2^3
1
>>> 6|9
15
>>> 6^9
15
>>> # 2 = 0010 , 3 = 0011, 2 | 3 = 0010+ 0011 ,|= or , ^ = exor, & = and --(remember on the binary values of data
>>> #logicl works on boolean data
>>> 2 >> 1
1
>>> 2 << 1
4
>>> 2 >> 2
0
>>> 2 << 3
16
>>>  #32 >>3 = 32 / 2**3
>>> 32>>3
4
>>> 32 / (2**3)
4.0
>>> # 32 << 3 = 32 * ( 2**3)
>>> 32 << 3
256
>>> 32 *(2**3)
256
>>> ~1
-2
>>> ~4
-5
>>> # whar it does (~) is it see the position of th provided value and keeps - by adding one
>>> # 6. membership: in, not in ( kya ye kisi particular collection ka member hai kya
>>>  "hi" in " mitashi"
 
SyntaxError: unexpected indent
>>> 'hi' in 'mitashi'
True
>>> 'z' in 'shalu'
False
>>> 'z' in 'shallow'
False
>>> 's' not in 'shalu'
False
>>> 'brain' in 'heart'
False
>>> #7. Identity: is , is not
>>> # what is identity
>>> a = 10 ;b = 20; c = 29
>>> id(a)
140709999637040
>>> id(b)
140709999637360
>>> id(c)
140709999637648
>>> a = b = 8
>>> id(a);id(b)
140709999636976
140709999636976
>>> a is b
True
>>> a id c
SyntaxError: invalid syntax
>>> a is c
False
>>> # we usully don't check this
>>> 
>>> ## DATA TYPES:
>>> #	1.Nuemeric ( int , float, complex) - complex -3 -4i
>>> a = 2
>>> a = float(a)
>>> a
2.0
>>> #int = 34 , float = 34.0 , complex = 34 + 0j
>>> a = complex(a)
>>> a
(2+0j)
>>> a = 3+ 8j
>>> type(a)
<class 'complex'>
>>> n = 00
>>> type(n);
<class 'int'>
>>> #2. Datatype ----- String (str) -- 'hello', "hello" , (multiple lines '''hello'''
>>> #string NB:- Immutable
>>> #3. datatype ---- List (list) -- inside - []-- basically collection of heterogenuous items  - [4, 'hi', 45, [9,90]]
>>> #N.B. = mutable
>>> #4. Tuple(datatype) - collection of het. items (4,'hi' 4.5, [8])
>>> # (immutable)
>>> #5 . Dictionary (dict) structured collection { key1:vlaue1 , key2:value2 ...}
>>> # dict is also mutable
>>> #6. Set (set) - collection of unique items {5,6,[8,9]} mutable
>>> #7. Boolean (bool)- True , False
>>> #FUNDAMEMTAL DATATYPES -- USING THIS WE CAN MAKE DERIVED DATATYPES
>>> #LET'S COME TO MUTABLE AND IMMUTABLE
>>> # LET'S HAVE a question -- variable and constant - if values of variable are not changed then also it's constant acting then why to use constant ( const int  a = 10 ) --- 1) whenever we make variable we actually assign recources to it such as typecasting , and all ,
>>> #allocating some resources ,so does it take speed, so let's not
>>> #resources to a const. values, so does speed is not reduced.
>>> # it helps in speed up-- mutable is something which can be changed and immutables are those which we can't modify
>>> #Item assignment, item deletion -- happens in mutable and can't take place in immutable ones -- it must be clear ----- so be clear -- be enthusiastic
>>> # Operations of data types
>>> #String operations
>>> a = 'shalu kumari is a very good girl'
>>> b =' hi it is a python string'; print(a,b)
shalu kumari is a very good girl  hi it is a python string
>>> print(a+b)
shalu kumari is a very good girl hi it is a python string
>>> s1 = 'hi ti is\nsecond line '
>>> print(s1)
hi ti is
second line 
>>> s1 = ''' hey baby
i am the universe
i am the greatest '''
>>> s1
' hey baby\ni am the universe\ni am the greatest '
>>> print(s1)
 hey baby
i am the universe
i am the greatest 
>>> s1[0]
' '
>>> s1[0:len(s1):2]
' e ayia h nvreia h raet'
>>> s2 = 'jupiter is great still uranus as great rings which i want in my hands'
>>> s2[0][0]
'j'
>>> s3 = 'hi it\'s a new string'
>>> s3;print(s3)
"hi it's a new string"
hi it's a new string
>>> type(s1);type(s3);
<class 'str'>
<class 'str'>
>>> type(a)
<class 'str'>
>>> len(s1);len(b);len(a)
46
25
32
>>> ##indexing -- here we bring out the elements based on their index(position) starting from 0 ,
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    s[0]
NameError: name 's' is not defined
>>> s1[0]
' '
>>> s = [3,'baby','father',[45,'baba']]
>>> s[0]
3
>>> s[0][0]
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    s[0][0]
TypeError: 'int' object is not subscriptable
>>> s[3][0]
45
>>> s[3][0]+s[0]
48
>>> a = "let us start'
SyntaxError: EOL while scanning string literal
>>> a = 'let sus strt'
>>> s[-1]
[45, 'baba']
>>> #negative indexing starts from -1
>>> #slicing
>>> 
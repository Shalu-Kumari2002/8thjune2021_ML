#List comprehension
a = [4,5,7,8,92,3]
##b = []
##for i in a:
##    b.append(i*2)
b = [i*2 for i in a]
print(b)
odd = [ i for i in a if i%2]
print(odd)
even = [ i for i in a if i%2 == False]
print(even)
#notice output is in extreme left only
values = [i if i%2 else i//2 for i in a]
print(values)
# we can keep only one statement at the right side , but on the left we have to keep as many as we want


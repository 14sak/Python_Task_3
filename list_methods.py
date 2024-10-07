# List Methods

#1.append():adds an element at the end of the list
print()
print('--1.append()--')
a=['Aa','Bb','Cc','Dd','Ee']
print(a)
print('---')
a.append('Ff')
print('Ff is appended :',a)
print()


#2.clear():removes all the elements from the list
print()
print('--2.clear()--')
b=['Old','is','Gold']
print(b)
print('---')
b.clear()
print('Results after applying clear()method: ',b)
print()

#3.copy():returns a copy of the list
print()
print('--3.copy()--')
c=['S','A','K','S','H','I']
print(c)
print('---')
c.copy()
print('copy of sakshi: ',c)
print()

#4.count():returns the number of elements with the specified value
print()
print('--4.count()--')
d=[-1,-3,None,'Laughter',True,9.9876,-1,-1,10,40]
print(d)
print('---')
ss=d.count(-1)
print('count of -1:',ss)
print()

#5.extend():add the elements of a list, to the end of the current list

print()
print('--5.extend()--')
e=['Humpty Dumpty']
print(e)
ee=['sat on a wall']
print('---')
e.extend(ee)
print('result after extend() method :',e)
print()

#6.index():returns the index of the first element with the specified value

print()
print('--6.index()--')
f=['100k',-1.10,True,'Chickoo','Potato',None]
print(f)
print('---')
ff=f.index(None)
print('Index/Position of None in the list : ',ff)
print()

#7.insert():adds an element at the specified position

print()
print('--7.insert()--')
g=['An apple','doctor away']
print(g)
print('---')
g.insert(1,'a day keeps')
print('Inserted at position 1 : ',g)
print()

#8.pop():removes the element at the specified position

print()
print('--8.pop()--')
h=['Twinkle', 'Tinkle', 'twinkle', 'little', 'star']
print(h)
print('---')
h.pop(1)
print('Removes element of 2nd index position:',h)
print()

#9.remove():removes the first item with the specified value

print()
print('--9.remove()--')
i=['Why','What','You','When']
print(i)
print('---')
i.remove('You')
print('You is removed :',i)
print()

#10.reverse():reverses the order of the list

print()
print('--10.reverse()--')
j=['D','U','B','A','I']
print(j)
print('---')
j.reverse()
print('Output after reverse :',j)
print()

#11.sort():sorts the list

print()
k=[-1,10,15.5,-190,-2.987767,2+3]
print(k)
print('---')
k.sort()
print('Output after sorting :',k)

 

# Dictionary Methods

#1.clear():Removes all the elements from the dictionary

print('---')
a={
    'id':18,
    'Name':'Virat Kohli',
    'Famous':'Yes',
    'Married':'Yes'
}
print(f'a={a}')
print()
a.clear()
print(f'Output_clear :{a}')
print()
print('---')

#2.copy():Returns a copy of the dictionary

print()
b={
    'aa':'Apple',
    'bb':None,
    'cc':-2.25,
    'dd':True,
    'ee':3-2
}
print(f'b={b}')
print()
b.copy()
print(f'Output_copy:{b}')
print()
print('---')


#3.fromkeys():It creates a new dictionary from the given sequence 
# with the specific value.

print()
c=['a',2,6.9,True]
print(f'c={c}')
print()
c=dict.fromkeys(c,10)
print(f'Output_fromkeys :{c}')
print('---')


#4.get():Returns the value of the specified key

print()
d={
    'Movie':'PK',
    'Ratings':'10',
    'Box Office Collection':'770 Crores',
    'Actor':'Amir Khan'
}
print(f'd={d}')
print()
dd=d.get('Box Office Collection')
print(f'Output_get :',dd)
print('---')


#5.items():Returns a list containing a tuple for each key value pair
 
print()
e={
    'a':'!1',
    'aa':'@2',
    'aaa':'#3',
    'aaaa':'$4'
}
print(f'e={e}')
print()
ee=e.items()
print(f'Output_items:{ee}')
print('---')


#6.pop():Removes the element with the specified key

print()
f={
    'P':'Twinkle',
    'O':'Twinklee',
    'E':'Little',
    'M':'Star'
}
print(f'f={f}')
print()
f.pop('M')
print(f'Output_pop :{f}')
print('---')


#7.popitem():Removes the last inserted key-value pair

print()
g={
    'id':18,
    'Name':'Virat Kohli',
    'Famous':'Obviously',
    'Married':'Yes'
}
print(f'g={g}')
print()
g.popitem()
print(f'Output_popitem:{g}')
print()
print('---')


#8.setdefault():Returns the value of the specified key. 
# If the key does not exist: insert the key, with the specified value
h={
    1:'One',
    3:'Three',
    5:'Five',
    7:'Seven'
}
print(f'h={h}')
print()
h.setdefault(9,'NINE')
print(f'Output_setdefault:{h}')
print()
print('---')
 

#9.update():Updates the dictionary with the specified key-value pairs

print()
i={
    'Icecream_flavour':'Butterscotch',
    'Icecream_colour':'Pink',
    'Icecrean_taste':'Delicious',
    'Rate_icecream out of 10': 9.5
}
print(f'i={i}')
print()
i.update({'Icecream_colour':'YELLOW'})
print(f'Output_update:{i}')
print()
print('---')

 
#10.values():Returns a list of all the values in the dictionary

print()
j={ 
    1:'One',
    3:'Three',
    5:'Five',
    7:'Seven'
}
print(f'j={j}')
print()
jj=j.values() 
print(f'Output_values:{jj}')
print()
print('---')

 
#11.keys():Returns a list containing the dictionary's keys
Student={
    'First_Name':'Priyanka',
    'Last_Name':'Chopra',
    'Class':10,
    'Age':16,
    'School':'Nagarparishad School'
}
print(f'Student={Student}')
print()
s=Student.keys()
print(f'Output_keys:{s}')
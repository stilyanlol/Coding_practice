# create a dict
mydict = {'name': 'Stichi', 'age': 23, 'city': 'Levunovo'}
mydict_2 = dict(name = 'Sashko', age = 22, city = 'Blgto')
print(mydict)

# assign keys and values to variables
name = mydict['name']
age = mydict['age']
city = mydict['city']
print(f'Hello, my name is {name}, I am {age} years old and I am from {city}!')

# add new keys and values to the dict
mydict['email'] = 'example@email.com'
print(f'{mydict} - added an email key and value')
# if we do the same and the key exists it will overwrite the value!
mydict['email'] = 'new_example@email.com'
print(f'{mydict} - modified the email')

# delete keys from the dict
del mydict['email']
print(f'{mydict} - deleted the email')
mydict.pop('age')
print(f'{mydict} - poped the age')
mydict.popitem() # default pops the last added item in the dict
print(f'{mydict} - poped last added items')

# ceck if a key is in the dict
if 'name' in mydict:
    print(mydict['name'], end='')
    print(' - prints the value')
if 'lastname' not in mydict:
    print('Key is non existent')

# try exept method for checking validity
try:
    print(mydict['name'])
except:
    print('error')
try:
    print(mydict['lastname'])
except:
    print('error')
    
# looping through dicts
mydict = {'name': 'Stichi', 'age': 23, 'city': 'Levunovo'}
for key in mydict:
    print(key)
for value in mydict.values():
    print(value)
for key, value in mydict.items():
    print(key, value)
    
#copy dict
mydict_cpy = mydict.copy()
mydict_cpy['email'] = 'example@sashkomail.com'
print(mydict)
print(f'{mydict_cpy} - modified only the copy')

# update dicts
mydict_2 = dict(name = 'Sashko', age = 22, city = 'Blgto')
mydict_cpy.update(mydict_2)
print(f'{mydict_cpy} - updated the dicts info')
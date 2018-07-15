#Automate the Boring Stuff with Python - Chapter 4
#Comma Code practice program

childName = []  #list that will store all names
printName = ''  #variable that will store a formated string of names

#Enter the names for all children, when finished type done
while True:
    print('Enter the name of child number ' + str(len(childName) +1 ) + ' in your family. When all names have been entered type "DONE".')
    name = input()
    if  name == 'DONE':
        break
    childName += [name]

#Format all items in the list to a single line. I had a little fun coding a different response for 0, 1, 2, and >= 3 items in the list.
for i in range(len(childName)-1):
    printName += childName[i] + ' is child number ' + str(i +1) + ', '
if  len(childName) == 0:
    print('What! You have no children?')
elif  len(childName) == 1:
    print('If you can''t even remember the name of one child I am not going to help you. Hint: (' + childName[0][:2] + ')')
elif len(childName) == 2:
    print('Names are stored in volatile memory huh? Here you go, your oldest child is ' + childName[0] + ' and your youngest is ' + childName[1] + '.')
else:
    print('Whoah... that is a lot of kids. I have your children''s names recorded here. Please be patient, this may take a while for me to retrieve all of those names.')
    printName += 'and ' + childName[-1] + ' is child number ' + str(len(childName)) + '.'
    print(printName)

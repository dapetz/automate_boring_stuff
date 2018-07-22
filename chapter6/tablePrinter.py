#Automate the Boring Stuff with Python - Chapter 6
#Table Print practice program

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    colWidths = [0] * len(data)     #create list to store len values
    for i in colWidths:
        colWidths = len(max(data[i], key=len))
        
    
    for r in range(len(data[0])):
        print()
        for c in range(len(data)):
            print(data[c][r].rjust(colWidths), end='')
            
    return data

printTable(tableData)

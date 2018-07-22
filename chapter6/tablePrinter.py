#Automate the Boring Stuff with Python - Chapter 6
#Table Print practice program

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    colWidths = []     
    maxWidth = 0
    for i in range(len(data)):      #find the max column length for each row
        colWidths.append(len(max(data[i], key=len)))
    maxWidth = max(colWidths)       #find the max column length across all rows
    
    for r in range(len(data[0])):   #pass the max column length to the rjust method
        print()
        for c in range(len(data)):
            print(data[c][r].rjust(maxWidth), end='')
    return data

printTable(tableData)

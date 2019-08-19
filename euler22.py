file =  open("names.txt", 'r')                        #Download the file `names.txt` from the link provided in line - 3

#https://projecteuler.net/project/resources/p022_names.txt

allNames = file.read()
allNames = allNames.replace("\"","").split(",")
allNames = sorted(allNames)

def alphaPos(string):
    pos = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4,
    'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9,
    'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14,
    'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 's' : 19,
    't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24,
    'y' : 25, 'z' : 26}
    total = 0
    for i in string:
        total+=pos[i]
    return total
print(alphaPos("zulim")*5613)
counter = 0
tSum = 0
for i in allNames:
    counter+=1
    i = i.lower()
    nameSum = alphaPos(i)*counter
    tSum+=nameSum
print(tSum)

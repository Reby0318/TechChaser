#Get the name of the file and open it
#name = input ('Expressions')
#hanle = open (name, 'r')

#Count word frequency
counts = dict()
for line in hanle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

#Find the most common word
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

#All done
#print (bigword, bigcount)
#Name my file 'Expressions.py'

#Converting User Input
#Convert elevator floors
inp= input ("Europe floor?")
usf = int(inp) + 1
print ('US floor', usf)

#Conclusion
name=input ("Enter your name")
print("Reby")
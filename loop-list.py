name=['parmod',"rachana",'kamal',"bajrang"]
for x in name:#loop thorough list item using for loop
    print(x)

for i in range(len(name)):  #loop through index number
    print(name[i])

i=0
while i<len(name): #using a while loop
    print(name[i])
    i+=1
[print(x) for x in name] #looping using list comprehension
name=['parmod',"rachana",'Kamal',"bajrang","sacha"]
# name.sort() #sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
# name.sort(reverse=True)
name.sort(key=str.lower)  #case-insensitive sort function, use str.lower as a key function
# name.reverse()#reverse the currunt sorting order
print(name)

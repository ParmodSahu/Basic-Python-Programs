name=['parmod',"rachana",'Kamal',"bajrang","sacha"]
# newlist=name.copy()#copy a list in another variable
# # newlist=list(name)#copy to used built in method list()
# newlist.append('aman')
# print(name)
# print(newlist)
secondlist=['kuldeep','vijay','shyam']
# finallist=name+secondlist #join to list using + operator
# print(finallist)
name.extend(secondlist)
print(name)
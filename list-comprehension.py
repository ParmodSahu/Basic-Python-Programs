name=['parmod',"rachana",'kamal',"bajrang","sacha"]
# [print(x) for x in name] #looping using list comprehension
newlist=[x for x in name if "ch" not in x]
# newlist = [expression for item in iterable if condition == True]
print(newlist)
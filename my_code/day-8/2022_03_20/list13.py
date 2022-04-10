list1=["a","b"]
list2=["c","d"]
#extend list1 to adopt the elemnts from list2
#final list should be ["a","b","c","d"]
#['a', 'b', ['c', 'd']] no correct
list1.extend(list2)
print(list1)

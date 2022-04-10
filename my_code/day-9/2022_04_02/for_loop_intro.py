#for loop can be created in two different ways
#1 st  using range function
#range(1,6)
#the above example creates a list internally with [1,2,3,4,5]
# this means loop is going to execute/iterate 5 times
#why 5 ?
#range function gererates the list with 5 elements, that is why loop is going to execute 5 times
#execution of loop means what ever you write with a tab , those lines will be executed multuiple times as per the the above rule
#every execution i will get a new value from the range starting from 1 to 5
for i in range(2,6):
    print(i,10,"ok")

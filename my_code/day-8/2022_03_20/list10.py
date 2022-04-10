#slicing in list
num=[1,2,3,4,5,6,7]
#only print [2,3,4]
#: known as slicing operator in python list
#fisrt index will inclusive and last one will exclusive
print(num[1:4])
#change postion 2 , 3 , 4 th with a value 8 only
#[1,8,5,6,7]
num[1:4]=[8]
roni=len(num)
print(roni)
#change position number 4 value to 10
#so it should be [1,8,5,10,7]
num[3]=10
print(num)


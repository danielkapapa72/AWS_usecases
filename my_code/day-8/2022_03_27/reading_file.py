#how to read from a text file in python 
import io #io module for input and opput operations 
with io.open("test.txt","r",encoding="utf-8") as f1 :#(filename,mode,encoding)
    data=f1.read()
    f1.close()
#print(data)
#\n is new line character
#how to count how many lines are there in your file
lines=data.split("\n")
#count of lines
print(len(lines))
#writing one by one
for line in lines:
    print(line)



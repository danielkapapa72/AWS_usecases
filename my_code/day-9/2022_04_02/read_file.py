import io
with io.open("input.csv","r",encoding="utf-8")as f1:
    data=f1.read()
    f1.close()
lines=data.split("\n")
for xx in lines:
    print(xx)

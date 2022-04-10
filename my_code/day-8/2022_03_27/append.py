import io
with io.open("output.txt","a",encoding="utf-8")as f1:
    f1.write("test1"+"\n") # when we need next line then we must use "\n"
    f1.write("test2"+"\n")
    f1.write("test3")
    f1.close()

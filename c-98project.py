def swapfiles():
    file1=input("please enter the name of the file 1 : ")
    file2=input("please enter the name of the fie 2 : ")
    with open(file1,'r') as a :
        data_a = a.read()
    with open(file2,'r') as b :
        data_b = b.read()
    
    with open(file1,'w') as a:
        a.write(data_b)
    with open(file2,'w') as b:
        b.write(data_a)


swapfiles()

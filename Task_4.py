N = int(input("Input number"))
def func(N):
    a = ""
    while N !=0:
        b = str(N%2)
        a= b+a
        N = N//2
    return a
print(func(N))
   
       
    

        

#def hello():
 #   print("hello")    

#name= input("whats ur name")
#hello()
#print(name)



#def hello(to):
#    print("Hello,", to)

#name =input("whats your name")
#hello(name)    



#def hello(to="world"):
#    print("Hello,", to)

#hello()
#name=input("Whats your name")
#hello(name)    

def main():
    x= int (input ("Whats x?"))
    print("x squared is ", square(x))

def square(n):
    #return n*n
    return pow(n,2)
main()    

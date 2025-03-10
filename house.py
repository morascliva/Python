#name = input("Whats your name")

#if name =="Harry":
#    print("Gryffindor")
#elif name == "Hermione":
#    print("Gryffindor")
#elif name =="Ron":
#    print("Gryffindor")
#elif name =="Draco":
#    print("Slytherin")  
#else:
#    print("Who?")    


#name = input("Whats your name")

#if name =="Harry" or name =="Hermoine" or name == "Ron":    print("Gryffindor")
#elif name =="Draco":
#    print("Slytherin")  
#else:
#    print("Who?")                  

name = input("Whats your name")

#match name:
#    case "Harry":
#        print("Gryffindor")
#    case "Hermoine":
#        print("Gryffindor")  
#    case "Ron":
#        print("Gryffindor") 
#    case "Draco":
#        print("Syltherine") 
#    case _:
#        print("Who")            

name = input("Whats your name")

match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
   
    case "Draco":
        print("Syltherine") 
    case _:
        print("Who")    

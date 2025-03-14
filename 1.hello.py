
#name =input("Whats your name ?")
#print("Hello, "+name)

#include space
# print("Hello, ", name)

#include quotations
#print( "Hi, \"student\"")

#print("Hello," , end="")
#print(name) 

#removes whitespace from string  from the left and right 
#name=name.strip()
#capitalizes the first string
#name=name.capitalize() 
#capitalizes the entire string 
#name=name.title()

#name=name.strip().title()


name =input("Whats your name ?").strip().title()
#print(f"Hello, {name}")

first,last =name.split()

print("Hello " +first)


#name =input("Whats your name ?")
#print("Hello, "+name)

#include space
# print("Hello, ", name)

#include quotations
#print( "Hi, \"student\"")

#print("Hello," , end="")    #end overrides \n
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




# f-strings allow embedding expressions inside {} within a string.
#"Hello, {name}"
#{name} is a placeholder inside the string.
#Python replaces {name} with the value of the name variable at runtime

first,last =name.split()

print("Hello " +first)

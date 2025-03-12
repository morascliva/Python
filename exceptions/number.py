#try:
#  x=int(input("Whats x?"))
#  print(f"x is {x}")
#except ValueError:
#    print("x is not an integer")


#try:
#  x = int(input("Whats x?"))
#except ValueError:
#  print("x is not an integer")
#else:
#  print(f"x is {x}")


while True:
    try:
      x = int(input("Whats x?"))
    except ValueError:
      print("x is not an integer")
    else:
      break
print(f"x is {x}")      





def mass_to_energy(mass):
    c = 300000000 
    energy = mass * c**2
    return energy

mass = int(input("Mass in kg: "))  
print(f"Energy (J): {mass_to_energy(mass)}")  # Output energy in Joules

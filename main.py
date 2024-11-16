def a(mass,acceleration):
    force = mass*acceleration
    print(f"force = {force}N")
a(600,50)

def b(velocity, time):
    acceleration = velocity/time
    print(f"acceleration = {acceleration}m/s^2")
b(5,6)

def c(force,time):
    impulse = force*time
    print(f"impulse = {impulse}Ns")
c(40,8)

def d(distance,time):
    speed = distance/time
    print(f"speed = {speed}m/s")
d(66,6)

def e(mass,acceleration_due_to_gravity,height):
    potential_energy = mass*acceleration_due_to_gravity*height
    print(f"potential_energy = {potential_energy}J")
e(55,38,50)

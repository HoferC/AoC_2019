import math


def calcFuel(mass):
    return math.floor(int(mass) / 3) - 2


def calcFuelForFuel(fuel):
    totalFuel = 0
    fuelForFuel = calcFuel(fuel)
    while fuelForFuel > 0:
        totalFuel += fuelForFuel
        fuelForFuel = calcFuel(fuelForFuel)
    return totalFuel

def star1():
    totalFuel = 0
    with open("puzzles/day1.txt", "r") as f:
        mass = f.readline()
        while mass:
            fuelForCargo = calcFuel(mass)
            totalFuel += fuelForCargo
            mass = f.readline()
    print("Fuel for Mass without Fuel:", totalFuel)

def star2():
    totalFuel = 0
    with open("puzzles/day1.txt", "r") as f:
        mass = f.readline()
        while mass:
            fuelForCargo = calcFuel(mass)
            totalFuel += fuelForCargo
            #print("Cargo:", mass)
            #print("Fuel for cargo: ", fuelForCargo)
            # "Recursively" figure out the mass taken by the fuel plus the mass
            totalFuel += calcFuelForFuel(fuelForCargo)
            mass = f.readline()
    print("Fuel for Mass with Fuel:", totalFuel)



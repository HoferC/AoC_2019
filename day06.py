import math

class Planet:
    name = ''
    valid = True

    def __init__(self, newName, isValid = True):
        self.orbitingPlanets = []
        self.name = newName
        self.valid = isValid
        self.orbitParent = 0

    def __str__(self):
        return self.name

    def findOrbitingPlanet(self, orbitName):
        for p in self.orbitingPlanets:
            if p.name == orbitName:
                return p
            else:
                o = p.findOrbitingPlanet(orbitName)
                if o.valid:
                    return o
        return Planet("INVALID", False)

    def addOrbit(self, newOrbiter):
        self.orbitingPlanets.append(newOrbiter)
        newOrbiter.orbitParent = self

    def printOrbits(self, tabLevel = 0):
        print(''.join(['\t'*tabLevel]), self.name)
        for p in self.orbitingPlanets:
            p.printOrbits(tabLevel + 1)

    def countOrbits(self):
        if len(self.orbitingPlanets) == 0:
            return 1
        orbitCount = 1
        for p in self.orbitingPlanets:
            orbitCount += p.countOrbits()
        return orbitCount

    def countOrbitsBackwards(self, planetName = "COM"):
        if self.name == planetName:
            return 0
        currentPlanet = self
        distance = 0
        while currentPlanet.name != planetName:
            currentPlanet = currentPlanet.orbitParent
            distance += 1
        return distance

    def getChainToPlanet(self, planetName = "COM"):
        chain = []
        currentPlanet = self
        while currentPlanet.name != planetName:
            chain.insert(0, currentPlanet)
            currentPlanet = currentPlanet.orbitParent
        return chain



def buildPlanetDirectory():
    com = Planet("COM")
    planetDirectory = {}
    planetDirectory["COM"] = com
    with open('puzzles/day6.txt', 'r') as f:
        lines = f.read().splitlines()
        for l in lines:
            planets = l.split(')')
            centerName = planets[0]
            orbitName = planets[1]
            # print("Center:", centerName, "Orbit:", orbitName)
            if not centerName in planetDirectory:
                planetDirectory[centerName] = Planet(centerName)
            if not orbitName in planetDirectory:
                planetDirectory[orbitName] = Planet(orbitName)

            planetDirectory[centerName].addOrbit(planetDirectory[orbitName])
    return planetDirectory


def star1():
    print("Day 6 Star 1")
    planetDirectory = buildPlanetDirectory()

    orbitCount = 0
    for planet in planetDirectory.values():
        orbitCount += planet.countOrbitsBackwards()
    print(orbitCount)


def star2():
    print("Star 2")
    planetDirectory = buildPlanetDirectory()
    # Find YOU and SAN
    you = planetDirectory["YOU"].orbitParent
    san = planetDirectory["SAN"].orbitParent
    youChain = you.getChainToPlanet("COM")
    sanChain = san.getChainToPlanet("COM")
    print("Your chain back to COM:", len(youChain))
    print("Santa's chain back to COM:", len(sanChain))

    # Iterate from COM through each of the chains until they diverge
    lastCommonIndex = 0
    for i in range(1, min(len(youChain), len(sanChain))):
        if youChain[i].name != sanChain[i].name:
            lastCommonIndex = i-1
            break
    if not youChain[lastCommonIndex].name == sanChain[lastCommonIndex].name:
        print("ERROR! Common Ancestors don't match!")
    commonAncestor = youChain[lastCommonIndex]

    print("Common Ancestor:", commonAncestor)
    print(commonAncestor, "chain back to COM:", len(commonAncestor.getChainToPlanet("COM")))
    print("You chain to ", commonAncestor, you.countOrbitsBackwards(commonAncestor.name))
    print("Santa chain to ", commonAncestor, san.countOrbitsBackwards(commonAncestor.name))
    totalDistance = you.countOrbitsBackwards(commonAncestor.name) + san.countOrbitsBackwards(commonAncestor.name)
    print("Total Distance:", totalDistance)



star1()
star2()
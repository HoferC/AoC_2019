import intcode

def star1():
    print("Star 1")
    with open("puzzles/day9.txt") as f:
        programText = f.readline()
    computer = intcode.IntCodeComputer()
    computer.loadProgram(programText)
    computer.process('1', False)



def star2():
    print("Star 2")
    with open("puzzles/day9.txt") as f:
        programText = f.readline()
    computer = intcode.IntCodeComputer()
    computer.loadProgram(programText)
    computer.process('2', False)

star1()
star2()
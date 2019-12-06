import intcode

def star1():
    print("Star 1")
    computer = intcode.IntCodeComputer()
    with open('puzzles/day5.txt', 'r') as f:
        program = f.readline()
        computer.loadProgram(program)
        computer.process('1', False)



def star2():
    print("Star 2")
    computer = intcode.IntCodeComputer()
    with open('puzzles/day5.txt', 'r') as f:
        program = f.readline()
        computer.loadProgram(program)
        computer.process('5', False)

star1()
star2()
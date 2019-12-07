import intcode
from itertools import permutations



def star1():
    print("Star 1")
    # Get all permutations of [0, 1, 2, 3, 4]
    perm = permutations([0, 1, 2, 3, 4])
    stages = []
    for i in range(5):
        stages.append(intcode.IntCodeComputer())
    with open('puzzles/day7.txt', 'r') as f:
        program = f.readline()
    maxOutput = 0
    for p in list(perm):
        prevStageOutput = 0
        for i in range(len(stages)):
            stages[i].loadProgram(program)
            stages[i].process(str(p[i]) + '\n' + str(prevStageOutput))
            prevStageOutput = stages[i].lastOutput
        finalStageOutput = stages[-1].lastOutput
        if finalStageOutput > maxOutput:
            maxOutput = finalStageOutput

    print("Max Thruster Output:", maxOutput)



def star2():
    print("Star 2")
    # Get all permutations
    perm = permutations([5, 6, 7, 8, 9])
    stages = []
    for i in range(5):
        stages.append(intcode.IntCodeComputer())

    with open('puzzles/day7.txt', 'r') as f:
        program = f.readline()
    maxOutput = 0
    # Iterate over permutations of phase codes
    for p in list(perm):
        prevStageOutput = 0
        for i in range(len(stages)):
            # For each set of phase codes, load the program
            # and add the phase code as the first input
            stages[i].loadProgram(program)
            stages[i].addInput(p[i])
        while not stages[0].isTerminated:
            for i in range(len(stages)):
                #print("&&& PROCESSING {0} &&&".format(i))
                stages[i].process(prevStageOutput, silent=True)
                #print("Stage {0} Complete. Instruction Pointer: {1}. Last Output: {2}".format(i, stages[i].instrPtr, stages[i].lastOutput))
                prevStageOutput = stages[i].lastOutput

        finalStageOutput = prevStageOutput
        if finalStageOutput > maxOutput:
            maxOutput = finalStageOutput

    print("Max Thruster Output:", maxOutput)


star1()
star2()
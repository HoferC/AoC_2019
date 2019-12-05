def dumpMemory(memory):
    output = ''
    for m in memory:
        output = output + str(m) + ','
    # Remove trailing comma when returning
    return output[0:len(output)-1]


def processIntCode(memory):
    index = 0
    while index < len(memory):
        command = memory[index]
        if command == 99:
            # Break immediately to avoid array out of bounds
            break
        op1 = int(memory[index + 1])
        op2 = int(memory[index + 2])
        dest = int(memory[index + 3])
        if command == 1:
            # Add
            memory[dest] = memory[op1] + memory[op2]

        elif command == 2:
            # Multiply
            memory[dest] = memory[op1] * memory[op2]
        index += 4
    return dumpMemory(memory)


def star1():
    print("Star 1")
    with open("puzzles/day2a.txt", "r") as f:
        instructionString  = f.readline()
        while instructionString:
            memory = []
            instructions = instructionString.split(',')
            for m in instructions:
                memory.append(int(m))
            # If we're working with the real case, set up the '1202 error'
            if len(memory) > 30:
                memory[1] = 12
                memory[2] = 2
            result = processIntCode(memory)
            print(result)
            instructionString = f.readline()


def star2():
    seed1 = 0
    seed2 = 0
    desiredAnswer = 19690720
    victory = 0
    with open("puzzles/day2.txt", "r") as f:
        instructionString = f.readline()
        instructions = instructionString.split(',')
        for seed1 in range(100):
            if victory != 0:
                break
            for seed2 in range(100):
                if victory != 0:
                    break
                memory = []
                for m in instructions:
                    memory.append(int(m))
                memory[1] = seed1
                memory[2] = seed2
                result = processIntCode(memory)
                if memory[0] == desiredAnswer:
                    victory = 100 * seed1 + seed2
        print(victory)
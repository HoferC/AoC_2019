class IntCodeComputer:

    def __init__(self):
        self.memory = []
        self.lastOutput = -1
        self.isTerminated = True
        self.input = []
        self.instrPtr = 0
        self.relativeBase = 0

    def dumpMemory(self):
        output = ''
        count = 0
        for m in self.memory:
            output = output + str(count) + ':' + str(m) + '\n'
            count += 1
        # Remove trailing comma when returning
        return output[0:len(output)-1]

    def readMemory(self, location:int):
        while len(self.memory) < location + 1:
            self.memory.append(0)
        return self.memory[location]

    def writeMemory(self, location:int, value:int):
        while len(self.memory) < location + 1:
            self.memory.append(0)
        self.memory[location] = value

    def getParameterValue(self, location, mode, verbose = False):
        if mode == 0:
            # Position Mode
            return self.readMemory(self.readMemory(location))
        if mode == 1:
            # Parameter Mode
            return self.readMemory(location)
        if mode == 2:
            # Relative mode
            if verbose:
                print("Relative Base: {0} - Operand: {1}".format(self.relativeBase, location))
            return self.readMemory(self.readMemory(location) + self.relativeBase)

    def setParameterValue(self, location, mode, value, verbose = False):
        if mode == 0:
            # Position Mode
            self.writeMemory(self.readMemory(location), value)
        if mode == 1:
            # Parameter Mode
            raise ValueError()
        if mode == 2:
            # Relative mode
            if verbose:
                print("Relative Base: {0} - Operand: {1}".format(self.relativeBase, location))
            self.writeMemory(self.readMemory(location) + self.relativeBase, value)


    def addInput(self, newInput:int):
        self.input.append(newInput)

    # Load a program into memory but does not execute it
    def loadProgram(self, progString):
        self.isTerminated = False
        self.memory = []
        self.instrPtr = 0
        instructions = progString.split(',')
        for m in instructions:
            self.memory.append(int(m))
        # print("Program Load Complete. Memory Size:", len(self.memory))

    def process(self, inputString = '', verbose = False, silent = False):
        input = str(inputString).split('\n')
        for i in input:
            self.input.append(i)
        while self.instrPtr < len(self.memory):
            if verbose:
                print('--- Scan ---')
                print('InstrPtr:', self.instrPtr)
                print('RelBase:', self.relativeBase)
            # Read the instruction as a string so we can index its digits
            instruction = str(self.memory[self.instrPtr])
            # Once we have the instruction, we need to parse it
            # which will tell us whether we are looking at position
            # or immediate mode
            if verbose:
                print('Instruction:', instruction)
            if len(instruction) < 3:
                opcode = int(instruction)
                modes = '000'
            else:
                opcode = int(instruction[-2:])  
                modes = instruction[:-2].zfill(3)
            if verbose:
                print("OpCode:", opcode)
                print("Mode:", modes)

            if opcode == 99:
                # Break immediately to avoid array out of bounds
                if verbose:
                    print("Program Halt")
                self.isTerminated = True
                break
            if opcode == 1:
                # Add
                # 3 operands
                op1 = self.getParameterValue(self.instrPtr + 1, int(modes[-1]))
                op2 = self.getParameterValue(self.instrPtr + 2, int(modes[-2]))
                result = op1 + op2
                if verbose:
                    print('Add', op1, '+', op2, '=', result)
                self.setParameterValue(self.instrPtr+3, int(modes[-3]), result)
                self.instrPtr += 4

            elif opcode == 2:
                # Multiply
                # 3 operands
                op1 = self.getParameterValue(self.instrPtr + 1, int(modes[-1]))
                op2 = self.getParameterValue(self.instrPtr + 2, int(modes[-2]))
                result = op1 * op2
                if verbose:
                    print('Mul', op1, '*', op2, '=', result)
                self.setParameterValue(self.instrPtr+3, int(modes[-3]), result)
                self.instrPtr += 4
            
            elif opcode == 3:
                # Input Save
                if len(self.input) == 0:
                    # No input available, break
                    break
                inputVal = int(self.input.pop(0))
                if verbose:
                    print("Processing input", inputVal)
                self.setParameterValue(self.instrPtr + 1, int(modes[-1]), inputVal, verbose=True)
                self.instrPtr += 2

            elif opcode == 4:
                # Output
                op1 = self.getParameterValue(self.instrPtr + 1, int(modes[-1]))
                if not silent:
                    print('********')
                    print(op1)
                    print('********')
                self.lastOutput = op1
                self.instrPtr += 2

            elif opcode == 5:
                # Jump if true
                op1 = self.getParameterValue(self.instrPtr + 1, int(modes[-1]))
                op2 = self.getParameterValue(self.instrPtr + 2, int(modes[-2]))
                if op1:
                    self.instrPtr = op2
                else:
                    self.instrPtr += 3

            elif opcode == 6:
                # Jump if false
                op1 = self.getParameterValue(self.instrPtr + 1, int(modes[-1]))
                op2 = self.getParameterValue(self.instrPtr + 2, int(modes[-2]))
                if not op1:
                    self.instrPtr = op2
                else:
                    self.instrPtr += 3

            elif opcode == 7:
                # Less than
                op1 = self.getParameterValue(self.instrPtr + 1, int(modes[-1]))
                op2 = self.getParameterValue(self.instrPtr + 2, int(modes[-2]))
                # 3rd operand always has to be position mode
                if op1 < op2:
                    self.setParameterValue(self.instrPtr+3, int(modes[-3]), 1)
                else:
                    self.setParameterValue(self.instrPtr+3, int(modes[-3]), 0)
                self.instrPtr += 4


            elif opcode == 8:
                # Equals
                op1 = self.getParameterValue(self.instrPtr+1, int(modes[-1]))
                op2 = self.getParameterValue(self.instrPtr+2, int(modes[-2]))
                # 3rd operand  always has to be position mode
                if op1 == op2:
                    self.setParameterValue(self.instrPtr+3, int(modes[-3]), 1)
                else:
                    self.setParameterValue(self.instrPtr+3, int(modes[-3]), 0)
                self.instrPtr += 4


            elif opcode == 9:
                # Set Relative Pointer
                op1 = self.getParameterValue(self.instrPtr + 1, int(modes[-1]), verbose)
                if verbose:
                    print('Adjusting RelPtr by {0}'.format(op1))
                self.relativeBase += op1
                if verbose:
                    print("New Relative Base: {0}".format(self.relativeBase))
                self.instrPtr += 2

            else:
                print("**** ERROR ****")
                print("Unrecognized OpCode:", opcode)
                if verbose:
                    print(self.dumpMemory())
                break

        return self.dumpMemory()

    



    # Updates the memory in a location to the provided value
    # location and value must be integers
    def modifyMemory(self, location, value):
        self.memory[location] = value

    # Gets the value stored in memory at the given location
    def getValue(self, location):
        return self.memory[location]
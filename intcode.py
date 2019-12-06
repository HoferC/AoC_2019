class IntCodeComputer:

    def __init__(self):
        self.memory = []

    def dumpMemory(self):
        output = ''
        count = 0
        for m in self.memory:
            output = output + str(count) + ':' + str(m) + '\n'
            count += 1
        # Remove trailing comma when returning
        return output[0:len(output)-1]

    def processOperand(self, operand, mode, verbose = False):
        if verbose:
                print('Op', operand, 'Mode', mode)
        if mode == 0:
            return self.memory[operand]
        if mode == 1:
            return operand


    def process(self, inputString = '', verbose = False):
        instrPtr = 0
        while instrPtr < len(self.memory):
            if verbose:
                print('InstrPtr:', instrPtr)
            # Read the instruction as a string so we can index its digits
            instruction = str(self.memory[instrPtr])
            # Once we have the instruction, we need to parse it
            # which will tell us whether we are looking at position
            # or immediate mode
            if verbose:
                print('I:', instruction)
            if len(instruction) < 3:
                opcode = int(instruction)
                modes = '000'
            else:
                opcode = int(instruction[-2:])  
                modes = instruction[:-2].zfill(3)
            if verbose:
                print("OpCode:", opcode)
                print("M:", modes)

            if opcode == 99:
                # Break immediately to avoid array out of bounds
                print("Program Halt")
                break
            if opcode == 1:
                # Add
                # 3 operands
                op1 = self.processOperand(self.memory[instrPtr+1], int(modes[-1]))
                op2 = self.processOperand(self.memory[instrPtr+2], int(modes[-2]))
                # 3rd operand always has to be position mode
                op3 = self.memory[instrPtr+3]
                result = op1 + op2
                if verbose:
                    print('Add', op1, '+', op2, '=', result)
                    print('Sto:', op3)
                self.memory[op3] = result
                instrPtr += 4

            elif opcode == 2:
                # Multiply
                # 3 operands
                op1 = self.processOperand(self.memory[instrPtr+1], int(modes[-1]))
                op2 = self.processOperand(self.memory[instrPtr+2], int(modes[-2]))
                # 3rd operand always has to be position mode
                op3 = self.memory[instrPtr+3]
                result = op1 * op2
                if verbose:
                    print('Mul', op1, '*', op2, '=', result)
                    print('Sto:', op3)
                self.memory[op3] = result
                instrPtr += 4
            
            elif opcode == 3:
                # Input Save
                inputVal = int(inputString)
                op1 = self.memory[instrPtr+1]
                self.modifyMemory(op1, inputVal)
                instrPtr += 2

            elif opcode == 4:
                # Output
                op1 = self.processOperand(self.memory[instrPtr+1], int(modes[-1]))
                print('********')
                print(op1)
                print('********')
                instrPtr += 2

            elif opcode == 5:
                # Jump if true
                op1 = self.processOperand(self.memory[instrPtr+1], int(modes[-1]))
                op2 = self.processOperand(self.memory[instrPtr+2], int(modes[-2]))
                if op1:
                    instrPtr = op2
                else:
                    instrPtr += 3

            elif opcode == 6:
                # Jump if false
                op1 = self.processOperand(self.memory[instrPtr+1], int(modes[-1]))
                op2 = self.processOperand(self.memory[instrPtr+2], int(modes[-2]))
                if not op1:
                    instrPtr = op2
                else:
                    instrPtr += 3

            elif opcode == 7:
                # Less than
                op1 = self.processOperand(self.memory[instrPtr+1], int(modes[-1]))
                op2 = self.processOperand(self.memory[instrPtr+2], int(modes[-2]))
                # 3rd operand always has to be position mode
                op3 = self.memory[instrPtr+3]
                if op1 < op2:
                    self.memory[op3] = 1
                else:
                    self.memory[op3] = 0
                instrPtr += 4


            elif opcode == 8:
                # Equals
                op1 = self.processOperand(self.memory[instrPtr+1], int(modes[-1]))
                op2 = self.processOperand(self.memory[instrPtr+2], int(modes[-2]))
                # 3rd operand  always has to be position mode
                op3 = self.memory[instrPtr+3]
                if op1 == op2:
                    self.memory[op3] = 1
                else:
                    self.memory[op3] = 0
                instrPtr += 4


            else:
                print("**** ERROR ****")
                print("Unrecognized OpCode:", opcode)
                if verbose:
                    print(self.dumpMemory())
                break



        return self.dumpMemory()

    
    # Load a program into memory but does not eecute it
    def loadProgram(self, progString):
        print("Loading Memory...")
        self.memory = []
        instructions = progString.split(',')
        for m in instructions:
            self.memory.append(int(m))
        print("Load Complete. Memory Size:", len(self.memory))


    # Updates the memory in a location to the provided value
    # location and value must be integers
    def modifyMemory(self, location, value):
        self.memory[location] = value

    # Gets the value stored in memory at the given location
    def getValue(self, location):
        return self.memory[location]
"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0

    def ram_read(self, MAR): # Memory Access Register
        # Finds and returns value at given address (= index)
        return self.ram[MAR]

    def ram_write(self, MAR, MDR): # Memory Data Register
        # Writes/overwrites value at given address
        self.ram[MAR] = MDR    

    def load(self):
        """Load a program into memory."""

        address = 0
        if len(sys.argv) < 2:
            print('The program name is required')
            sys.exit()

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1
        while open(sys.argv[1]) as f:
            for line in f:
                if line[0] != '#' and line != '\n':
                    self.ram[address] = int(line[0:8], 2)
                    address += 1
                    
                f.closed



    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        HLT = 0b00000001
        LDI = 0b10000010
        PRN  = 0b01000111 
        PUSH = 0b01000101 
        POP  = 0b01000110 
        MUL  = 0b10100010
        running = True

        while running:
            IR = self.ram[self.pc]

            operand_a = self.ram_read(self.pc +1)
            operand_b = self.ram_read(self.pc +2)
            if IR == HLT:
                running = False
            elif IR == LDI:
                self.reg[operand_a] = operand_b
                self.pc += 3
            elif IR == PRN:
                print(self.reg[operand_a])
                self.pc += 2
            elif IR == MUL:
                self.alu("MUL ->", operand_a, operand_b)
                self.pc += 3
            else:
                print("HALTED")
                running = False

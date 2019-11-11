PRINT_BEEJ = 1
HALT = 2
SAVE_REG = 3
PRINT_REG = 4

memory = [
    PRINT_BEEJ,
    SAVE_REG, # SAVE_REG value 2 in R2
    10,# Value 10
    2, # R2
    PRINT_REG,
    2,
    HALT,
]

# ------
# print('Beej!')
# r2 = 10
# print(r2)
# ------

register = [0] * 8 # Like variables, fixed number of them, fixed names R0 R1 R2 ... R7

pc = 0 # Program counter, current index, pointer to currently executing instruction
halted = False

while not halted:
    instruction = memory[pc]

    if instruction == PRINT_BEEJ:
        print('Beej!')

        pc += 1
    elif instruction == SAVE_REG:
        value = memory[pc + 1]
        reg_num = memory[pc + 2]

        register[reg_num] = value

        pc += 3
    elif instruction == PRINT_REG:
        reg_num = memory[pc + 1]
        print(register[reg_num])

        pc += 2

    elif instruction == HALT:
        halted = True

        pc += 1
    else:
        print(f'Unknown instruction at index {pc}')
        sys.exit(1)



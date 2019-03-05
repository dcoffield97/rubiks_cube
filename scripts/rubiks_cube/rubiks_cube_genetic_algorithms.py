import rubiks_cube

"""
RULES:
    * The further that a chromosome is from the optimal fitness, the more likely it is that mutating a bit further to the left will increase the fitness the most
    * The closer that a chromosome is to the optimal fitness, the more likely it is that mutating a bit further to the right will increase the fitness the most
    * Therefore, it is more likely that chromosomes with the optimal fitness will be found close to other highly-fit chromosomes
"""

def Get_Rubiks_Cube_Chromosome(cube_turns_executed_list):
    rubiks_cube_chromosome = ""
    rubiks_cube_turns_list = rubiks_cube.Get_Rubiks_Cube_Turns_List()
    
    for cube_turn_executed in cube_turns_executed_list:
        cube_turn_binary_value = bin(rubiks_cube_turns_list.index(cube_turn_executed))[2:]
        rubiks_cube_chromosome = rubiks_cube_chromosome + cube_turn_binary_value
    
    return rubiks_cube_chromosome

def Get_Rubiks_Cube_Chromosome_Fitness(rubiks_cube_chromosome, cube):
    rubiks_cube_chromosome_fitness = None
    cube_turns_executed_list = Get_Cube_Turns_Executed_List(rubiks_cube_chromosome)
    for cube_turn_executed in cube_turns_executed_list:
        cube = rubiks_cube.Get_Rotated_Cube(cube, cube_turn_executed)
    
    rubiks_cube_chromosome_fitness = Get_Rubiks_Cube_Fitness(cube)
    
    return rubiks_cube_chromosome_fitness

def Get_Rubiks_Cube_Fitness(cube):
    rubiks_cube_fitness = None
    
    return rubiks_cube_fitness

def Get_Cube_Turns_Executed_List(rubiks_cube_chromosome):
    cube_turns_executed_list = []
    rubiks_cube_turns_list = rubiks_cube.Get_Rubiks_Cube_Turns_List()
    cube_turn_binary_length = len(bin(len(rubiks_cube_turns_list))[2:])
    rubiks_cube_chromosome_binary_index = 0
    while rubiks_cube_chromosome_binary_index < (len(rubiks_cube_chromosome) - cube_turn_binary_length - 1):
        cube_turn_executed_binary_value = rubiks_cube_chromosome[rubiks_cube_chromosome_binary_index:(rubiks_cube_chromosome_binary_index + cube_turn_binary_length)]
        cube_turn_executed_turn_list_index = int(cube_turn_executed_binary_value, base = 2)
        cube_turn_executed = rubiks_cube_turns_list[cube_turn_executed_turn_list_index]
        cube_turns_executed_list.append(cube_turn_executed)
        rubiks_cube_chromosome_binary_index = rubiks_cube_chromosome_binary_index + cube_turn_binary_length
    
    return cube_turns_executed_list
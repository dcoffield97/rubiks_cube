import random
import rubiks_cube

"""
RULES:
    * The further that a chromosome is from the optimal fitness, the more likely it is that mutating a bit further to the left will increase the fitness the most
    * The closer that a chromosome is to the optimal fitness, the more likely it is that mutating a bit further to the right will increase the fitness the most
    * Therefore, it is more likely that chromosomes with the optimal fitness will be found close to other highly-fit chromosomes
"""

def Get_Binary_Value_Of_Rubiks_Cube_Face_Turn(face_turn):
    binary = ""
    face_turns = rubiks_cube.Get_Rubiks_Cube_Face_Turn_List()
    for turn in face_turns:
        if turn == face_turn:
            bit_value = "1"
        else:
            bit_value = "0"
        binary = binary + bit_value
    
    return binary

def Get_Rubiks_Cube_Face_Turn_From_Binary(binary):
    face_turn = ""
    face_turns = rubiks_cube.Get_Rubiks_Cube_Face_Turn_List()
    face_turn_index = list(binary).index("1")
    
    face_turn = face_turns[face_turn_index]
    
    return face_turn

def Get_Face_Turns_Executed_List_From_Binary(binary):
    face_turns_executed_list = []
    face_turns = rubiks_cube.Get_Rubiks_Cube_Face_Turn_List()
    face_turn_binary_length = len(face_turns)
    
    binary_index = 0
    while binary_index + face_turn_binary_length < len(binary):
        face_turn_executed = Get_Rubiks_Cube_Face_Turn_From_Binary(binary[binary_index:binary_index + face_turn_binary_length])
        face_turns_executed_list.append(face_turn_executed)
        binary_index = binary_index + face_turn_binary_length
    
    return face_turns_executed_list

def Get_Binary_Value_Of_Rubiks_Cube_Turns_Executed(cube_turns_executed_list):
    binary = ""
    for cube_turn_executed in cube_turns_executed_list:
        binary = binary + Get_Binary_Value_Of_Rubiks_Cube_Face_Turn(cube_turn_executed)
    return binary

def Get_Crossover_Chromosomes(first_chromosome, second_chromosome, cutoff):
    crossover_chromosomes = []
    first_crossover = ""
    second_crossover = ""
    if len(first_chromosome) == len(second_chromosome):
        first_crossover = second_chromosome[0:cutoff] + first_chromosome[cutoff:len(first_chromosome)]
        second_crossover = first_chromosome[0:cutoff] + second_chromsome[cutoff:len(second_chromosome)]
        crossover_chromosomes = [first_crossover, second_crossover]
    else:
        raise ValueError("The length of the first chromosome must be equal to the length of the second chromosome in order to crossover!")
    
    return crossover_chromosomes

def Get_Mutated_Chromosome(chromosome):
    mutated_chromosome = ""
    chromosome_array = list(chromosome)
    random.shuffle(chromosome_array)
    mutated_chromosome = "".join(chromosome_array)
    
    return mutated_chromosome

def Get_Rubiks_Cube_Chromosome(cube_turns_executed_list):
    rubiks_cube_chromosome = ""
    rubiks_cube_face_turns_list = rubiks_cube.Get_Rubiks_Cube_Face_Turn_List()
    
    for cube_turn_executed in cube_turns_executed_list:
        cube_turn_binary_value = bin(rubiks_cube_turns_list.index(cube_turn_executed))[2:]
        rubiks_cube_chromosome = rubiks_cube_chromosome + cube_turn_binary_value
    
    return rubiks_cube_chromosome

def Get_Rubiks_Cube_Chromosome_Fitness(rubiks_cube_chromosome, cube):
    rubiks_cube_chromosome_fitness = None
    cube_turns_executed_list = Get_Face_Turns_Executed_List_From_Binary(rubiks_cube_chromosome)
    cube_with_turns_executed = rubiks_cube.Get_Cube_With_Turns_Executed(cube, cube_turns_executed_list)
    
    rubiks_cube_chromosome_fitness = Get_Rubiks_Cube_Fitness(cube_with_turns_executed)
    
    return rubiks_cube_chromosome_fitness

def Get_Rubiks_Cube_Fitness(cube):
    rubiks_cube_fitness = None
    
    
    return rubiks_cube_fitness

def Trace_Rubiks_Cube_Genetic_Algorithm():
    default_cube = rubiks_cube.Get_Default_Cube()
    scrambled_cube = rubiks_cube.Get_Scrambled_Cube(default_cube, num_turns = 20)
    rubiks_cube.Print_Cube(scrambled_cube["CUBE"])
import rubiks_cube
import time

#Function makes the cube array into a string array
def Get_Cube_Array_As_String_Array(cube_array):
    string_array = []
    #gets into the cube array and uses the function to get the string array
    for cube in cube_array:
        cube_string = rubiks_cube.Get_String_From_Cube(cube)
        string_array.append(cube_string)
    
    return string_array

#Function checks if the cubes are the same
def Get_If_Rubiks_Cubes_Equivalent(first_cube, second_cube):
    rubiks_cubes_equivalent = False #starts off as false to be compared and determined if true
    #assigning and calling functions of the first cube and the second cube
    first_cube_string_format = rubiks_cube.Get_String_From_Cube(first_cube)
    second_cube_string_format = rubiks_cube.Get_String_From_Cube(second_cube)
    
    #comparing each cube to determine if they are the same
    if first_cube_string_format == second_cube_string_format:
        rubiks_cubes_equivalent = True
    
    return rubiks_cubes_equivalent

#Function gets a new cube from a searching the turn lists, scrambled and default cubes
def Get_New_Rubiks_Cube_Search_Tree(scrambled_cube_with_turns_executed = None):
    cube_search_tree = {}
    default_cube = rubiks_cube.Get_Default_Cube()
    if scrambled_cube_with_turns_executed == None:
        scrambled_cube_with_turns_executed = rubiks_cube.Get_Scrambled_Cube(default_cube.copy(), 2)
    scrambled_cube = scrambled_cube_with_turns_executed["CUBE"]
    scramble_turns = scrambled_cube_with_turns_executed["TURNS_EXECUTED"]
    turn_options = rubiks_cube.Get_Rubiks_Cube_Turns_List()
    
    #assigning each variable to a state or cube
    cube_search_tree = {"CURRENT_CUBE" : scrambled_cube.copy(),
                        "ROOT_CUBE" : scrambled_cube.copy(),
                        "ROOT_CUBE_TURNS_EXECUTED" : scramble_turns,
                        "GOAL_CUBE" : default_cube.copy(),
                        "TURN_OPTIONS" : turn_options.copy(),
                        "OPEN_STATES" : [],
                        "CLOSED_STATES" : [],
                        "PATH_COST" : 0}
    
    return cube_search_tree

def Get_Default_Rubiks_Cube_Search_Tree():
    cube_search_tree = {}
    default_cube = rubiks_cube.Get_Default_Cube()
    turn_options = rubiks_cube.Get_Rubiks_Cube_Turns_List()
    
    cube_search_tree = {"CURRENT_CUBE" : default_cube.copy(),
                        "ROOT_CUBE" : default_cube.copy(),
                        "GOAL_CUBE" : None,
                        "TURN_OPTIONS" : turn_options.copy(),
                        "OPEN_STATES" : [],
                        "CLOSED_STATES" : [],
                        "PATH_COST" : 0}
    
    return cube_search_tree

def Get_If_Rubiks_Cube_Search_Trees_Intersect(first_search_tree, second_search_tree):
    trees_intersect = False
    
    first_search_tree_current_state = rubiks_cube.Get_String_From_Cube(first_search_tree["CURRENT_CUBE"])
    second_search_tree_visited_states = second_search_tree["OPEN_STATES"] + second_search_tree["CLOSED_STATES"] + [rubiks_cube.Get_String_From_Cube(second_search_tree["CURRENT_CUBE"])]
    
    if first_search_tree_current_state in second_search_tree_visited_states:
        trees_intersect = True
    
    return trees_intersect

#Functions uses the search tree to get the children of the current cube
def Get_Children_Of_Current_Cube(cube_search_tree):
    children = []
    parent = cube_search_tree["CURRENT_CUBE"].copy()
    turn_options = cube_search_tree["TURN_OPTIONS"]
    for turn_option in turn_options:
        child = rubiks_cube.Get_String_From_Cube(rubiks_cube.Get_Rotated_Cube_Using_Notation(parent.copy(), turn_option))
        if child not in cube_search_tree["CLOSED_STATES"] and child not in cube_search_tree["OPEN_STATES"]:
            children.append(child)
    
    return children

def Get_Updated_Cube_Depth_First_Search_Tree(cube_search_tree):
    updated_cube_search_tree = cube_search_tree
    
    updated_cube_search_tree["OPEN_STATES"] = updated_cube_search_tree["OPEN_STATES"] + Get_Children_Of_Current_Cube(updated_cube_search_tree)
    updated_cube_search_tree["CLOSED_STATES"].append(rubiks_cube.Get_String_From_Cube(updated_cube_search_tree["CURRENT_CUBE"]))
    updated_cube_search_tree["CURRENT_CUBE"] = rubiks_cube.Get_Cube_From_String(updated_cube_search_tree["OPEN_STATES"].pop(-1))
    updated_cube_search_tree["PATH_COST"] = updated_cube_search_tree["PATH_COST"] + 1
    
    return updated_cube_search_tree

#Functions updates the cube using breadth first search
def Get_Updated_Cube_Breadth_First_Search_Tree(cube_search_tree):
    updated_cube_search_tree = cube_search_tree
    
    updated_cube_search_tree["OPEN_STATES"] = updated_cube_search_tree["OPEN_STATES"] + Get_Children_Of_Current_Cube(updated_cube_search_tree)
    updated_cube_search_tree["CLOSED_STATES"].append(rubiks_cube.Get_String_From_Cube(updated_cube_search_tree["CURRENT_CUBE"]))
    updated_cube_search_tree["CURRENT_CUBE"] = rubiks_cube.Get_Cube_From_String(updated_cube_search_tree["OPEN_STATES"].pop(0))
    updated_cube_search_tree["PATH_COST"] = updated_cube_search_tree["PATH_COST"] + 1
    
    return updated_cube_search_tree

def Get_Updated_Cube_Bidirectional_Search_Tree(scrambled_cube_search_tree, default_cube_search_tree):
    updated_scrambled_cube_search_tree = scrambled_cube_search_tree
    updated_default_cube_search_tree = default_cube_search_tree
    
    updated_scrambled_cube_search_tree = Get_Updated_Cube_Breadth_First_Search_Tree(updated_scrambled_cube_search_tree.copy())
    updated_default_cube_search_tree = Get_Updated_Cube_Breadth_First_Search_Tree(updated_default_cube_search_tree.copy())
    
    return updated_scrambled_cube_search_tree, updated_default_cube_search_tree

#Function traces the cube through breadth first search
def Trace_Rubiks_Cube_Depth_First_Search(scrambled_cube_with_turns_executed = None):
    print("Depth First Search:")
    start_time = time.time()
    cube_search_tree = Get_New_Rubiks_Cube_Search_Tree(scrambled_cube_with_turns_executed)
    while Get_If_Rubiks_Cubes_Equivalent(cube_search_tree["CURRENT_CUBE"], cube_search_tree["GOAL_CUBE"]) != True:
        cube_search_tree = Get_Updated_Cube_Depth_First_Search_Tree(cube_search_tree.copy())
    end_time = time.time()
    rubiks_cube.Print_Cube(cube_search_tree["ROOT_CUBE"])
    print("\n")
    print("Turns Used to Scramble:\t" + str(cube_search_tree["ROOT_CUBE_TURNS_EXECUTED"]))
    print("\n")
    rubiks_cube.Print_Cube(cube_search_tree["CURRENT_CUBE"])
    print("\n")
    print("------------------------------")
    path_cost = str(cube_search_tree["PATH_COST"])
    print("Path Cost:\t" + path_cost)
    execution_time = str(end_time - start_time)
    print("Execution Time:\t" + execution_time)
    print("------------------------------")
    
    return path_cost, execution_time

def Trace_Rubiks_Cube_Breadth_First_Search(scrambled_cube_with_turns_executed = None):
    print("Breadth First Search:")
    start_time = time.time()
    cube_search_tree = Get_New_Rubiks_Cube_Search_Tree(scrambled_cube_with_turns_executed)
    while Get_If_Rubiks_Cubes_Equivalent(cube_search_tree["CURRENT_CUBE"], cube_search_tree["GOAL_CUBE"]) != True:
        cube_search_tree = Get_Updated_Cube_Breadth_First_Search_Tree(cube_search_tree.copy())
    end_time = time.time()
    rubiks_cube.Print_Cube(cube_search_tree["ROOT_CUBE"])
    print("\n")
    print("Turns Used to Scramble:\t" + str(cube_search_tree["ROOT_CUBE_TURNS_EXECUTED"]))
    print("\n")
    rubiks_cube.Print_Cube(cube_search_tree["CURRENT_CUBE"])
    print("\n")
    print("------------------------------")
    path_cost = str(cube_search_tree["PATH_COST"])
    print("Path Cost:\t" + path_cost)
    execution_time = str(end_time - start_time)
    print("Execution Time:\t" + execution_time)
    print("------------------------------")
    
    return path_cost, execution_time

def Trace_Rubiks_Cube_Bidirectional_Search(scrambled_cube_with_turns_executed = None):
    print("Bidirectional Search:")
    start_time = time.time()
    scrambled_cube_search_tree = Get_New_Rubiks_Cube_Search_Tree(scrambled_cube_with_turns_executed)
    default_cube_search_tree = Get_Default_Rubiks_Cube_Search_Tree()
    default_cube_search_tree["GOAL_STATE"] = scrambled_cube_search_tree["ROOT_CUBE"]
    while Get_If_Rubiks_Cube_Search_Trees_Intersect(scrambled_cube_search_tree, default_cube_search_tree) != True:
        scrambled_cube_search_tree, default_cube_search_tree = Get_Updated_Cube_Bidirectional_Search_Tree(scrambled_cube_search_tree.copy(), default_cube_search_tree.copy())
    end_time = time.time()
    rubiks_cube.Print_Cube(scrambled_cube_search_tree["ROOT_CUBE"])
    print("\n")
    print("Turns Used to Scramble:\t" + str(scrambled_cube_search_tree["ROOT_CUBE_TURNS_EXECUTED"]))
    print("\n")
    print("Search Convergence Cube:\n")
    rubiks_cube.Print_Cube(scrambled_cube_search_tree["CURRENT_CUBE"])
    print("\n")
    print("------------------------------")
    path_cost = str(scrambled_cube_search_tree["PATH_COST"] + default_cube_search_tree["PATH_COST"])
    print("Path Cost:\t" + path_cost)
    execution_time = str(end_time - start_time)
    print("Execution Time:\t" + execution_time)
    print("------------------------------")
    
    return path_cost, execution_time

def Trace_Performance_Comparison_Search_Algorithms():
    default_cube = rubiks_cube.Get_Default_Cube()
    scrambled_cube_with_turns_executed = rubiks_cube.Get_Scrambled_Cube(default_cube.copy(), 1)
    bfs_path_cost, bfs_execution_time = Trace_Rubiks_Cube_Breadth_First_Search(scrambled_cube_with_turns_executed.copy())
    bis_path_cost, bis_execution_time = Trace_Rubiks_Cube_Bidirectional_Search(scrambled_cube_with_turns_executed.copy())
    dfs_path_cost, dfs_execution_time = Trace_Rubiks_Cube_Depth_First_Search(scrambled_cube_with_turns_executed.copy())

Trace_Performance_Comparison_Search_Algorithms()
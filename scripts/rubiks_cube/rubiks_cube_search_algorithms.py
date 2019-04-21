import rubiks_cube

def Get_String_From_Cube(cube):
    string = ""
    for side in cube:
        for row in cube[side]:
            for block in row:
                string = string + block
    
    return string

def Get_Cube_Array_As_String_Array(cube_array):
    string_array = []
    for cube in cube_array:
        cube_string = Get_String_From_Cube(cube)
        string_array.append(cube_string)
    
    return string_array

def Get_If_Rubiks_Cubes_Equivalent(first_cube, second_cube):
    rubiks_cubes_equivalent = False
    first_cube_string_format = Get_String_From_Cube(first_cube)
    second_cube_string_format = Get_String_From_Cube(second_cube)
    
    if first_cube_string_format == second_cube_string_format:
        rubiks_cubes_equivalent = True
    
    return rubiks_cubes_equivalent

def Get_New_Rubiks_Cube_Search_Tree():
    cube_search_tree = {}
    default_cube = rubiks_cube.Get_Default_Cube()
    scrambled_cube = rubiks_cube.Get_Scrambled_Cube(default_cube.copy(), 1)["CUBE"]
    
    cube_search_tree = {"CURRENT_CUBE" : scrambled_cube.copy(),
                        "ROOT_CUBE" : scrambled_cube.copy(),
                        "GOAL_CUBE" : default_cube.copy(),
                        "TURN_OPTIONS" : rubiks_cube.Get_Rubiks_Cube_Turns_List(),
                        "OPEN_STATES" : [],
                        "CLOSED_STATES" : [],
                        "FINAL_PATH" : [],
                        "PATH_COST" : 0}
    
    return cube_search_tree

def Get_Children_Of_Current_Cube(cube_search_tree):
    children = []
    parent = cube_search_tree["CURRENT_CUBE"].copy()
    turn_options = cube_search_tree["TURN_OPTIONS"]
    for turn_option in turn_options:
        child = rubiks_cube.Get_Rotated_Cube_Using_Notation(parent.copy(), turn_option)
        children.append(child)
    
    return children

def Get_Updated_Cube_Breadth_First_Search_Tree(cube_search_tree):
    updated_cube_search_tree = cube_search_tree.copy()
    
    updated_cube_search_tree["CLOSED_STATES"].append(updated_cube_search_tree["CURRENT_CUBE"])
    
    updated_cube_search_tree["OPEN_STATES"] = updated_cube_search_tree["OPEN_STATES"] + Get_Children_Of_Current_Cube(updated_cube_search_tree)
    updated_cube_search_tree["CURRENT_CUBE"] = updated_cube_search_tree["OPEN_STATES"].pop(0)
    
    return updated_cube_search_tree

def Trace_Rubiks_Cube_Breadth_First_Search():
    cube_search_tree = Get_New_Rubiks_Cube_Search_Tree().copy()
    while Get_If_Rubiks_Cubes_Equivalent(cube_search_tree["CURRENT_CUBE"], cube_search_tree["GOAL_CUBE"]) != True:
        cube_search_tree = Get_Updated_Cube_Breadth_First_Search_Tree(cube_search_tree).copy()
    print(rubiks_cube.Print_Cube(cube_search_tree["ROOT_CUBE"]))
    print(rubiks_cube.Print_Cube(cube_search_tree["CURRENT_CUBE"]))
    print("------------------------------")
    print("Final Path: " + str(cube_search_tree["FINAL_PATH"]))
    print("Path Cost: " + str(cube_search_tree["PATH_COST"]))
def Get_Default_Cube():
    default_cube = {"TOP" : None,
                    "BOTTOM" : None,
                    "LEFT" : None,
                    "RIGHT" : None,
                    "FRONT" : None,
                    "BACK" : None}
    default_cube_colors = Get_Default_Cube_Colors()
    default_cube_color_index = 0
    
    for cube_side in default_cube.keys():
        default_cube[cube_side] = Get_Colored_Cube_Side(default_cube_colors[default_cube_color_index])
        default_cube_color_index = default_cube_color_index + 1
        
    return default_cube

def Print_Cube_Side(cube_side, cube):
    cube_sides = cube.keys()
    if cube_side not in cube_sides:
        raise IndexError("Cube side given (" + cube_side + ") does not exist in cube! Valid cube sides are " + cube_sides + ".")
    else:
        if isinstance(cube_side, list):
            for row in cube[cube_side]:
                print("".join(row))
        elif isinstance(cube_side, str):
            print(cube_side)

def Get_Default_Cube_Colors():
    default_colors = []
    color = {"NAME" : None,
             "STR_ID" : None,
             "INT_ID" : None}
    color_names = ["WHITE", "BLUE", "ORANGE", "RED", "GREEN", "YELLOW"]
    color_index = 0
    for color_name in color_names:
        color = {"NAME" : color_name,
                 "STR_ID" : color_name[0].upper(),
                 "INT_ID" : color_index}
        default_colors.append(color)
        color_index = color_index + 1
        
    return default_colors

def Get_Blank_Cube_Side():
    blank_cube_side = """[][][]
                         [][][]
                         [][][]"""
    
    return blank_cube_side

def Get_Colored_Cube_Side(color):
    colored_cube_side = []
    colored_cube_side_table = []
    blank_cube_side = Get_Blank_Cube_Side()
    blank_cube_side_table = Get_Cube_Side_Table(blank_cube_side)
    for blank_cube_row in blank_cube_side_table:
        colored_cube_row = []
        for blank_cube_block in blank_cube_row:
            colored_cube_block = blank_cube_block.replace("[]", str("[" + color["STR_ID"] + "]"))
            colored_cube_row.append(colored_cube_block)
        colored_cube_side_table.append(colored_cube_row)
    colored_cube_side = colored_cube_side_table
    
    return colored_cube_side

def Get_Blank_Cube():
    blank_cube = {"TOP" : None,
                  "BOTTOM" : None,
                  "LEFT" : None,
                  "RIGHT" : None,
                  "FRONT" : None,
                  "BACK" : None}
    blank_cube_side = Get_Blank_Cube_Side()
    for cube_side in blank_cube:
        blank_cube[cube_side] = blank_cube_side
    
    return blank_cube

def Get_Cube_Side_Table(cube_side):
    cube_side_table = []
    cube_side_rows = cube_side.split("\n")
    for cube_side_row in cube_side_rows:
        cube_side_row = cube_side_row.replace(" ", "")
        cube_side_row = cube_side_row.replace("][", "],[")
        cube_side_row = cube_side_row.split(",")
        cube_side_table.append(cube_side_row)
    
    return cube_side_table

def Is_Cube_Completed(cube):
    is_cube_completed = True
    for cube_side in cube:
        for cube_row in cube[cube_side]:
            for cube_block in cube_row:
                if cube_block != cube_row[0]:
                    is_cube_completed = False
                    break
    
    return is_cube_completed

def Print_Invalid_Parameters_Message():
    print("Invalid parameters entered!")

def Get_Cube_In_Perspective(cube, perspective):
    cube_in_perspective = Get_Blank_Cube()
    perspectives = ["TOP", "BOTTOM", "LEFT", "RIGHT", "FRONT", "BACK"]
    if perspective.upper() in perspectives:
        if perspective.upper() == "TOP":
            cube_in_perspective["TOP"] = cube["BACK"]
            cube_in_perspective["BOTTOM"] = cube["FRONT"]
            cube_in_perspective["LEFT"] = [[cube["LEFT"][2][0]] + [cube["LEFT"][1][0]] + [cube["LEFT"][0][0]],
                                           [cube["LEFT"][2][1]] + [cube["LEFT"][1][1]] + [cube["LEFT"][0][1]],
                                           [cube["LEFT"][2][2]] + [cube["LEFT"][1][2]] + [cube["LEFT"][0][2]]]
            cube_in_perspective["RIGHT"] = [[cube["RIGHT"][0][2]] + [cube["RIGHT"][1][2]] + [cube["RIGHT"][2][2]],
                                            [cube["RIGHT"][0][1]] + [cube["RIGHT"][1][1]] + [cube["RIGHT"][2][1]],
                                            [cube["RIGHT"][0][0]] + [cube["RIGHT"][1][0]] + [cube["RIGHT"][2][0]]]
            cube_in_perspective["FRONT"] = cube["TOP"]
            cube_in_perspective["BACK"] = [[cube["BOTTOM"][2][2]] + [cube["BOTTOM"][2][1]] + [cube["BOTTOM"][2][0]],
                                           [cube["BOTTOM"][1][2]] + [cube["BOTTOM"][1][1]] + [cube["BOTTOM"][1][0]],
                                           [cube["BOTTOM"][0][2]] + [cube["BOTTOM"][0][1]] + [cube["BOTTOM"][0][0]]]
        elif perspective.upper() == "BOTTOM":
            cube_in_perspective["TOP"] = cube["FRONT"]
            cube_in_perspective["BOTTOM"] = [[cube["BACK"][2][2]] + [cube["BACK"][2][1]] + [cube["BACK"][2][0]],
                                             [cube["BACK"][1][2]] + [cube["BACK"][1][1]] + [cube["BACK"][1][0]],
                                             [cube["BACK"][0][2]] + [cube["BACK"][0][1]] + [cube["BACK"][0][0]]]
            cube_in_perspective["LEFT"] = [[cube["LEFT"][0][2]] + [cube["LEFT"][1][2]] + [cube["LEFT"][2][2]],
                                           [cube["LEFT"][0][1]] + [cube["LEFT"][1][1]] + [cube["LEFT"][2][1]],
                                           [cube["LEFT"][0][0]] + [cube["LEFT"][1][0]] + [cube["LEFT"][2][0]]]
            cube_in_perspective["RIGHT"] = [[cube["RIGHT"][2][0]] + [cube["RIGHT"][1][0]] + [cube["RIGHT"][0][0]],
                                            [cube["RIGHT"][2][1]] + [cube["RIGHT"][1][1]] + [cube["RIGHT"][0][1]],
                                            [cube["RIGHT"][2][2]] + [cube["RIGHT"][1][2]] + [cube["RIGHT"][0][2]]]
            cube_in_perspective["FRONT"] = cube["BOTTOM"]
            cube_in_perspective["BACK"] = [[cube["TOP"][2][2]] + [cube["TOP"][2][1]] + [cube["TOP"][2][0]],
                                           [cube["TOP"][1][2]] + [cube["TOP"][1][1]] + [cube["TOP"][1][0]],
                                           [cube["TOP"][0][2]] + [cube["TOP"][0][1]] + [cube["TOP"][0][0]]]
        elif perspective.upper() == "LEFT":
            cube_in_perspective["TOP"] = [[cube["TOP"][0][2]] + [cube["TOP"][1][2]] + [cube["TOP"][2][2]],
                                          [cube["TOP"][0][1]] + [cube["TOP"][1][1]] + [cube["TOP"][2][1]],
                                          [cube["TOP"][0][0]] + [cube["TOP"][1][0]] + [cube["TOP"][2][0]]]
            cube_in_perspective["BOTTOM"] = [[cube["BOTTOM"][2][0]] + [cube["BOTTOM"][1][0]] + [cube["BOTTOM"][0][0]],
                                             [cube["BOTTOM"][2][1]] + [cube["BOTTOM"][1][1]] + [cube["BOTTOM"][0][1]],
                                             [cube["BOTTOM"][2][2]] + [cube["BOTTOM"][1][2]] + [cube["BOTTOM"][0][2]]]
            cube_in_perspective["LEFT"] = cube["BACK"]
            cube_in_perspective["RIGHT"] = cube["FRONT"]
            cube_in_perspective["FRONT"] = cube["LEFT"]
            cube_in_perspective["BACK"] = cube["RIGHT"]
        elif perspective.upper() == "RIGHT":
            cube_in_perspective["TOP"] = [[cube["TOP"][2][0]] + [cube["TOP"][1][0]] + [cube["TOP"][0][0]],
                                          [cube["TOP"][2][1]] + [cube["TOP"][1][1]] + [cube["TOP"][0][1]],
                                          [cube["TOP"][2][2]] + [cube["TOP"][1][2]] + [cube["TOP"][0][2]]]
            cube_in_perspective["BOTTOM"] = [[cube["BOTTOM"][0][2]] + [cube["BOTTOM"][1][2]] + [cube["BOTTOM"][2][2]],
                                             [cube["BOTTOM"][0][1]] + [cube["BOTTOM"][1][1]] + [cube["BOTTOM"][2][1]],
                                             [cube["BOTTOM"][0][0]] + [cube["BOTTOM"][1][0]] + [cube["BOTTOM"][2][0]]]
            cube_in_perspective["LEFT"] = cube["FRONT"]
            cube_in_perspective["RIGHT"] = cube["BACK"]
            cube_in_perspective["FRONT"] = cube["RIGHT"]
            cube_in_perspective["BACK"] = cube["LEFT"]
        elif perspective.upper() == "FRONT":
            cube_in_perspective["TOP"] = cube["TOP"]
            cube_in_perspective["BOTTOM"] = cube["BOTTOM"]
            cube_in_perspective["LEFT"] = cube["LEFT"]
            cube_in_perspective["RIGHT"] = cube["RIGHT"]
            cube_in_perspective["FRONT"] = cube["FRONT"]
            cube_in_perspective["BACK"] = cube["BACK"]
        elif perspective.upper() == "BACK":
            cube_in_perspective["TOP"] = [[cube["TOP"][2][2]] + [cube["TOP"][2][1]] + [cube["TOP"][2][0]],
                                          [cube["TOP"][1][2]] + [cube["TOP"][1][1]] + [cube["TOP"][1][0]],
                                          [cube["TOP"][0][2]] + [cube["TOP"][0][1]] + [cube["TOP"][0][0]]]
            cube_in_perspective["BOTTOM"] = [[cube["BOTTOM"][2][2]] + [cube["BOTTOM"][2][1]] + [cube["BOTTOM"][2][0]],
                                             [cube["BOTTOM"][1][2]] + [cube["BOTTOM"][1][1]] + [cube["BOTTOM"][1][0]],
                                             [cube["BOTTOM"][0][2]] + [cube["BOTTOM"][0][1]] + [cube["BOTTOM"][0][0]]]
            cube_in_perspective["LEFT"] = cube["RIGHT"]
            cube_in_perspective["RIGHT"] = cube["LEFT"]
            cube_in_perspective["FRONT"] = cube["BACK"]
            cube_in_perspective["BACK"] = cube["FRONT"]
    else:
        Print_Invalid_Parameters_Message()
    
    return cube_in_perspective

## Assumes that the cube is a dictionary, with each key being a cube side, and with each value in the dictionary being an array of rows, and with each row containing an array of blocks
def Get_Rotated_Cube(cube, what_to_rotate, what_to_rotate_index, rotation_direction, rotation_perspective):
    rotated_cube = cube
    
    rotation_directions = []
    rotation_perspectives = ["TOP", "BOTTOM", "LEFT", "RIGHT", "FRONT", "BACK"]
    
    if what_to_rotate.upper() == "ROW":
        rotation_directions = ["LEFT", "RIGHT"]
    elif what_to_rotate.upper() == "COLUMN":
        rotation_directions = ["UP", "DOWN"]
        
    if rotation_direction.upper() in rotation_directions:
        cube = Get_Cube_In_Perspective(cube, rotation_perspective)
        if what_to_rotate.upper() == "ROW":
            if rotation_direction.upper() == "LEFT":
                if what_to_rotate_index == 0:
                    rotated_cube["TOP"] = [[cube["TOP"][2][0]] + [cube["TOP"][1][0]] + [cube["TOP"][0][0]],
                                           [cube["TOP"][2][1]] + [cube["TOP"][1][1]] + [cube["TOP"][0][1]],
                                           [cube["TOP"][2][2]] + [cube["TOP"][1][2]] + [cube["TOP"][0][2]]]
                    rotated_cube["BOTTOM"] = cube["BOTTOM"]
                    rotated_cube["LEFT"] = [cube["FRONT"][0]] + cube["LEFT"][1:]
                    rotated_cube["RIGHT"] = [cube["BACK"][0]] + cube["RIGHT"][1:]
                    rotated_cube["FRONT"] = [cube["RIGHT"][0]] + cube["FRONT"][1:]
                    rotated_cube["BACK"] = [cube["LEFT"][0]] + cube["BACK"][1:]
                elif what_to_rotate_index == 1:
                    rotated_cube["TOP"] = cube["TOP"]
                    rotated_cube["BOTTOM"] = cube["BOTTOM"]
                    rotated_cube["LEFT"] = [cube["LEFT"][0]] + [cube["FRONT"][1]] + [cube["LEFT"][2]]
                    rotated_cube["RIGHT"] = [cube["RIGHT"][0]] + [cube["BACK"][1]] + [cube["RIGHT"][2]]
                    rotated_cube["FRONT"] = [cube["FRONT"][0]] + [cube["RIGHT"][1]] + [cube["FRONT"][2]]
                    rotated_cube["BACK"] = [cube["BACK"][0]] + [cube["LEFT"][1]] + [cube["BACK"][2]]
                elif what_to_rotate_index == 2:
                    rotated_cube["TOP"] = cube["TOP"]
                    rotated_cube["BOTTOM"] = [[cube["BOTTOM"][0][2]] + [cube["BOTTOM"][1][2]] + [cube["BOTTOM"][2][2]],
                                              [cube["BOTTOM"][0][1]] + [cube["BOTTOM"][1][1]] + [cube["BOTTOM"][2][1]],
                                              [cube["BOTTOM"][0][0]] + [cube["BOTTOM"][1][0]] + [cube["BOTTOM"][2][0]]]
                    rotated_cube["LEFT"] = cube["LEFT"][:-1] + [cube["FRONT"][2]]
                    rotated_cube["RIGHT"] = cube["RIGHT"][:-1] + [cube["BACK"][2]]
                    rotated_cube["FRONT"] = cube["FRONT"][:-1] + [cube["RIGHT"][2]]
                    rotated_cube["BACK"] = cube["BACK"][:-1] + [cube["LEFT"][2]]
                    
            elif rotation_direction.upper() == "RIGHT":
                if what_to_rotate_index == 0:
                    rotated_cube["TOP"] = [[cube["TOP"][0][2]] + [cube["TOP"][1][2]] + [cube["TOP"][2][2]],
                                           [cube["TOP"][0][1]] + [cube["TOP"][1][1]] + [cube["TOP"][2][1]],
                                           [cube["TOP"][0][0]] + [cube["TOP"][1][0]] + [cube["TOP"][2][0]]]
                    rotated_cube["BOTTOM"] = cube["BOTTOM"]
                    rotated_cube["LEFT"] = [cube["BACK"][0]] + cube["LEFT"][1:]
                    rotated_cube["RIGHT"] = [cube["FRONT"][0]] + cube["RIGHT"][1:]
                    rotated_cube["FRONT"] = [cube["LEFT"][0]] + cube["FRONT"][1:]
                    rotated_cube["BACK"] = [cube["RIGHT"][0]] + cube["BACK"][1:]
                elif what_to_rotate_index == 1:
                    rotated_cube["TOP"] = cube["TOP"]
                    rotated_cube["BOTTOM"] = cube["BOTTOM"]
                    rotated_cube["LEFT"] = [cube["LEFT"][0]] + [cube["BACK"][1]] + [cube["LEFT"][2]]
                    rotated_cube["RIGHT"] = [cube["RIGHT"][0]] + [cube["FRONT"][1]] + [cube["RIGHT"][2]]
                    rotated_cube["FRONT"] = [cube["FRONT"][0]] + [cube["LEFT"][1]] + [cube["FRONT"][2]]
                    rotated_cube["BACK"] = [cube["BACK"][0]] + [cube["RIGHT"][1]] + [cube["BACK"][2]]
                elif what_to_rotate_index == 2:
                    rotated_cube["TOP"] = cube["TOP"]
                    rotated_cube["BOTTOM"] = [[cube["BOTTOM"][2][0]] + [cube["BOTTOM"][1][0]] + [cube["BOTTOM"][0][0]],
                                              [cube["BOTTOM"][2][1]] + [cube["BOTTOM"][1][1]] + [cube["BOTTOM"][0][1]],
                                              [cube["BOTTOM"][2][2]] + [cube["BOTTOM"][1][2]] + [cube["BOTTOM"][0][2]]]
                    rotated_cube["LEFT"] = cube["LEFT"][:-1] + [cube["BACK"][2]]
                    rotated_cube["RIGHT"] = cube["RIGHT"][:-1] + [cube["FRONT"][2]]
                    rotated_cube["FRONT"] = cube["FRONT"][:-1] + [cube["LEFT"][2]]
                    rotated_cube["BACK"] = cube["BACK"][:-1] + [cube["RIGHT"][2]]
                
        elif what_to_rotate.upper() == "COLUMN":
            if rotation_direction.upper() == "UP":
                if what_to_rotate_index == 0:
                    rotated_cube["TOP"] = [[cube["FRONT"][0][0]] + cube["TOP"][0][1:], 
                                           [cube["FRONT"][1][0]] + cube["TOP"][1][1:],
                                           [cube["FRONT"][2][0]] + cube["TOP"][2][1:]]
                    rotated_cube["BOTTOM"] = [[cube["BACK"][0][0]] + cube["BOTTOM"][0][1:],
                                              [cube["BACK"][1][0]] + cube["BOTTOM"][1][1:],
                                              [cube["BACK"][2][0]] + cube["BOTTOM"][2][1:]]
                    rotated_cube["LEFT"] = [[cube["LEFT"][0][2]] + [cube["LEFT"][1][2]] + [cube["LEFT"][2][2]],
                                            [cube["LEFT"][0][1]] + [cube["LEFT"][1][1]] + [cube["LEFT"][2][1]],
                                            [cube["LEFT"][0][0]] + [cube["LEFT"][1][0]] + [cube["LEFT"][2][0]]]
                    rotated_cube["RIGHT"] = cube["RIGHT"]
                    rotated_cube["FRONT"] = [[cube["BOTTOM"][0][0]] + cube["FRONT"][0][1:],
                                             [cube["BOTTOM"][1][0]] + cube["FRONT"][1][1:],
                                             [cube["BOTTOM"][2][0]] + cube["FRONT"][2][1:]]
                    rotated_cube["BACK"] = [[cube["TOP"][0][0]] + cube["BACK"][0][1:],
                                            [cube["TOP"][1][0]] + cube["BACK"][1][1:], 
                                            [cube["TOP"][2][0]] + cube["BACK"][2][1:]]
                elif what_to_rotate_index == 1:
                    rotated_cube["TOP"] = [[cube["TOP"][0][0]] + [cube["FRONT"][0][1]] + [cube["TOP"][0][2]],
                                           [cube["TOP"][1][0]] + [cube["FRONT"][1][1]] + [cube["TOP"][1][2]],
                                           [cube["TOP"][2][0]] + [cube["FRONT"][2][1]] + [cube["TOP"][2][2]]]
                    rotated_cube["BOTTOM"] = [[cube["BOTTOM"][0][0]] + [cube["BACK"][0][1]] + [cube["BOTTOM"][0][2]],
                                              [cube["BOTTOM"][1][0]] + [cube["BACK"][1][1]] + [cube["BOTTOM"][1][2]],
                                              [cube["BOTTOM"][2][0]] + [cube["BACK"][2][1]] + [cube["BOTTOM"][2][2]]]
                    rotated_cube["LEFT"] = cube["LEFT"]
                    rotated_cube["RIGHT"] = cube["RIGHT"]
                    rotated_cube["FRONT"] = [[cube["FRONT"][0][0]] + [cube["BOTTOM"][0][1]] + [cube["FRONT"][0][2]],
                                             [cube["FRONT"][1][0]] + [cube["BOTTOM"][1][1]] + [cube["FRONT"][1][2]],
                                             [cube["FRONT"][2][0]] + [cube["BOTTOM"][2][1]] + [cube["FRONT"][2][2]]]
                    rotated_cube["BACK"] = [[cube["BACK"][0][0]] + [cube["TOP"][0][1]] + [cube["BACK"][0][2]],
                                            [cube["BACK"][1][0]] + [cube["TOP"][1][1]] + [cube["BACK"][1][2]],
                                            [cube["BACK"][2][0]] + [cube["TOP"][2][1]] + [cube["BACK"][2][2]]]
                elif what_to_rotate_index == 2:
                    rotated_cube["TOP"] = [cube["TOP"][0][:-1] + cube["FRONT"][0][2],
                                           cube["TOP"][1][:-1] + cube["FRONT"][1][2],
                                           cube["TOP"][2][:-1] + cube["FRONT"][2][2]]
                    rotated_cube["BOTTOM"] = [cube["BOTTOM"][0][:-1] + cube["BACK"][0][2],
                                              cube["BOTTOM"][1][:-1] + cube["BACK"][1][2],
                                              cube["BOTTOM"][2][:-1] + cube["BACK"][2][2]]
                    rotated_cube["LEFT"] = cube["LEFT"]
                    rotated_cube["RIGHT"] = [[cube["RIGHT"][2][0]] + [cube["RIGHT"][1][0]] + [cube["RIGHT"][0][0]],
                                             [cube["RIGHT"][2][1]] + [cube["RIGHT"][1][1]] + [cube["RIGHT"][0][1]],
                                             [cube["RIGHT"][2][2]] + [cube["RIGHT"][1][2]] + [cube["RIGHT"][0][2]]]
                    rotated_cube["FRONT"] = [cube["FRONT"][0][:-1] + cube["BOTTOM"][0][2],
                                             cube["FRONT"][1][:-1] + cube["BOTTOM"][1][2],
                                             cube["FRONT"][2][:-1] + cube["BOTTOM"][2][2]]
                    rotated_cube["BACK"] = [cube["BACK"][0][:-1] + cube["TOP"][0][2],
                                            cube["BACK"][1][:-1] + cube["TOP"][1][2],
                                            cube["BACK"][2][:-1] + cube["TOP"][2][2]]
                
            elif rotation_direction.upper() == "DOWN":
                if what_to_rotate_index == 0:
                    rotated_cube["TOP"] = [[cube["BACK"][0][0]] + cube["TOP"][0][1:],
                                           [cube["BACK"][1][0]] + cube["TOP"][1][1:],
                                           [cube["BACK"][2][0]] + cube["TOP"][2][1:]]
                    rotated_cube["BOTTOM"] = [[cube["FRONT"][0][0]] + cube["BOTTOM"][0][1:],
                                              [cube["FRONT"][1][0]] + cube["BOTTOM"][1][1:],
                                              [cube["FRONT"][2][0]] + cube["BOTTOM"][2][1:]]
                    rotated_cube["LEFT"] = [[cube["LEFT"][2][0]] + [cube["LEFT"][1][0]] + [cube["LEFT"][0][0]],
                                            [cube["LEFT"][2][1]] + [cube["LEFT"][1][1]] + [cube["LEFT"][0][1]],
                                            [cube["LEFT"][2][2]] + [cube["LEFT"][1][2]] + [cube["LEFT"][0][2]]]
                    rotated_cube["RIGHT"] = cube["RIGHT"]
                    rotated_cube["FRONT"] = [[cube["TOP"][0][0]] + cube["FRONT"][0][1:],
                                             [cube["TOP"][1][0]] + cube["FRONT"][1][1:],
                                             [cube["TOP"][2][0]] + cube["FRONT"][2][1:]]
                    rotated_cube["BACK"] = [[cube["BOTTOM"][0][0]] + cube["BACK"][0][1:],
                                            [cube["BOTTOM"][1][0]] + cube["BACK"][1][1:],
                                            [cube["BOTTOM"][2][0]] + cube["BACK"][2][1:]]
                elif what_to_rotate_index == 1:
                    rotated_cube["TOP"] = [[cube["TOP"][0][0]] + [cube["BACK"][0][1]] + [cube["TOP"][0][2]],
                                           [cube["TOP"][1][0]] + [cube["BACK"][1][1]] + [cube["TOP"][1][2]],
                                           [cube["TOP"][2][0]] + [cube["BACK"][2][1]] + [cube["TOP"][2][2]]]
                    rotated_cube["BOTTOM"] = [[cube["BOTTOM"][0][0]] + [cube["FRONT"][0][1]] + [cube["BOTTOM"][0][2]],
                                              [cube["BOTTOM"][1][0]] + [cube["FRONT"][1][1]] + [cube["BOTTOM"][1][2]],
                                              [cube["BOTTOM"][2][0]] + [cube["FRONT"][2][1]] + [cube["BOTTOM"][2][2]]]
                    rotated_cube["LEFT"] = cube["LEFT"]
                    rotated_cube["RIGHT"] = cube["RIGHT"]
                    rotated_cube["FRONT"] = [[cube["FRONT"][0][0]] + [cube["TOP"][0][1]] + [cube["FRONT"][0][2]],
                                             [cube["FRONT"][1][0]] + [cube["TOP"][1][1]] + [cube["FRONT"][1][2]],
                                             [cube["FRONT"][2][0]] + [cube["TOP"][2][1]] + [cube["FRONT"][2][2]]]
                    rotated_cube["BACK"] = [[cube["BACK"][0][0]] + [cube["BOTTOM"][0][1]] + [cube["BACK"][0][2]],
                                            [cube["BACK"][1][0]] + [cube["BOTTOM"][1][1]] + [cube["BACK"][1][2]],
                                            [cube["BACK"][2][0]] + [cube["BOTTOM"][2][1]] + [cube["BACK"][2][2]]]
                elif what_to_rotate_index == 2:
                    rotated_cube["TOP"] = [cube["TOP"][0][:-1] + cube["BACK"][0][2],
                                           cube["TOP"][1][:-1] + cube["BACK"][1][2],
                                           cube["TOP"][2][:-1] + cube["BACK"][2][2]]
                    rotated_cube["BOTTOM"] = [cube["BOTTOM"][0][:-1] + cube["FRONT"][0][2],
                                              cube["BOTTOM"][1][:-1] + cube["FRONT"][1][2],
                                              cube["BOTTOM"][2][:-1] + cube["FRONT"][2][2]]
                    rotated_cube["LEFT"] = cube["LEFT"]
                    rotated_cube["RIGHT"] = [[cube["RIGHT"][0][2]] + [cube["RIGHT"][1][2]] + [cube["RIGHT"][2][2]],
                                             [cube["RIGHT"][0][1]] + [cube["RIGHT"][1][1]] + [cube["RIGHT"][2][1]],
                                             [cube["RIGHT"][0][0]] + [cube["RIGHT"][1][0]] + [cube["RIGHT"][2][0]]]
                    rotated_cube["FRONT"] = [cube["FRONT"][0][:-1] + cube["TOP"][0][2],
                                             cube["FRONT"][1][:-1] + cube["TOP"][1][2],
                                             cube["FRONT"][2][:-1] + cube["TOP"][2][2]]
                    rotated_cube["BACK"] = [cube["BACK"][0][:-1] + cube["BOTTOM"][0][2],
                                            cube["BACK"][1][:-1] + cube["BOTTOM"][1][2],
                                            cube["BACK"][2][:-1] + cube["BOTTOM"][2][2]]
    else:
        Print_Invalid_Parameters_Message()
    
    return rotated_cube

def Get_Rubiks_Cube_Turns_List():
    rubiks_cube_turns_list = []
    face_turn_list = ["U", "R", "F", "D", "L", "B"]
    double_layer_turn_list = ["u", "r", "f", "d", "l", "b"]
    middle_layer_turn_list = ["M", "E", "S"]
    
    for turn_list in [face_turn_list, double_layer_turn_list, middle_layer_turn_list]:
        for turn in turn_list:
            rubiks_cube_turns_list.append(turn)
            rubiks_cube_turns_list.append(turn + "2")
            rubiks_cube_turns_list.append(turn + "'")
            rubiks_cube_turns_list.append(turn + "2'")
            
    return rubiks_cube_turns_list

def Get_Rotated_Cube_Using_Notation(cube, move):
    rotated_cube = cube
    if move in Get_Rubiks_Cube_Turns_List():
        if move == "U":
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 0, "LEFT", "FRONT")
        elif move == "R":
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 2, "UP", "FRONT")
        elif move == "F":
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 2, "UP", "LEFT")
        elif move == "D":
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 2, "RIGHT", "FRONT")
        elif move == "L":
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 0, "DOWN", "FRONT")
        elif move == "B":
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 0, "LEFT", "TOP")
        
        elif move == "U'":
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 0, "RIGHT", "FRONT")
        elif move == "R'":
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 2, "DOWN", "FRONT")
        elif move == "F'":
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 2, "DOWN", "LEFT")
        elif move == "D'":
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 2, "LEFT", "FRONT")
        elif move == "L'":
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 0, "UP", "FRONT")
        elif move == "B'":
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 0, "RIGHT", "TOP")
        
        elif move == "u":
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 0, "LEFT", "FRONT")
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 1, "LEFT", "FRONT")
        elif move == "r":
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 2, "UP", "FRONT")
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 1, "UP", "FRONT")
        elif move == "f":
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 2, "UP", "LEFT")
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 1, "UP", "LEFT")
        elif move == "d":
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 2, "RIGHT", "FRONT")
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 1, "RIGHT", "FRONT")
        elif move == "l":
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 0, "DOWN", "FRONT")
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 1, "DOWN", "FRONT")
        elif move == "b":
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 0, "LEFT", "TOP")
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 1, "LEFT", "TOP")
        
        elif move == "u'":
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 0, "RIGHT", "FRONT")
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 1, "RIGHT", "FRONT")
        elif move == "r'":
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 2, "DOWN", "FRONT")
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 1, "DOWN", "FRONT")
        elif move == "f'":
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 2, "DOWN", "LEFT")
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 1, "DOWN", "LEFT")
        elif move == "d'":
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 2, "LEFT", "FRONT")
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 1, "LEFT", "FRONT")
        elif move == "l'":
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 0, "UP", "FRONT")
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 1, "UP", "FRONT")
        elif move == "b'":
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 0, "RIGHT", "TOP")
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 1, "RIGHT", "TOP")
        
        elif move == "M":
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 1, "DOWN", "FRONT")
        elif move == "M'":
            rotated_cube = Get_Rotated_Cube(cube, "COLUMN", 1, "UP", "FRONT")
        elif move == "E":
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 1, "RIGHT", "FRONT")
        elif move == "E'":
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 1, "LEFT", "FRONT")
        elif move == "S":
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 1, "RIGHT", "TOP")
        elif move == "S'":
            rotated_cube = Get_Rotated_Cube(cube, "ROW", 1, "LEFT", "TOP")
        
        elif move == "x":
            rotated_cube = Get_Cube_In_Perspective(cube, "BOTTOM")
        elif move == "x'":
            rotated_cube = Get_Cube_In_Perspective(cube, "TOP")
        elif move == "y":
            rotated_cube = Get_Cube_In_Perspective(cube, "RIGHT")
        elif move == "y":
            rotated_cube = Get_Cube_In_Perspective(cube, "LEFT")
        elif move == "z":
            rotated_cube = Get_Cube_In_Perspective(cube, "TOP")
            rotated_cube = Get_Cube_In_Perspective(rotated_cube, "LEFT")
            rotated_cube = Get_Cube_In_Perspective(rotated_cube, "BOTTOM")
        elif move == "z'":
            rotated_cube = Get_Cube_In_Perspective(cube, "TOP")
            rotated_cube = Get_Cube_In_Perspective(rotated_cube, "RIGHT")
            rotated_cube = Get_Cube_In_Perspective(rotated_cube, "BOTTOM")
        
        if "2" in move:
            move = move.replace("2", "")
            rotated_cube = Get_Rotated_Cube_Using_Notation(cube, move)
            rotated_cube = Get_Rotated_Cube_Using_Notation(rotated_cube, move)
    else:
        Print_Invalid_Parameters_Message()
    return rotated_cube
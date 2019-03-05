from idlelib import pyshell
from importlib import reload
from pathlib import Path
import os

Root_Directory = str(Path().absolute())
Scripts_Directory = Root_Directory + "\\" + "scripts"
     

def Add_Test_Directories_To_Path (Directories_To_Add = [Scripts_Directory]):
   for Directory_To_Add in Directories_To_Add:
      if Directory_To_Add is Scripts_Directory:
        for Script_Folder in os.listdir(Scripts_Directory):
          Script_Directory = Scripts_Directory + "\\" + Script_Folder
          pyshell.sys.path.append(Script_Directory)
      else:
         pyshell.sys.path.append(Directory_To_Add)

def Get_Setup_Choice (Setup_Option,
                      Input_Options = "Y, N"):

   Operator_Input = None
   Setup_Choice = None
   Input_Options = {"Y" : True,
                    "N" : False}
               
   if Input_Options is None:
      Operator_Input = raw_input(Setup_Option)
   else:
      if type(Input_Options) is str:
        Input_Options_String = Input_Options
        Input_Options = string_utilities.Get_String_As_List(Input_Options)
      else:
         Input_Options_String = string_utilities.Get_List_As_String(Input_Options)

   while Operator_Input.upper() not in Input_Options.keys():
        Operator_Input = raw_input(Setup_Option + " " + Input_Options_String)
        if Operator_Input not in Input_Options.keys():
           print("Input not recognized. Please enter one of the following values: " + Input_Options_String)
   
   Setup_Choice = Input_Options[Operator_Input.upper()]

   return Setup_Choice

def Startup():
   Add_Test_Directories_To_Path()
   pyshell.main()
   sys.stdout.shell.write("import m0 to execute scripts")
   
Startup()
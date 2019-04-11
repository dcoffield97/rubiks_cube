import binascii
import os
import rubiks_cube

def Get_New_Agent(agent_name):
	agent = {"NAME" : agent_name,
			 "PUBLIC_KEY" : Get_New_Key(),
			 "PRIVATE_KEY" : Get_New_Key()}
			 
	return agent
	
def Get_New_Agents(agent_names = ["Alice", "Bob"]):
	agents = []
	for agent_name in agent_names:
		agent = Get_New_Agent(agent_name)
		agents.append(agent)
	
	return agents

def Get_Random_Integer(num_bytes):
	random_integer = None
	random_integer = int.from_bytes(os.urandom(1), byteorder = "big")
	
	return random_integer

def Get_Random_Hex(num_bytes):
	random_hex = None
	random_hex = hex(Get_Random_Integer(num_bytes))[2:]
	
	return random_hex

def Get_Integer_From_Hex(hex):
	integer = None
	integer = int(hex, 16)
	
	return integer

def Get_Char_From_Hex(hex):
	char = ""
	char = chr(Get_Integer_From_Hex(hex))
	
	return char

def Get_Hex_From_Char(char):
	hex = ""
	hex = hex(ord(char))[2:]
	
	return hex

def Get_Hex_Array_From_String(string):
	hex_array = []
	for char in list(string):
		hex_array.append(Get_Hex_From_Char(char))
	
	return hex_array

def Get_Byte_Array_From_Hex(hex):
	byte_array = []
	hex_list = list(hex)
	hex_list_index = 0
	while hex_list_index+1 < len(hex_list):
		byte = hex_list[hex_list_index] + hex_list[hex_list_index+1]
		byte_array.append(byte)
		hex_list_index = hex_list_index + 2
	
	return byte_array

def Get_New_Key(num_bytes = 56):
	key = ""
	
	for byte in range(0, num_bytes):
		key = key + Get_Random_Hex(num_bytes)
	
	return key

def Get_Hex_Mapped_To_Cube(hex):
	cube = {"TOP" : None,
			"BOTTOM" : None,
			"LEFT" : None,
			"RIGHT" : None,
			"FRONT" : None,
			"BACK" : None}
	hex_byte_array = Get_Byte_Array_From_Hex(hex)
	hex_bytes_index = 0
	for side in cube:
		cube[side] = []
		for row in range(0, 3):
			cube[side].append(hex_byte_array[hex_bytes_index:hex_bytes_index + 3])
			hex_bytes_index = hex_bytes_index + 3
		
	return cube

def Get_Hex_Array_From_Cube(cube):
	cube_hex = []
	for side in cube:
		for row in cube[side]:
			for block in row:
				cube_hex.append(block)
	
	return cube_hex

def Get_String_From_Hex_Array(hex_array):
	string = ""
	for hex in hex_array:
		string = string + Get_Char_From_Hex(hex)
	
	return string

def Get_String_From_Cube(cube):
	string = ""
	cube_hex = Get_Hex_Array_From_Cube(cube)
	string = Get_String_From_Hex_Array(cube_hex)
	
	return string

def Get_Message_Cipher(receiving_agent, message):
	message_cipher = ""
	message_hex_array = Get_Hex_Array_From_String(message)
	public_key_hex_array = Get_Byte_Array_From_Hex(receiving_agent["PUBLIC_KEY"])
	
	
	
	return message_cipher

def Trace_Key_Exchange():
	alice, bob = Get_New_Agents(["Alice", "Bob"])
	
	
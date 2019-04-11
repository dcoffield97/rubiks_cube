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

def Get_Key_Mapped_To_Cube(key):
	cube = {"TOP" : None,
			"BOTTOM" : None,
			"LEFT" : None,
			"RIGHT" : None,
			"FRONT" : None,
			"BACK" : None}
	key_byte_array = Get_Byte_Array_From_Hex(key)
	key_bytes_index = 0
	for side in cube:
		cube[side] = []
		for row in range(0, 3):
			cube[side].append(key_byte_array[key_bytes_index:key_bytes_index + 3])
			key_bytes_index = key_bytes_index + 3
		
	return cube

def Get_Message_From_Cube(cube):
	message = None
	return message

def Trace_Key_Exchange():
	alice, bob = Get_New_Agents(["Alice", "Bob"])
	
	
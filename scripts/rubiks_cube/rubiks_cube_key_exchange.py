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
	hex = format(ord(char), "x")
	
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

def Get_New_Key(num_bytes = 57):
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

def Get_Hex_From_Cube(cube):
	hex = ""
	for side in cube:
		for row in cube[side]:
			for block in row:
				hex = hex + block
	
	return hex

def Get_Hex_From_String(string):
	hex = ""
	hex = "".join(Get_Hex_Array_From_String(string))
	
	return hex

def Get_String_From_Hex(hex):
	string = ""
	hex_byte_array = Get_Byte_Array_From_Hex(hex)
	
	for hex_byte in hex_byte_array:
		string = string + Get_Char_From_Hex(hex_byte)
	
	return string

def Get_String_From_Cube(cube):
	string = ""
	cube_hex = Get_Hex_Array_From_Cube(cube)
	string = Get_String_From_Hex_Array(cube_hex)
	
	return string

def Get_Binary_From_Hex(hex):
	binary = ""
	hex_array = list(hex)
	hex_to_binary = {"0" : "0000", 
					 "1" : "0001", 
					 "2" : "0010", 
					 "3" : "0011",
					 "4" : "0100",
					 "5" : "0101", 
					 "6" : "0110", 
					 "7" : "0111", 
					 "8" : "1000", 
					 "9" : "1001", 
					 "A" : "1010",
					 "B" : "1011",
					 "C" : "1100",
					 "D" : "1101",
					 "E" : "1110", 
					 "F" : "1111"}
	
	for hex_value in hex_array:
		binary = binary + hex_to_binary[hex_value.upper()]
		
	return binary

def Get_Hex_From_Binary(binary):
	hex = ""
	
	binary_to_hex = {"0000" : "0", 
					 "0001" : "1", 
					 "0010" : "2", 
					 "0011" : "3",
					 "0100" : "4",
					 "0101" : "5", 
					 "0110" : "6", 
					 "0111" : "7", 
					 "1000" : "8", 
					 "1001" : "9", 
					 "1010" : "A",
					 "1011" : "B",
					 "1100" : "C",
					 "1101" : "D",
					 "1110" : "E", 
					 "1111" : "F"}
	
	binary_index = 0
	while binary_index < len(binary):
		hex_value = binary_to_hex[binary[binary_index:binary_index + 4]]
		hex = hex + hex_value
		binary_index = binary_index + 4
		
	return hex

def Get_Exclusive_Or_Of_Binary(first_binary, second_binary):
	exclusive_or_of_binary = ""
	
	if len(first_binary) > len(second_binary):
		first_binary_array = list(first_binary)
		second_binary_array = list(second_binary.zfill(len(first_binary)))
	else:
		first_binary_array = list(first_binary.zfill(len(second_binary)))
		second_binary_array = list(second_binary)
	
	binary_arrays_index = 0
	for binary_arrays_index in range(0, len(first_binary_array)):
		if first_binary_array[binary_arrays_index] != second_binary_array[binary_arrays_index]:
			exclusive_or_of_bits = "1"
		else:
			exclusive_or_of_bits = "0"
		exclusive_or_of_binary = exclusive_or_of_binary + exclusive_or_of_bits
	
	return exclusive_or_of_binary

def Get_Exclusive_Or_Of_Hex(first_hex, second_hex):
	exclusive_or_of_hex = ""
	first_binary = Get_Binary_From_Hex(first_hex)
	second_binary = Get_Binary_From_Hex(second_hex)
	
	exclusive_or_of_binary = Get_Exclusive_Or_Of_Binary(first_binary, second_binary)
	exclusive_or_of_hex = Get_Hex_From_Binary(exclusive_or_of_binary)
	
	return exclusive_or_of_hex

def Get_Message_Cipher(public_key, message):
	message_cipher = ""
	
	hex_message = Get_Hex_From_String(message)
	message_cipher = Get_Exclusive_Or_Of_Hex(public_key, hex_message)
	
	return message_cipher

def Get_Scrambled_Cipher_Cube(public_key, message, num_turns):
	cipher_cube = None
	message_cipher = Get_Message_Cipher(public_key, message)
	cipher_cube = Get_Hex_Mapped_To_Cube(message_cipher)
	cipher_cube = rubiks_cube.Get_Scrambled_Cube(cipher_cube, num_turns)
	
	return cipher_cube

def Get_Unscrambled_Cipher_Cube(scrambled_cipher_cube):
	unscrambled_cipher_cube = None
	
	return unscrambled_cipher_cube

def Get_Decrypted_Cipher(private_key, cipher):
	decrypted_cipher = None
	
	return decrypted_cipher

def Trace_Key_Exchange():
	alice, bob = Get_New_Agents(["Alice", "Bob"])
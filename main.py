#Use Python 3.x
import Nishit
import CSK
import Ankur
import Subir
import Abhijeet

def main():
	print("Enter the name of the log file to be read: ")
	log_file_name = input()
	
	# For Nishit: Read the output in the log file for "show interfaces status" and create/output 7 lists each covering one column in the output of the command. Also output the hostname of the device
	# Definition Name: Regexr
	# Input: log_file_name
	# Output: 7 lists (Port, Name, Status, Vlan, Duplex, Speed, Type) and a string (hostname)
	# Definition Structure: Port, Name, Status, Vlan, Duplex, Speed, Type, hostname = Regexr(log_file_name)
	# Python file name: Nishit.py
	Port, Name, Status, Vlan, Duplex, Speed, Type, hostname = Nishit.Regexr(log_file_name)
	
	# For CSK: Convert 7 lists into a list of dictionaries
	# Definition Name: Dictionarize
	# Input: 7 lists (Port, Name, Status, Vlan, Duplex, Speed, Type)
	# Output: Interfaces dictionary (dict_interfaces[Port] = {"Name": Name, "Status": Status, "Vlan": Vlan, "Duplex": Duplex, "Speed": Speed, "Type": Type})
	# Definition Structure: dict_interfaces = Dictionarize(Port, Name, Status, Vlan, Duplex, Speed, Type)
	# Python file name: CSK.py
	dict_interfaces = CSK.Dictionarize(Port, Name, Status, Vlan, Duplex, Speed, Type)
	
	# For Ankur: Read the dictionary and find the number of interfaces and their types. Print the output directly on the console or create an excel output
	# Definition Name: count_and_type
	# Input: dict_interfaces
	# Output: Print the output directly on the console or Excel file
	# Definition Structure: count_and_type(dict_interfaces)
	# Python file name: Ankur.py
	Ankur.count_and_type(dict_interfaces)
	
	# For Subir: Read the dictionary and find the total count of interfaces with duplex(half, full, auto, a-half, a-full and all possible combinations) and speed(10, 100, 1000, auto, a-10, a-100, a-1000, a-10-100 and all possible combinations). Print the output directly on the console or create an excel output
	# Definition Name: duplex_and_speed
	# Input: dict_interfaces
	# Output: Print the output directly on the console or Excel file
	# Definition Structure: duplex_and_speed(dict_interfaces)
	# Python file name: Subir.py
	Subir.duplex_and_speed(dict_interfaces)
	
	# For Abhijeet: Read the dictionary and create an excel output with 7 columns containing attributes(Port, Name, Status, Vlan, Duplex, Speed, Type) and hostname of the device as sheet name
	# Definition Name: Interface_status
	# Input: dict_interfaces
	# Output: Print the output directly on the console or Excel file
	# Definition Structure: Interface_status(dict_interfaces, hostname)
	# Python file name: Abhijeet.py
	Abhijeet.Interface_status(dict_interfaces, hostname)
	
	return


if __name__ == "__main__":
	main()

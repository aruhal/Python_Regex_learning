import re
from collections import defaultdict
from collections import Counter
import collections


def count_interface():
    print("Enter the name of the log file to be read: ")
    log_file_name = input()
    file = open(log_file_name)
    #file = open("Hostname.txt", "rt")
    line = file.readline()
    Port = []
    Name = []
    Status = []
    Vlan = []
    Duplex = []
    Speed = []
    Type = []

    dict_interfaces = {}
    dict_count = []

    flag_interface_status = False

    while ("show interfaces status" not in line):
        line = file.readline()
    if ("show interfaces status" in line):
        flag_interface_status = True
        line = file.readline()
    if (flag_interface_status):
        while ("INAHD---SA001#" not in line):
            Temp = re.search("^([\w\/]+)\s+(.{19})([\w\-]+)\s+(\w+)\s+([\w\-]+)\s+([\w\-]+)\s+(.+)$", line)
            if Temp is not None:
                #print(Temp.group(1))
                #print(Temp.group(2).strip())
                #print(Temp.group(3))
                #print(Temp.group(4))
                #print(Temp.group(5))
                #print(Temp.group(6))
                #print(Temp.group(7))
                Port.append(Temp.group(1))
                Name.append(Temp.group(2).strip())
                Status.append(Temp.group(3))
                Vlan.append(Temp.group(4))
                Duplex.append(Temp.group(5))
                Speed.append(Temp.group(6))
                Type.append(Temp.group(7))


                dict_interfaces[Temp.group(1)] = {"Name": Temp.group(2).strip(), "Status": Temp.group(3),"Vlan": Temp.group(4), "Duplex": Temp.group(5),"Speed": Temp.group(6), "Type": Temp.group(7)}


                dict_count.append({"Port": Temp.group(1), "Name": Temp.group(2).strip(), "Status": Temp.group(3), "Vlan": Temp.group(4), "Duplex": Temp.group(5), "Speed": Temp.group(6), "Type": Temp.group(7)})



            line = file.readline()
    #print(Port)
    #print(Name)
    #print(Status)
    #print(Vlan)
    #print(Duplex)
    #print(Speed)
    #print(Type)
    #print(dict_interfaces)

    print("Total no of ports are", len(dict_count) - 1)

    typewise_count = defaultdict(int)
    for item in dict_count:
        typewise_count[item.get("Type")] += 1
        #typewise_count[item.get("Duplex")] += 1
        #typewise_count[item.get("Speed")] += 1

        #print(typewise_count)

    for i in typewise_count.keys():
        print(i + " : " + repr(typewise_count[i]))


    file.close()

    return

if __name__ == "__main__":
    count_interfcae()

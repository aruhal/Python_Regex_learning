from collections import defaultdict

dict_interfaces = {}

dict = []


dict_interfaces = {"Name": "User", "Status": "notconnect", "Vlan": "10", "Duplex": "half", "Speed": "auto", "Type": "BaseTX"}


dict.append({"Port": "Fa1/0/1", "Name": "User", "Status": "notconnect", "Vlan": "10", "Duplex": "auto", "Speed": "auto", "Type": "BaseTX"})

print("Total no of ports are", len(dict_interfaces))

typewise_count = defaultdict(int)
for item in dict:
    typewise_count[item.get("Type")] += 1
    # typewise_count[item.get("Duplex")] += 1
    # typewise_count[item.get("Speed")] += 1

    # print(typewise_count)

for i in typewise_count.keys():
    print(i + " : " + repr(typewise_count[i]))
    

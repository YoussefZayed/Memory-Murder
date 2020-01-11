import json

def set_location(x):
    return x

with open(set_location('/Users/dhritiaravind/Desktop/MLH/Cuhacking-2020/dat.json'), 'r') as f:
    data_dict = json.load(f)

def get_big_list(info):
    temp = []
    temp2 =[["Time", "device", "device-id", "event", "guest-id"]]
    for key, value in info.items():
        temp.append(int(key))
        for v in value.items():
            #print(v[1])
            temp.append(v[1])
        temp3 = temp.copy()
        temp2.append(temp3) 
        temp.clear()
    return temp2
print(get_big_list(data_dict))


        




        
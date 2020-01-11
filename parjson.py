import json


with open('/Users/dhritiaravind/Desktop/MLH/Cuhacking-2020/dat.json', 'r') as f:
    data_dict = json.load(f)

temp_person = []

def get_info(info):
    temp = []
    temp2 =[]
    for key, value in info.items():
         temp.append(key)
        for v in value.items():
            #print(v[1])
            temp.append(v[1])
        temp3 = temp.copy()
        temp2.append(temp3) 
        temp.clear()
    return temp2
print(get_info(data_dict))


        




        
import json
import time

def set_location(x):
    with open(x, 'r') as f:
        data_dict = json.load(f)
    lst = get_big_list(data_dict)
    #return lst
    return lst


def get_big_list(info):
    temp = []
    temp2 =[]
    for key, value in info.items():
        temp.append(time.strftime(key))
        for v in value.items():
            #print(v[1])
            temp.append(v[1])
        temp3 = temp.copy()
        temp2.append(temp3) 
        temp.clear()
    #twodarr = twodarray(temp2)
    return temp2


def types():
    return [['time', 'timestamp'],
    ['device', 'text'],
    ['device_id', 'text'],
    ['event','text'],
    ['guest_id', 'text']]

def twodarray(f):
    lst = []
    lst2 = []
    for i in range(len(f)):
        for j in range(5):
            if j % 5 == 4:
                lst.append('guest-id')
                lst.append(f[i][j])
            elif j % 5 == 3:
                lst.append('event')
                lst.append(f[i][j])
            elif j % 5 == 2:
                lst.append('device-id')
                lst.append(f[i][j])
            elif j % 5 == 1:
                lst.append('device')
                lst.append(f[i][j])
            elif j % 5 == 0:
                lst.append('time')
                lst.append(f[i][j])
            lst3 = lst.copy()
            lst2.append(lst3)
            lst.clear()
    return lst2


#print(set_location('/Users/dhritiaravind/Desktop/MLH/Cuhacking-2020/dat.json'))


        




        
#This script controls all the other scripts 
# its the script to rule them all 

from databaseBuilder import DatabaseBuilder
from parjason import *

test = DatabaseBuilder()
#print(test.dataReturnIf(["NAME"],[["integer"]], 0, "France"))
f = set_location('Cuhacking-2020/mdat.json')
#test.deleteTable('h')
test.createTable('testing', types())
test.insertTable('testing', f)
#test.createTable('Json_Data', f)

#This script controls all the other scripts 
# its the script to rule them all 

from databaseBuilder import DatabaseBuilder

test = DatabaseBuilder()
print(test.dataReturnIf(["NAME"],[["integer"]], 0, "France"))
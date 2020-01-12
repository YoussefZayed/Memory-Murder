#This script controls all the other scripts 
# its the script to rule them all 

from databaseBuilder import DatabaseBuilder
from parjason import *

test = DatabaseBuilder()
#print(test.dataReturnIf(["device"],[["access point"]],0,'h') )
print(test.seeDatabase("h",1))

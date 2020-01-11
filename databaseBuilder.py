#this file handles all the priliminary database importing and cleaning

import sqlite3

class DatabaseBuilder:
    
    def __init__ (self, database_name = "data.db"):
        """ Create a connection to a database  
            Returns: None
        """
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()


    def deleteTable(self,tableName= "None"):
        """ deletes table if table is specified
            Returns:  String status of function 
        """
        if  not tableName == "None":
            self.cursor.execute("DROP TABLE "+tableName + ";")
            return tableName + " has been deleted!"
        else:
            return "no table was given"

    



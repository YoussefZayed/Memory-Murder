#this file handles all the priliminary database importing and cleaning

import sqlite3

class DatabaseBuilder:
    
    def __init__ (self, database_name = "data.db"):
        """ Create a connection to a database  
            parameters : String database name
            Returns: None
        """
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()


    def deleteTable(self,tableName= "None"):
        """ deletes table if table is specified
            parameters : String Table name
            Returns:  String exit status of function 
        """
        if  not tableName == "None":
            self.cursor.execute("DROP TABLE "+tableName + ";")
            return tableName + " has been deleted!"
        else:
            return "no table was given"

    def createTable (self, tableName= "None" , tableColumns = []):
        """
        Creates a table with a table name given and each column in it 
         parameters : String table name
                      2d Array of column name and type eg [["time","int"]["location","TEXT"]]
        return : exit Status
       """
        if tableName == "None" or len(tableColumns) == 0:
           return "improper arguments given"
        else:
            command = " CREATE TABLE " + tableName + "("
            for column in tableColumns:
                command += column[0] + " " + column[1] +","
            command += ");"
            return "Table created"


    



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
        self.currentTable = "None"


    def deleteTable(self,tableName= self.currentTable):
        """ deletes table if table is specified
            parameters : String Table name
            Returns:  String exit status of function 
        """
        if  not tableName == "None":
            self.cursor.execute("DROP TABLE "+tableName + ";")
            return tableName + " has been deleted!"
        else:
            return "no table was given"

    def createTable (self, tableName= self.currentTable , tableColumns = []):
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
            command = command[:-1] #gets rid of the extra ,
            command += ");"
            self.cursor.execute(command)
            return "Table created"

    def insertTable (self, tableName= self.currentTable , tableRows = []):
        """
        inserts into a table with a table name given and each column in it 
         parameters : String table name
                      2d Array of row Values and type eg [["time","location"]]
        return : exit Status
       """
        if tableName == "None" or len(tableRows) == 0:
           return "improper arguments given"
        else:
            columnsArray = self.getTableColumns(tableName)
            columns = ""
            for column in columnsArray:
                columns +=   column +","
            columns = columns[:-1] #gets rid of the extra ,
            
            for row in tableRows:
                command = " INSERT INTO "+ tableName + " (" + columns+" ) VALUES ("
                values = ""
                for value in row:
                    values += "\"" +str(value) + "\" ,"
                values = values[:-1]
                command += values + ");"
                self.cursor.execute(command)
            return "Table rows inserted"
    
    def getTableColumns (self, tableName = self.currentTable):
            """ Grabs Columns from table
                parameters : String table name
                return : columns String array
            
            """
            command = """ PRAGMA table_info( """ + tableName + """ );"""

            self.cursor.execute(command)
            data = self.cursor.fetchall()
            columns = []
            for column in data:
                columns.append(column[1])
            return(columns)

    # def dataReturnIf (self,column ="None", value = "None", limit = 0,tableName = self.currentTable):

    #         """ This method returns all the rows in the table 

            
    #         """




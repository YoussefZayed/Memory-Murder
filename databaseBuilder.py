#this file handles all the priliminary database importing and cleaning

import sqlite3

class DatabaseBuilder:
    currentTable = "None"
    def __init__ (self, database_name = "data.db", currentTable = "None"):
        """ Create a connection to a database  
            parameters : String database name
            Returns: None
        """
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self.currentTable = "None"


    def deleteTable(self,tableName= currentTable):
        """ deletes table if table is specified
            parameters : String Table name
            Returns:  String exit status of function 
        """
        if  not tableName == "None":
            self.cursor.execute("DROP TABLE IF EXISTS "+tableName + ";")
            return tableName + " has been deleted!"
        else:
            return "no table was given"
    def createTable (self, tableName= currentTable , tableColumns = []):
        """
        Creates a table with a table name given and each column in it 
         parameters : String table name
                      2d Array of column name and type eg [["time","int"],["location","TEXT"]]
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

    def insertTable (self, tableName= currentTable , tableRows = []):
        """
        inserts into a table with a table name given and each column in it 
         parameters : String table name
                      2d Array of row Values eg [["time","location"]]
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
                
                command = " INSERT INTO `"+ tableName + "` (" + columns+") VALUES ("
                values = ""
                for value in row:
                    if type(value) is str:
                        values += "\"" +str(value) + "\","
                    else:
                        values += str(value) + ","
                values = values[:-1]
                command += values + ");"
                self.cursor.execute(command)
            self.connection.commit()
            return "Table rows inserted"
    
    def getTableColumns (self, tableName = currentTable):
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

    def dataReturnIf (self,columns ="None", values = "None", limit = 0,tableName = currentTable):

        """ This method returns all the rows in the table 
                where a column matches a value
                 parameters : column array of columns
                              value array of limited value
                              limit of how many items to return
                              tableName name of the table
                return : values
        """
        try:
            command = "Select * From " + tableName+ " "
        
            for i in range(0,len(columns)):
                if i == 0:
                    command += "WHERE "
                
                if len(values[i]) == 2:
                    command +=  " "+columns[i]+"   BETWEEN \"" + str(values[i][0]) + "\"" + " AND \"" + str(values[i][1]) + "\""
                else:
                    command +=  columns[i]+ " = \'" + str(values [i] [0]) + "\'"
                command += ","
            command = command[:-1] 
            if limit <1:
                command += ";"
            else :
                command += "LIMIT " + str(limit) + ";"
            self.cursor.execute(command)
            data = self.cursor.fetchall()
            return(data)
         
        except EOFError as e:
            return "Improper parameters"

    def seeDatabase (self,tableName = currentTable,limit = 0):
        # """ returns the entire table """"
        if limit == 0:
            self.cursor.execute("SELECT * FROM " + tableName + " ;")
        else:
             self.cursor.execute("SELECT * FROM " + tableName + " LIMIT " +str(limit)+ ";")
        return self.cursor.fetchall()





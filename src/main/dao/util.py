# Database utillity functions
import pyodbc
class Util:
    @staticmethod
    def get_connection():
        # Read database path from config file and read the line dbPath=...
        configPath = "app.conf"
        with open(configPath, "r") as configFile:
            config = configFile.readlines()
            for line in config:
                if line.startswith("dbPath="):
                    dbPath = line[7:]
                    # to utf-8
                    dbPath = dbPath.encode("utf-8").decode("utf-8-sig")
                    print(dbPath)
                    return pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + dbPath + ";")
            raise Exception("Database path not found in config file")
    
    @staticmethod
    def close_connection(connection):
        connection.close()

        

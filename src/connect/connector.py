import mysql.connector
class Connection:
    def __init__(self) -> None:
        try:
            self.cnx = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = 'f00tball@143',
                database = 'comms'
            )
            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as error:
            print(f"Error: {error}")
            return []
        
    def retrieveComms(self) -> list[tuple]:
        try:
            if self.cnx.is_connected():
                self.cursor.execute("SELECT * FROM msgs")
                records = self.cursor.fetchall()
                return records
        except mysql.connector.Error as error:
            print(f"Error: {error}")
            return []
    def sendComms(self, username: str, message: str) -> None:
        try:
            if self.cnx.is_connected():
                query = f"INSERT INTO msgs VALUES (%s, %s);"
                values = (username, message)
                self.cursor.execute(query, values)
                self.cnx.commit()        
        except mysql.connector.Error as error:
            print(f"Error: {error}")
            return []

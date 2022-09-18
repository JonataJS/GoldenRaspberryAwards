import jaydebeapi
from marshmallow import Schema, fields, INCLUDE
import csv



class Ormdb:

    def _execute(self, query, returnResult=None):
        connection  = jaydebeapi.connect(
                "org.h2.Driver",
                "jdbc:h2:tcp://localhost:5234/movies;DATABASE_TO_LOWER=TRUE",
                ["SA", ""],
                "db/h2-2.1.214.jar")
        cursor = connection.cursor()
        cursor.execute(query)
        if returnResult:
            returnResult = self._convert_to_schema(query, cursor)
        cursor.close()
        connection.close()
        
        return returnResult

    def __create_table(self):
        #query =  ("CREATE TABLE IF NOT EXISTS MOVIE ("
        # "  \"year\"  INT,"
        # "  title VARCHAR,"
        # "  studios VARCHAR,"
        # "  producers VARCHAR,"
        # "  winner VARCHAR)")
        query = ("CREATE TABLE IF NOT EXISTS MOVIE AS SELECT * FROM CSVREAD('files/movielist.csv');")
        self._execute(query)
        print("Table created")

    def __fill_table(self):
        file = open("files/movielist.csv")
        csvreader = csv.reader(file)
        header = next(csvreader)

        rows = []
        fields = "\"year\", title, studios, producers, winner"
        table = "MOVIE"
        for row in csvreader:
            row_formatted = ','.join(map(str,row)).split(";")
            last_element = len(row_formatted)-1
            if not row_formatted[last_element]:
                row_formatted[last_element] = "no"
            values = '{},"{}","{}","{}","{}"'.format(row_formatted[0],row_formatted[1],row_formatted[2],row_formatted[3],row_formatted[4])
            query =  (f"INSERT INTO {table} VALUES({values});")
            self._execute(query)
            rows.append(row)
        


    def _convert_to_schema(self,query, cursor):
        column_names = [record[0].lower() for record in cursor.description][0].split(";")
        cursor.execute(query)
        column_and_values = []
        
        for record in cursor.fetchall():
            #value = record[0].split(";")
            value = ''.join(map(str,record[0])).split(";")
            value_dict = {}
            for i in range(len(value)):
                value_dict[column_names[i]] = value[i]
            column_and_values.append(value_dict)
        return MoviesSchema().load(column_and_values, many=True)

    def get_all(self):
        return self._execute("SELECT * FROM MOVIE", returnResult=True)

    def initialize(self):
        self.__create_table()
        #self.__fill_table()

class MoviesSchema(Schema):
    year = fields.Str()
    title = fields.Str()
    studios = fields.Str()
    producers = fields.Str()
    winner = fields.Str(default="no")


import mysql.connector
from ..models import SelectedField
from ..serializers import SelectedFieldSerializer
from rest_framework.response import Response
from rest_framework import status

class MysqlConnection:
    def connect(self, settings):

        mydb = mysql.connector.connect(
            host=settings.host,
            user=settings.user,
            password=settings.password,
            database=settings.database
        )

        return mydb

    def existTable(self, mycursor, tableSelected, settings):
        newCursor = mycursor.cursor()
        newCursor.execute("SELECT TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA = " + "'" + settings.database + "'")
        myresult = newCursor.fetchall()
        for table in myresult:
            if (tableSelected == table[0]):
                return True
        return False

    def createTable(self, mycursor, tableSelected):
        data = SelectedField.objects.all()
        serializer = SelectedFieldSerializer(data, many=True)
        fields = serializer.data

        stringSql = "CREATE TABLE " + tableSelected + " (id INT AUTO_INCREMENT PRIMARY KEY, "

        for field in fields:
            stringSql = stringSql + (field['nameBank'] + " VARCHAR(255), ")

        stringSqlComplete = stringSql[: -2] + ")"

        cursor = mycursor.cursor(buffered=True, dictionary=True)
        cursor.execute(stringSqlComplete)

    def insertTable(self, mycursor, table, settings, dataReady):
        newCursor = mycursor.cursor()
        newCursor.execute(
            "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = " + "'" + settings.database + "' AND TABLE_NAME = " + "'" + table + "'"
        )
        myresult = newCursor.fetchall()

        fieldsTable = []

        for field in myresult:
            if 'id' != list(field)[0]:
                fieldsTable.append(list(field)[0])

        fieldsExist = []
        fieldsNotExist = []

        for field in dataReady:
            if field['nameBank'] in fieldsTable:
                fieldsExist.append(field)
            else:
                fieldsNotExist.append(field)

        sql = "INSERT INTO " + table + " ("

        for data in fieldsExist:
                sql = sql + data['nameBank'] + ", "

        sql = sql[: -2] + ") VALUES ("

        for data in fieldsExist:
                sql = sql + "'" + data['name'] + "'" + ", "

        sql = sql[:-2] + ")"

        newCursor.execute(sql)

        mycursor.commit()

        return Response(data, status=status.HTTP_201_CREATED)


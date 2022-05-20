from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from .services.OCR import Ocr
from .services.MysqlConnection import MysqlConnection
from .models import SelectedField, ConnectionsMysql, UserMan
from. serializers import SelectedFieldSerializer, ConnectionsMysqlSerializer, UsersManSerializer

class ConnectionsMysqlApiView(APIView):
    def get(self, request):
        connectionsMysql = ConnectionsMysql.objects.all()
        serializer = ConnectionsMysqlSerializer(connectionsMysql, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ConnectionsMysqlSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        field = ConnectionsMysql.objects.get(id=request.data['id'])
        serializer = ConnectionsMysqlSerializer(field, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        field = ConnectionsMysql.objects.get(id=request.data['id'])
        serializer = ConnectionsMysqlSerializer(field)
        field.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

class UsersManAPIView(APIView):
    def get(self, request):
        userMan = UserMan.objects.get(id=request.data['id'])
        serializer = UsersManSerializer(userMan)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersManSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        field = UserMan.objects.filter(id=request.data['id'], name=request.data['name'])
        serializer = UsersManSerializer(field, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class SelectedFieldAPIView(APIView):
    def get(self, request):
        fields = SelectedField.objects.all()
        serializer = SelectedFieldSerializer(fields, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SelectedFieldSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        field = SelectedField.objects.get(id=request.data['id'])
        serializer = SelectedFieldSerializer(field, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        field = SelectedField.objects.get(id=request.data['id'])
        serializer = SelectedFieldSerializer(field)
        field.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

class ScanningApiView(APIView):
    def post(self, request):
        data = Ocr.getAllWords(self, request)
        fieldsSelected = Ocr.returnAllFieldsSelected(self)
        fieldBank = Ocr.returnAllFieldBankSelected(self)
        dataReady = []
        for index, field in enumerate(fieldsSelected):
            dataFieldValues = Ocr.getValuesField(self, data, field, fieldsSelected)
            valueField = Ocr.valueFormated(self, dataFieldValues)
            dataReady.append({'name': valueField, 'nameBank': fieldBank[index]})

        settingsBank = ConnectionsMysql.objects.get(ativo=True)
        myCursor = MysqlConnection.connect(self, settingsBank)

        result = None

        if MysqlConnection.existTable(self, myCursor, request.data['table'], settingsBank):
            myCursor = MysqlConnection.connect(self, settingsBank)
            result = MysqlConnection.insertTable(self, myCursor, request.data['table'], settingsBank, dataReady)
        else:
            myCursor = MysqlConnection.connect(self, settingsBank)
            MysqlConnection.createTable(self, myCursor, request.data['table'])
            result = MysqlConnection.insertTable(self, myCursor, request.data['table'], settingsBank, dataReady)

        return result

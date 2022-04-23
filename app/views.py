from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .services.OCR import Ocr
from .models import SelectedField
from. serializers import SelectedFieldSerializer


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
        fieldsSelected = Ocr.returnAllFieldsSelected(self, request)
        dataReady = []
        for field in fieldsSelected:
            dataFieldValues = Ocr.getValuesField(self, data, field, fieldsSelected)
            valueField = Ocr.valueFormated(self, dataFieldValues)
            dataReady.append({field: valueField});

        return Response(dataReady, status=status.HTTP_201_CREATED)

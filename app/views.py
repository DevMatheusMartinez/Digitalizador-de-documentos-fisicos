from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .services.OCR import Ocr
from .models import SelectedField
from. serializers import SelectedFieldSerializer

class SelectedFieldAPIView(APIView):
    def get(self, request):
        cursos = SelectedField.objects.all()
        serializer = SelectedFieldSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = Ocr.getAllWords(self, request)
        fieldsSelected = Ocr.returnAllFieldsSelected(self, request)
        dataReady = []
        for field in fieldsSelected:
            dataFieldValues = Ocr.getValuesField(self, data, field, fieldsSelected)
            valueField = Ocr.valueFormated(self, dataFieldValues)
            dataReady.append({field: valueField});

        return Response(dataReady, status=status.HTTP_201_CREATED)


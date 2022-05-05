import cv2
import pytesseract
import numpy
from ..models import SelectedField
from ..serializers import SelectedFieldSerializer

class Ocr:
    def getAllWords(self, request):
        img = cv2.imdecode(numpy.fromstring(request.FILES['image'].read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        boxes = pytesseract.image_to_data(img)
        data = []
        for x, b in enumerate(boxes.splitlines()):
            if x != 0:
                b = b.split()
                if len(b) == 12:
                    x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                    cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
                    if '_' in b[11]:
                        formated = ' '.join(b[11].split('_')).split()
                        for value in formated:
                            data.append(value)
                    else:
                        data.append(b[11])

        return data

    def returnAllFieldsSelected(self):
        data = SelectedField.objects.all()
        serializer = SelectedFieldSerializer(data, many=True)
        fields = serializer.data
        namesFields = []
        for field in fields:
            namesFields.append(field['name']+':')

        return namesFields

    def returnAllFieldBankSelected(self):
        data = SelectedField.objects.all()
        serializer = SelectedFieldSerializer(data, many=True)
        fields = serializer.data
        fieldsBank = []
        for field in fields:
            fieldsBank.append(field['nameBank'])

        return fieldsBank


    def getValuesField(self, data, fieldSelected, fieldsSelected):
        fieldValues = []
        hasFieldSelected = False
        for word in data:
            if hasFieldSelected:
                if not word[-1] == ':' and word != fieldsSelected:
                    fieldValues.append(word)
                else:
                    return fieldValues

            if word == fieldSelected:
                hasFieldSelected = True

        return fieldValues


    def valueFormated(self, data):

        for word in data:
            if word[-1] == ':':
                return ' '.join(data[0 : data.index(word)])

        return ' '.join(data)


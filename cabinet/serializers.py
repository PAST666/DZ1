import io
from rest_framework import serializers
from .models import Visit, Master, Service
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer



class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('__all__')

class VisitModel:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class VisitSerializer2(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=12)

def encode():
    model =     VisitModel("Ivan", "81234567899")
    model_sr = VisitSerializer2(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)

def decode():
    stream = io.BytesIO(b'{"name":"Ivan", "phone":"81234567899"}')
    data = JSONParser().parse(stream)
    serializer = VisitSerializer2(data=data)
    serializer.is_valid()
    print(serializer.validated_data)

class VisitSerializer3(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=12)
    comment = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    status = serializers.IntegerField()
    master = serializers.PrimaryKeyRelatedField(queryset=Master.objects.all())
    services = serializers.PrimaryKeyRelatedField(many=True, queryset=Service.objects.all())
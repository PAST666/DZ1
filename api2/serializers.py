import io
from rest_framework import serializers
from cabinet.models import Visit, Master, Service
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

class VisitSerializer3(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('__all__')

    # name = serializers.CharField(max_length=255)
    # phone = serializers.CharField(max_length=12)
    # comment = serializers.CharField()
    # created_at = serializers.DateTimeField(read_only=True)
    # status = serializers.IntegerField()
    # master = serializers.PrimaryKeyRelatedField(queryset=Master.objects.all())
    # services = serializers.PrimaryKeyRelatedField(many=True, queryset=Service.objects.all())

    # def create(self, validated_data):
    #     services_data = validated_data.pop('services', None)  # Извлекаем services из validated_data
    #     visit_instance = Visit.objects.create(**validated_data)  # Создаем объект Visit

    #     if services_data:  # Если есть данные для services
    #         visit_instance.services.set(services_data) # Устанавливаем many-to-many отношения
    #     return visit_instance

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.comment = validated_data.get('comment', instance.comment)
    #     instance.created_at = validated_data.get('created_at', instance.created_at)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.master = validated_data.get('master', instance.master)
    #     services_data = validated_data.get('services', None)
    #     if services_data is not None:
    #         instance.services.set(services_data)
    #     instance.save()
    #     return instance
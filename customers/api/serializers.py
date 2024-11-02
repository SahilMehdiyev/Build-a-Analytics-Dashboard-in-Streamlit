from rest_framework import serializers
from customers.models import Customer
from ..choices import GENDER_CHOICES


class GenderChoiceFieldSerializer(serializers.Field):
    def to_representation(self,obj):
        return dict(GENDER_CHOICES)[obj]
    
    def to_internal_value(self, data):
        for key, value in GENDER_CHOICES:
            if value == data:
                return key
        raise serializers.ValidationError("Invalid gender choice.")



class CustomerSerializer(serializers.ModelSerializer):
    gender = GenderChoiceFieldSerializer()
    created = serializers.SerializerMethodField()
    class Meta:
        model = Customer
        fields = (
            'id',
            'name',
            'gender',
            'age',
            'favorite_number',
            'created'
        )
    def get_created(self,obj):
        return obj.created.strftime('%Y-%m-%d %H:%M:%S')
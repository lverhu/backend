from rest_framework import serializers
from power import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['phone', 'password']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id', 'name', 'procedure']


class GlobalParamSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.GlobalParam
        fields = ['name', 'value','product', 'product_name']
        extra_kwargs = {
            'product':{'write_only':True},
            'product_name':{'read_only':True},
        }


class TestUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TestUnit
        fields = ['name', 'function','description','product', 'product_name']
        extra_kwargs = {
            'product':{'write_only':True},
            'product_name':{'read_only':True},
        }


class UnitParamSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.UnitParam
        fields = ['name', 'type','description','value', 'testunit','testunit_name']
        extra_kwargs = {
            'testunit':{'write_only':True},
            'testunit_name':{'read_only':True},
        }
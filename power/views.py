from rest_framework.views import APIView
from rest_framework.response import Response
from power import models
from power.serializers import ProductSerializer, GlobalParamSerializer, TestUnitSerializer,UnitParamSerializer, UserSerializer


class APIResponse(Response):
    def __init__(self, code='0', message='success', data=None, status=None, headers=None, **kwargs):
        dic = {'code':code, 'message':message}
        if data:
            dic = {'code':code, 'message':message, 'data':data}
        dic.update(kwargs)
        super().__init__(data=dic, status=status, headers=headers)


class UserInfoView(APIView):
    def get(self, request, *args, **kwargs):        
        return APIResponse(success=True, state=11, message="success", content="{\"access_token\": \"111\"}")


class UserLoginView(APIView):
    def get(self, request, *args, **kwargs):  
    #     {
    #     "success": true,
    #     "state": 11,
    #     "message": "success",
    #     "content": {
    #         "isUpdatedPassword": false,
    #         "portrait":"https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
    #         "userName":"lverhu"
    #     }
    # }      
        return APIResponse(success=True, state=11, message="success", content="{\"access_token\": \"111\"}")

class ProductAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # 查询单个和查询所有，合到一起
        if kwargs.get('pk', None):
            product = models.Product.objects.filter(pk=kwargs.get('pk')).first()
            product_ser = ProductSerializer(product, many=False)
            return APIResponse(data=product_ser.data)

        product_list = models.Product.objects.all().filter(is_delete=False)
        product_list_ser = ProductSerializer(product_list, many=True)
        return APIResponse(data=product_list_ser.data)
    
    def post(self, request, *args, **kwargs):
        # 增单条和多条功能
        if isinstance(request.data,dict):
            product_ser = ProductSerializer(data=request.data)
            product_ser.is_valid(raise_exception=True)
            product_ser.save()
        elif isinstance(request.data, list):
            # 现在是ListSerializer对象
            product_ser = ProductSerializer(data=request.data, many=True) #增多条
            product_ser.is_valid(raise_exception=True)
            product_ser.save()
        return APIResponse(data=product_ser.data)
    
    # 修改
    def put(self, request, *args, **kwargs):
        if kwargs.get('pk', None):
            product = models.Product.objects.filter(pk=kwargs.get('pk')).first()
            print(request.data)
            product_ser = ProductSerializer(instance=product, data=request.data, partial=True)
            product_ser.is_valid(raise_exception=True)
            product_ser.save()
            return APIResponse(data=product_ser.data)
        
    def delete(self, request, *args, **kwargs):
        # 单条和批量删除
        pk = kwargs.get('pk')
        pks = []
        if pk:
            # 单条删除
            pks.append(pk)
        # 不管单条删除还是批量删除，都用批量删除
        # {'pks':[1,2,3]}
        else:
            pks = request.data.get('pks')
        ret = models.Product.objects.filter(pk__in=pks, is_delete=False).update(is_delete=True)
        if ret:
            return APIResponse(data={'message':'delete success'})
        else:
            return APIResponse(data={'message':'no data to delete'})
    

class GlobalParamAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # 查询单个和查询所有，合到一起
        global_param_list = models.GlobalParam.objects.all().filter(is_delete=False)
        global_param_list_ser = GlobalParamSerializer(global_param_list, many=True)
        return APIResponse(data=global_param_list_ser.data)
    

class TestUnitAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # 查询单个和查询所有，合到一起
        test_unit_list = models.TestUnit.objects.all().filter(is_delete=False)
        test_unit_list_ser = TestUnitSerializer(test_unit_list, many=True)
        return APIResponse(data=test_unit_list_ser.data)
    
    def post(self, request, *args, **kwargs):
        # 增单条和多条功能
        if isinstance(request.data,dict):
            test_unit_ser = TestUnitSerializer(data=request.data)
            test_unit_ser.is_valid(raise_exception=True)
            test_unit_ser.save()
        elif isinstance(request.data, list):
            # 现在是ListSerializer对象
            test_unit_ser = TestUnitSerializer(data=request.data, many=True) #增多条
            test_unit_ser.is_valid(raise_exception=True)
            test_unit_ser.save()
        return APIResponse(data=test_unit_ser.data)
    
    # 修改
    def put(self, request, *args, **kwargs):
        if kwargs.get('pk', None):
            test_unit = models.TestUnit.objects.filter(pk=kwargs.get('pk')).first()
            test_unit_ser = TestUnitSerializer(instance=test_unit, data=request.data, partial=True)
            test_unit_ser.is_valid(raise_exception=True)
            test_unit_ser.save()
            return APIResponse(data=test_unit_ser.data)

    def delete(self, request, *args, **kwargs):
        # 单条和批量删除
        pk = kwargs.get('pk')
        pks = []
        if pk:
            # 单条删除
            pks.append(pk)
        # 不管单条删除还是批量删除，都用批量删除
        # {'pks':[1,2,3]}
        else:
            pks = request.data.get('pks')
        ret = models.TestUnit.objects.filter(pk__in=pks, is_delete=False).update(is_delete=True)
        if ret:
            return APIResponse(data={'message':'delete success'})
        else:
            return APIResponse(data={'message':'no data to delete'})



class UnitParamAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # 查询单个和查询所有，合到一起
        unit_param_list = models.UnitParam.objects.all().filter(is_delete=False)
        unit_param_list_ser = UnitParamSerializer(unit_param_list, many=True)
        return APIResponse(data=unit_param_list_ser.data)

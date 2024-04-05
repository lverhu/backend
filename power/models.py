from django.db import models


class BaseModel(models.Model):
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(models.Model):
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.phone
    
    class Meta:
        db_table = "tb_user"
        verbose_name_plural = "用户表"


class Product(BaseModel):
    name = models.CharField(max_length=32)
    procedure = models.CharField(max_length=32)
    # productdetail = models.OneToOneField(to='ProductDetail', db_constraint=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "tb_product"
        verbose_name_plural = "产品表"


class ProductDetail(BaseModel):
    type = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.type
    
    class Meta:
        db_table = "tb_productdetail"
        verbose_name_plural = "产品详情表"


class GlobalParam(BaseModel):
    name = models.CharField(max_length=32)
    value = models.CharField(max_length=32)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    class Meta:
        db_table = "tb_globalparam"
        verbose_name_plural = "全局参数表"

    def __str__(self) -> str:
        return self.name

    @property
    def product_name(self):
        return self.product.name
    

class TestUnit(BaseModel):
    name = models.CharField(max_length=32)
    function = models.CharField(max_length=32)
    description = models.CharField(max_length=32)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    class Meta:
        db_table = "tb_testunit"
        verbose_name_plural = "测试用例表"

    def __str__(self) -> str:
        return self.name

    @property
    def product_name(self):
        return self.product.name


class UnitParam(BaseModel):
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    value = models.CharField(max_length=32)
    description = models.CharField(max_length=32)
    testunit = models.ForeignKey(TestUnit, on_delete=models.CASCADE)

    class Meta:
        db_table = "tb_unitparam"
        verbose_name_plural = "用例参数表"

    def __str__(self) -> str:
        return self.name
    
    @property
    def testunit_name(self):
        return self.testunit.name
    
    

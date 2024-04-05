"""
URL configuration for backends project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from power import views

urlpatterns = [
    path('user/getInfo/', views.UserInfoView.as_view()),
    path('user/login/', views.UserLoginView.as_view()),
    path('products/', views.ProductAPIView.as_view()),
    re_path('products/(?P<pk>\d+)', views.ProductAPIView.as_view()),
    # path('productdetail/', views.ProductAPIView.as_view()),
    path('globalparams/', views.GlobalParamAPIView.as_view()),
    re_path('globalparams/(?P<pk>\d+)', views.GlobalParamAPIView.as_view()),
    path('testunits/', views.TestUnitAPIView.as_view()),
    re_path('testunits/(?P<pk>\d+)', views.TestUnitAPIView.as_view()),
    path('unitparams/', views.UnitParamAPIView.as_view()),
    re_path('unitparams/(?P<pk>\d+)', views.UnitParamAPIView.as_view()),
]

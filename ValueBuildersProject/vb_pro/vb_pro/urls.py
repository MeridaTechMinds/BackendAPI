"""
URL configuration for vb_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from vb_app.views import property_details
from vb_app.views import *
router = DefaultRouter()
router.register(r'property', property_details)
router.register(r'districts_filter', DistrictViewSet, basename='districts')
router.register(r'states_filter', StateViewSet, basename='states')
router.register(r'price_filter', PriceViewSets, basename='price')
router.register(r'doorfaceing_filter', DoorFacingViewSets, basename='door_facing')
router.register(r'data_search', SearchDataViewSets, basename='data_search')
router.register(r'pincode_data/(?P<pincode>\d+)', PincodeDataViewSet, basename='pincode_data')
router.register(r'category/(?P<category>[^/]+)', PropertycategoryData, basename='categoryData')
router.register(r'sub_category/(?P<sub_category>[^/]+)', PropertysubcategoryData, basename='subcategoryData')
router.register(r'contact_details', ContactViewSets, basename='contactsiewsets')
# router.register(r'unique_property', UniquePropertyViewSet, basename='unique_property')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include("vb_app.urls")),
    path("api/", include(router.urls)),
    path('api/unique_property/<str:property_id>/', UniquePropertyViewSet.as_view({'get': 'retrieve'}), name='unique_property_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

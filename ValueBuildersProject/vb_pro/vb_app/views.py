from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404
import nltk
from concurrent.futures import ProcessPoolExecutor
from collections import defaultdict
nltk.download('punkt')


class property_details(viewsets.ModelViewSet):
    queryset = PropertyModel.objects.all()
    serializer_class = property_serializer

class UniquePropertyViewSet(viewsets.ViewSet):
    def retrieve(self, request, property_id=None):
        try:
            property_instance = PropertyModel.objects.get(property_id=property_id)
        except PropertyModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = property_serializer(property_instance, context={'request': request})
        return Response(serializer.data)
    

    

class PropertycategoryData(viewsets.ModelViewSet):
    queryset = PropertyModel.objects.all()
    serializer_class = property_serializer
    def get_queryset(self):
        cat_val = self.kwargs.get('category')
        queryset = self.queryset.filter(Q(category=cat_val))
        return queryset
    
class PropertysubcategoryData(viewsets.ModelViewSet):
    queryset = PropertyModel.objects.all()
    serializer_class = property_serializer
    def get_queryset(self):
        sub_cat_val = self.kwargs.get('sub_category')
        queryset = self.queryset.filter(Q(sub_category=sub_cat_val))
        return queryset
    
class PincodeDataViewSet(viewsets.ModelViewSet):
    queryset = PropertyModel.objects.all()
    serializer_class = property_serializer

    def get_queryset(self):
        pincode = self.kwargs.get('pincode')
        queryset = self.queryset.filter(pincode=pincode)
        return queryset
    
class PriceViewSets(viewsets.ModelViewSet):
    def price(self,your_price):
        l = []
        l2=[]
        for i in your_price:
            a = i[0]
            b = i[1]
            queryset = PropertyModel.objects.filter(price__range=(a,b))
            serializer = property_serializer(queryset, many=True,context={"request":self.request})
            k = serializer.data
            l.append(k)
        for j in l:
            if j==list():
                pass
            elif j in l2:
                pass
            else:
                l2.extend(j)
        return Response(l2)
    # def list(self, request):
    #     your_price = request.data.get('Price')
    #     return self.price(your_price)
    def create(self, request):
        your_data = request.data.get('Price')
        return self.price(your_data)

class StateViewSet(viewsets.ModelViewSet):
    def state(self,your_state):
        s=[]
        ss=[]
        for i in your_state:
            queryset = PropertyModel.objects.filter(Q(state=i))
            serializer = property_serializer(queryset, many=True,context={"request":self.request})
            sk = serializer.data
            s.append(sk)
        for j in s:
            if j==list():
                pass
            elif j in ss:
                pass
            else:
                ss.extend(j)
        return Response(ss)
    # def list(self, request):
    #     your_state = request.data.get('State')
    #     return self.state(your_state)
    def create(self, request):
        your_data = request.data.get('State')
        return self.state(your_data)

class DistrictViewSet(viewsets.ViewSet):
    def district(self, your_dist):
        s = []
        ss = []
        for i in your_dist:
            queryset = PropertyModel.objects.filter(Q(District=i))
            serializer = property_serializer(queryset, many=True, context={'request': self.request})
            sk = serializer.data
            s.append(sk)
        
        for j in s:
            if j == []:
                pass
            else:
                ss.extend(j)
        return Response(ss)

    # def list(self, request):
    #     your_dist = request.data.get('District')
    #     return self.district(your_dist)
    def create(self, request):
        your_data = request.data.get('District')
        return self.district(your_data)
 
class DoorFacingViewSets(viewsets.ViewSet):
    serializer_class = property_serializer

    def door_facing(self, your_data):
        if your_data is None:
            return Response([])
        
        s = []
        for i in your_data:
            queryset = PropertyModel.objects.filter(Q(door_facing=i))
            serializer = self.serializer_class(queryset, many=True, context={"request": self.request})
            sk = serializer.data
            s.append(sk)

        # Merge lists in s into a single list
        ss = [item for sublist in s for item in sublist]

        return Response(ss)

    def create(self, request):
        your_data = request.data.get('door_facing')
        return self.door_facing(your_data)
    



class SearchDataViewSets(viewsets.ModelViewSet):
    def search(self):
        data = PropertyModel.objects.all()
        d={}
        for obj in data:
            d[int(obj.id)]=f"{obj.category},{obj.sub_category},{obj.address_line1},{obj.address_line2},{obj.state},{obj.District},{obj.pincode},{obj.price},{obj.door_facing},{obj.property_id},{obj.description}"
        return d

    def search_index(self,index, query):
        file_list = list()
        query_tokens = set(nltk.word_tokenize(query.lower()))

        for id,record in index.items():
            text_tokens = set(nltk.word_tokenize(record.lower()))

            if query_tokens.issubset(text_tokens):
                file_list.append(id)
                
        return file_list

    def getd(self,query,index):
        self.query = query
        results = self.search_index(index, query)

        l=[]
        ml=[]
        for i in results:
            obj_list = get_list_or_404(PropertyModel, id=i)
            serializer = property_serializer(obj_list, many=True,context={"request":self.request})
            l.append(serializer.data)
        for j in l:
            ml=ml+list(j)
        return Response(ml)
        
    # def list(self, request):
    #     self.your_dist = request.data.get('query')
    #     index = self.search()
    #     return self.getd(self.your_dist,index)
    def create(self, request):
        self.your_dist = request.data.get('query')
        index = self.search()
        return self.getd(self.your_dist,index)



            

class ContactViewSets(viewsets.ModelViewSet):
    queryset = contact.objects.all()
    serializer_class = contact_serializer

from django.core.mail import send_mail     
@api_view(['POST',])
def Contact_data(request):
    if request.method=='POST':
        serializer=contact_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data['email']
            
            # Send email
            name=serializer.validated_data['name']
            subject="Value Builders Contact By : "+name
            send_mail(
               subject,
                f"Name: {serializer.validated_data['name']}\nEmail: {serializer.validated_data['email']}\nmessage: {serializer.validated_data['message']}",
                email, 
                ['athirupan.kk@gmail.com'],
                fail_silently=False,
                
            )
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
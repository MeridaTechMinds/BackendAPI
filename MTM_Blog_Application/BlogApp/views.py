from django.shortcuts import render

from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,get_object_or_404,get_list_or_404,HttpResponse
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Blog, Points
from .serializers import BlogSerializer, pointSerializer,commentSerializer,contactSerializer,ApointmentSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
 
class PointViewSet(viewsets.ModelViewSet):
    queryset = Points.objects.all()
    serializer_class = pointSerializer

@api_view(['GET',])
def catagory_details(request,slug):
    try:
        tasks=Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serialized_task=BlogSerializer(tasks,context={'request': request})
    return Response(serialized_task.data)

@api_view(['GET',])
def catagory(request,Category):
    try:
        tasks=get_list_or_404(Blog,Category=Category)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serialized_task=BlogSerializer(tasks,many=True,context={'request': request})
        return Response(serialized_task.data)
    
@api_view(['POST',])
def comments_list(request):
    if request.method=='POST':
        serialized_task=commentSerializer(data=request.data)
        if serialized_task.is_valid():
            serialized_task.save()
            return Response(serialized_task.data,status=status.HTTP_201_CREATED)


from django.core.mail import send_mail     
@api_view(['POST',])
def contacts_data(request):
    if request.method=='POST':
        serializer=contactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data['email']
            # Send email
            name=serializer.validated_data['first_name']
            subject='Contact Details Form Filled By : '+name
            send_mail(
                subject,
                f"First name: {serializer.validated_data['first_name']}\nLast name:{serializer.validated_data['last_name']}\nEmail: {serializer.validated_data['email']}\nCompany: {serializer.validated_data['company']}\nPhone_num: {serializer.validated_data['phone']}\ninterested: {serializer.validated_data['interested']}\nmessage: {serializer.validated_data['message']}",
                email, 
                ['dmmanager@meridatechminds.com'],
                fail_silently=False,
                
            )
            print("got it ")
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST',])
def apointment_data(request):
    if request.method=='POST':
        serializer=ApointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data['email']
            # Send email
            name=serializer.validated_data['name']
            subject="Apointment Details Form Filled By: "+name
            send_mail(
                subject,
                f"Name: {serializer.validated_data['name']}\nEmail: {serializer.validated_data['email']}\nPhone_num: {serializer.validated_data['phone']}\nSubject: {serializer.validated_data['subjects']}\nmessage: {serializer.validated_data['message']}",
                email, 
                ['dmmanager@meridatechminds.com'],
                fail_silently=False,
                
            )
            
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            



from .models import Job_Portal,Details
from .serializers import jobserializers,DetailSerializer


class job_ViewSet(viewsets.ModelViewSet):
    queryset = Job_Portal.objects.all()
    serializer_class = jobserializers


class DetailsViewSet(viewsets.ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = DetailSerializer
 


# from rest_framework.views import APIView     
# class details_list(APIView):
#     def get(self, request):
#         studies = Details.objects.all()
#         serializer =DetailSerializer(studies, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         # Assuming the request contains user registration data
#         serializer = DetailSerializer(data=request.data)

#         if serializer.is_valid():
#             # Save the user instance
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['POST',])
def subscription_data(request):
    if request.method=='POST':
        serializer=subscription(data=request.data)
        if serializer.is_valid():
            serializer.save()
             # Send email
            email = serializer.validated_data['email']
            subject="Subscribed By : "+email
            send_mail(
                subject,
                f"Email: {serializer.validated_data['email']}",
                ['dmmanager@meridatechminds.com'],
                fail_silently=False,
                
            )
            return Response("your mail has been registred",status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            




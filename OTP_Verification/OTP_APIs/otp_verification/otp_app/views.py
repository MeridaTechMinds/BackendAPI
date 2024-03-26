# views.py
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PhoneNumberSerializer
from .models import PhoneNumber
from django.conf import settings
from twilio.rest import Client
import random
from django.urls import reverse_lazy


def send_verification_code(phone_number, verification_code):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to=phone_number,
        from_=settings.TWILIO_PHONE_NUMBER,
        body=f'Your verification code is {verification_code}'
    )

@api_view(['POST'])
def verify_phone_number(request):
    if request.method == 'POST':
        serializer = PhoneNumberSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            name = serializer.validated_data['name']
            phone_number = "+91" + phone_number
            verification_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            send_verification_code(phone_number, verification_code)
            # Serialize the response data with the generated verification code
            phone_number_store = PhoneNumber.objects.create(
            name=name,
            phone_number=phone_number,
            verification_code=verification_code,
            )
            phone_number_store.save()
            response_data = {
                'phone_number': phone_number,
                "name":name,
                'verification_code': verification_code,
            }
           
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

a=[]
i=1
num=100
while i<=num:
    random_val=random.randrange(1,num+1)
    if random_val not in a:
        a.append(random_val)
        if len(a)==100:
            break 

@api_view(['POST'])
def verify_code(request, id):
    if request.method =="POST":
        serializer = PhoneNumberSerializer(data=request.data)
        if serializer.is_valid():
            entered_code = serializer.validated_data['verification_code']
            phone_number_store=PhoneNumber.objects.get(pk=id)
            if phone_number_store.verification_code == str(entered_code):
                phone_number_store.is_verified = True
                phone_number_store.save()
                if PhoneNumber.is_verified:
                    c = PhoneNumber.objects.get(pk=id)
                    c.count_no = c.pk
                    c.save()
                    count = a[c.count_no]
                    a.append(a[c.count_no])
                    if 1 <= count <= 100:
                        if count >= 1 and count <= 20:
                            c.offer = "15%"
                            c.save()
                            return render(request,'offer.html',{"offer":c.offer})
                        elif count >= 21 and count <= 70:
                            c.offer = "10%"
                            c.save()
                            return render(request,'offer.html',{"offer":c.offer})
                        elif count >= 71 and count <= 90:
                            c.offer = "25%"
                            c.save()
                            return render(request,'offer.html',{"offer":c.offer})
                        elif count >= 91 and count <= 95:
                            c.offer = "50%"
                            c.save()
                            return render(request,'offer.html',{"offer":c.offer})
                        elif count >= 96 and count <= 100:
                            c.offer = "80%"
                            c.save()
                            return render(request,'offer.html',{"offer":c.offer})
                        else:
                            return render(request,'offer.html',{"offer":c.offer})
            response_data = PhoneNumberSerializer(phone_number_store)
            return Response(response_data.data, status=status.HTTP_200_OK)
        




# @api_view(['GET'])
# def verify_code(request, entered_code):
#     if request.method =="GET":
#         phone_number_store=PhoneNumber.objects.get(verification_code=entered_code)
#         if phone_number_store.verification_code == str(entered_code):
#             phone_number_store.is_verified = True
#             phone_number_store.save()
#             if PhoneNumber.is_verified:
#                 c = PhoneNumber.objects.get(verification_code=entered_code)
#                 c.count_no = c.pk
#                 c.save()
#                 count = a[c.count_no]
#                 a.append(a[c.count_no])
#                 if 1 <= count <= 100:
#                     if count >= 1 and count <= 20:
#                         c.offer = "15%"
#                         c.save()
#                         return render(request,'offer.html',{"offer":c.offer})
#                     elif count >= 21 and count <= 70:
#                         c.offer = "10%"
#                         c.save()
#                         return render(request,'offer.html',{"offer":c.offer})
#                     elif count >= 71 and count <= 90:
#                         c.offer = "25%"
#                         c.save()
#                         return render(request,'offer.html',{"offer":c.offer})
#                     elif count >= 91 and count <= 95:
#                         c.offer = "50%"
#                         c.save()
#                         return render(request,'offer.html',{"offer":c.offer})
#                     elif count >= 96 and count <= 100:
#                         c.offer = "80%"
#                         c.save()
#                         return render(request,'offer.html',{"offer":c.offer})
#                     else:
#                         return render(request,'offer.html',{"offer":c.offer})
#         response_data = PhoneNumberSerializer(phone_number_store)
#         return Response(response_data.data, status=status.HTTP_200_OK)
        


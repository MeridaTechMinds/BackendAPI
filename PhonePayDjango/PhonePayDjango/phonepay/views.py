import jsons
import base64
import requests
import shortuuid
from django.shortcuts import render
from cryptography.hazmat.primitives import hashes
from django.views.decorators.csrf import csrf_exempt
from cryptography.hazmat.backends import default_backend
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
from django.core.mail import send_mail   
# views.py

@api_view(['GET', 'POST'])
def details_list(request):
    if request.method == 'GET':
        details = Details.objects.all()
        serializer = DetailSerializer(details, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DetailSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data['email']
            # Send email
            send_mail(
                'Registration Details',
                f"Name: {serializer.validated_data['name']}\nEmail: {serializer.validated_data['email']}\nPhone_num: {serializer.validated_data['phone']}\nAmount: {serializer.validated_data['amount']}",
                email, 
                ['harikrishnad76@gmail.com'],
                fail_silently=False,
                
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
########################## HELPER FUNCTION ################################
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def calculate_sha256_string(input_string):
    # Create a hash object using the SHA-256 algorithm
    sha256 = hashes.Hash(hashes.SHA256(), backend=default_backend())
    # Update hash with the encoded string
    sha256.update(input_string.encode('utf-8'))
    # Return the hexadecimal representation of the hash
    return sha256.finalize().hex()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def base64_encode(input_dict):
    # Convert the dictionary to a JSON string
    json_data = jsons.dumps(input_dict)
    # Encode the JSON string to bytes
    data_bytes = json_data.encode('utf-8')
    # Perform Base64 encoding and return the result as a string
    return base64.b64encode(data_bytes).decode('utf-8')
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
########################## Create your views here. ########################
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@api_view(['GET'])
@permission_classes([AllowAny])
@csrf_exempt
def pay(request, id):
    tid = shortuuid.uuid()
    MAINPAYLOAD = {
        "merchantId": "M220KBWVG6WTI",
        "merchantTransactionId": tid,
        "merchantUserId": "MUID123",
        "amount": int(id)*100,
        # "redirectUrl":"http://127.0.0.1:8000/phonepay/home/",
        "redirectMode": "POST",
        # "callbackUrl": "http://127.0.0.1:8000/phonepay/return-to-me/",
        "mobileNumber": "9999999999",
        "paymentInstrument": {
            "type": "PAY_PAGE",
        }
    }
    INDEX = "1"
    ENDPOINT = "/pg/v1/pay"
    SALTKEY = "79635c64-7991-4633-b727-fb8df4ad4492"
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    base64String = base64_encode(MAINPAYLOAD)
    mainString = base64String + ENDPOINT + SALTKEY;
    sha256Val = calculate_sha256_string(mainString)
    checkSum = sha256Val + '###' + INDEX;

    # # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # # Payload Send
    # # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    headers = {
        'Content-Type': 'application/json',
        'X-VERIFY': checkSum,
        'accept': 'application/json',
    }
    json_data = {
        'request': base64String,
    }
    response = requests.post('https://api.phonepe.com/apis/hermes/pg/v1/pay', headers=headers, json=json_data)
    responseData = response.json()

    # Response to the client
    return Response({'redirect_url': responseData['data']['instrumentResponse']['redirectInfo']['url']}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
@csrf_exempt
def payment_return(request):
    INDEX = "1"
    SALTKEY = "79635c64-7991-4633-b727-fb8df4ad4492"
    # Access form data in a POST request

    form_data = request.data

    # Convert form data to a dictionary

    transaction_id = form_data.get('transactionId', None)
    # 1. In the live, please match the amount you get by the amount you send also so that a hacker can't pass a static value.
    # 2. Don't take Marchent ID directly validate it with your Marchent ID
    if transaction_id:
        request_url = f'https://api.phonepe.com/apis/hermes/pg/v1/status/M220KBWVG6WTI/{transaction_id}'
        sha256_Pay_load_String = f'/pg/v1/status/M220KBWVG6WTI/{transaction_id}{SALTKEY}'
        sha256_val = calculate_sha256_string(sha256_Pay_load_String)
        checksum = sha256_val + '###' + INDEX

        # Payload Send

        headers = {
            'Content-Type': 'application/json',
            'X-VERIFY': checksum,
            'X-MERCHANT-ID': transaction_id,
            'accept': 'application/json',
        }
        response = requests.get(request_url, headers=headers)
        

        return Response({'output': response.text, 'main_request': form_data}, status=status.HTTP_200_OK)

    return Response({'error': 'transactionId not provided'}, status=status.HTTP_400_BAD_REQUEST)













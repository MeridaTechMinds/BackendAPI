from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from twilio.rest import Client
from .forms import PhoneNumberForm
from .models import PhoneNumber
import copy
import random

def send_verification_code(phone_number, verification_code):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to=phone_number,
        from_=settings.TWILIO_PHONE_NUMBER,
        body=f'Your verification code is {verification_code}'
    )

def verify_phone_number(request):
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            name=form.cleaned_data['name']
            name=name.capitalize()
            phone_number="+91"+phone_number
            otps=''.join([str(random.randint(0, 9)) for _ in range(6)])
            verification_code = otps 
            new_phone_number = PhoneNumber.objects.create(phone_number=phone_number, verification_code=verification_code,name=name)
            send_verification_code(phone_number, verification_code)

            messages.success(request, 'Verification code sent successfully!')
            return redirect('verification_app:verify_code', phone_number_id=new_phone_number.id)
    else:
        form = PhoneNumberForm()
    return render(request, 'verify_phone_number.html', {'form': form})

a=[]
i=1
num=100
while i<=num:
    random_val=random.randrange(1,num+1)
    if random_val not in a:
        a.append(random_val)
        if len(a)==100:
            break 

def verify_code(request, phone_number_id):
    phone_number = get_object_or_404(PhoneNumber, pk=phone_number_id)

    if request.method == 'POST':
        entered_code = request.POST.get('verification_code')

        if entered_code == phone_number.verification_code:
            phone_number.is_verified = True
            phone_number.save()
            if phone_number.is_verified:
                c=PhoneNumber.objects.get(pk=phone_number_id)
                c.count_no=c.pk
                c.save()
                count=a[c.count_no]
                a.append(a[c.count_no])
                # l=["name",'phone_number','count_no','is_verified','offer','verification_code']
                if 1 <= count <= 100:
                    if count >= 1 and count <= 20:
                        c.offer="15%"
                        c.save()
                        
                        return render(request,'offer.html',{"offer":c.offer})
                    elif count >= 21 and count <= 70:
                        c.offer="10%"
                        c.save()
                        return render(request,'offer.html',{"offer":c.offer})
                    elif count >= 71 and count <= 90:
                        c.offer="25%"
                        c.save()
                        
                        return render(request,'offer.html',{"offer":c.offer})
                    elif count >= 91 and count <= 95:
                        c.offer="50%"
                        c.save()
                        
                        return render(request,'offer.html',{"offer":c.offer})
                    elif count >= 96 and count <= 100:
                        c.offer="80%"
                        c.save()
                        
                        return render(request,'offer.html',{"offer":c.offer})
                    else:
                        return render(request,'offer.html',{"offer":c.offer})
                # else:
                #     return HttpResponse("Phone number verified successfully!",)
        else:
            messages.error(request, 'Invalid verification code. Please try again.')
    return render(request, 'verify_code.html', {'phone_number': phone_number})


from django.shortcuts import render
import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.core.files import File

def generate_qr_code(request):
    # Create a QRCode instance
    url = 'https://www.youtube.com/watch?v=RsN0aXfPR1E&ab_channel=GeeksforGeeks'

    qr = qrcode.QRCode(
        version=1,
        box_size=40,
        border=5,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="blue", back_color="white")

    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)
    content_type='image/png'
    return render(buffer,{"qr":content_type})

    return HttpResponse(buffer, content_type='image/png')

from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_202_ACCEPTED, HTTP_226_IM_USED, HTTP_406_NOT_ACCEPTABLE, HTTP_401_UNAUTHORIZED, HTTP_200_OK
import random
from threading import Thread
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password, check_password
from .models import Customer
from .seriallizer import CustomarSerializer

# email imports
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sign_up(request):
    return render(request, "signUp.html")

def sign_in(request):
    return render(request, "signIn.html")

def verify_email(request, OTP, user_name):
    return render(request, "verifyEmail.html")


# OTP send by email


def send_mail(to, subject, body):

    smtp_server = 'smtp.gmail.com'
    smtp_port = '465'
    sender_email = 'mushroomyan01@gmail.com'
    sender_password = 'fjjvrpvxrrubkbsg'
    server = None

    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.ehlo()
        server.login(sender_email, sender_password)
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to
        msg['Subject'] = subject


        html = """\
        <html>
            <head></head>
            <body>
        """
        html += body.replace('\r\n', '<br/>\r\n')
        """
            </body>
        </html>
        """
        msg.attach(MIMEText(html, 'html'))
        server.sendmail(
            from_addr=sender_email,
            to_addrs=to,
            msg=msg.as_string())
        print("Mail Send")
    except Exception as ex:
        print(str(ex))
    finally:
        if server != None:
            server.quit()


def thread_send_email(to, subject, body):

    thread = Thread(target=send_mail, args=(to, subject, body))
    thread.start()




# APIs


class ApiSignUp(CreateAPIView):

    permission_classes = []

    def post(self, request):

        result = {}

        try:
            data = json.loads(request.body)

            if 'full_name' not in data or data['full_name'] == '':
                result['massage'] = "Name can not be null."
                result['error'] = "Full name"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'email' not in data or data['email'] == '':
                result['massage'] = "Email can not be null."
                result['error'] = "Email"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'phone_number' not in data or data['phone_number'] == '':
                result['massage'] = "Phone number can not be null."
                result['error'] = "Phone number"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'password' not in data or data['password'] == '':
                result['massage'] = "Password can not be null."
                result['error'] = "Password"
                return Response(result, status=HTTP_400_BAD_REQUEST)

            user = User.objects.filter(username=data['phone_number']).first()

            if not user:

                user = User()
                user.username = data['phone_number']
                user.first_name = data['full_name']
                user.password = make_password(data['password'])
                user.is_active = False
                user.save()

                random_number = random.randint(000000, 999999)
                customer = Customer()
                customer.full_name = data['full_name']
                customer.email = data['email']
                customer.phone_number = data['phone_number']
                customer.user = user
                customer.otp = random_number
                customer.save()

                # thread_send_otp(data['phone_number'], random_number)
                thread_send_email(data['email'], 'your OTP', 'OTP : '+str(random_number)+" \n or \nclick this link 127.0.0.1:8000/user/verify_email/"+str(random_number)+"/"+str(data['phone_number']))

                result['status'] = HTTP_202_ACCEPTED
                result['massage'] = "Success"
                result['phone_number'] = data['phone_number']
                result['email'] = data['email']
                return Response(result)
            else:
                result['status'] = HTTP_226_IM_USED
                result['massage'] = "This phone number is already have a account"
                return Response(result)

        except Exception as ex:
            result['massage'] = str(ex)
            return Response(result)


class ApiOTPCheck(CreateAPIView):

    permission_classes = []

    def put(self, request):

        result = {}
        try:
            data = json.loads(request.body)

            if 'phone_number' not in data or data['phone_number'] == '':
                result['massage'] = "Phone number can not be null."
                result['error'] = "Phone number"
                return Response(result, status=HTTP_400_BAD_REQUEST)

            if 'otp' not in data or data['otp'] == '':
                result['massage'] = "otp can not be null."
                result['error'] = "OTP"
                return Response(result, status=HTTP_400_BAD_REQUEST)

            user = User.objects.filter(username=data['phone_number']).first()
            if not user:

                result['massage'] = "Please create a account."
                return Response(result, status=HTTP_406_NOT_ACCEPTABLE)

            elif user.is_active:

                result['massage'] = "You already created account."
                return Response(result, status=HTTP_226_IM_USED)

            else:
                customer = Customer.objects.filter(user=user).first()
                if customer.otp == data['otp']:
                    user.is_active = True
                    user.save()
                    customer.otp = ''
                    customer.save()
                    result['massage'] = "Success."
                    result['status'] = HTTP_202_ACCEPTED
                    return Response(result)

                else:

                    result = {}
                    result['status'] = HTTP_400_BAD_REQUEST
                    result['massage'] = "OTP did not match."
                    result['Error'] = "OTP"
                    return Response(result)

        except Exception as ex:
            result = {}
            result['massage'] = str(ex)
            return Response(result)


class ApiLogIn(ListAPIView):

    permission_classes = []

    def post(self, request, *args, **kwargs):
        result = {}

        try:
            data = json.loads(request.body)
            if 'phone_number' not in data or data['phone_number'] == '':
                result['message'] = "Email can not be null."
                result['Error'] = "Email"
                return Response(result, status=HTTP_400_BAD_REQUEST)

            if 'password' not in data or data['password'] == '':
                result['message'] = "Password can not be null."
                result['Error'] = "Password"
                return Response(result, status=HTTP_400_BAD_REQUEST)

            user = User.objects.filter(username=data['phone_number']).first()
            if not user:
                result['message'] = "Please create a account."
                return Response(result, status=HTTP_400_BAD_REQUEST)
            elif not user.is_active:
                result['message'] = "Please active your account."
                return Response(result, status=HTTP_400_BAD_REQUEST)
            else:
                if not check_password(data['password'], user.password):
                    result['message'] = "Wrong password"
                    return Response(result, status=HTTP_401_UNAUTHORIZED)
                else:
                    customer = Customer.objects.filter(user=user).first()
                    token = RefreshToken.for_user(user)
                    data = {}
                    data['user_name'] = user.username
                    data['full_name'] = customer.full_name
                    data['access'] = str(token.access_token)
                    data['token'] = str(token)
                    data['status'] = HTTP_200_OK

                    return Response(data)

        except Exception as e:
            print("exp")
            result['message'] = str(e)
            return Response(result)

class CustomarDetailsApi(ListAPIView):

    premission_class = [IsAuthenticated]

    def get(self, request, slug):

        customer_data = Customer.objects.filter(slug=slug).first()
        customer_data = CustomarSerializer(customer_data).data
        return Response(customer_data)
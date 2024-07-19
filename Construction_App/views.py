from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import SetPasswordForm
# from django.utils.encoding import force_text
# from django.utils.encoding import force_text
from django.utils.encoding import force_bytes,force_str

from django.utils.http import urlsafe_base64_decode
from Construction_App.forms import CustomPasswordResetForm
from Construction_App.models import Contractor_Registration, UserType, Category, worker_Registration
from django.contrib import messages


# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'


class Login(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            if user.is_active:                
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "contractor":
                    return redirect('/contractor')
                elif UserType.objects.get(user_id=user.id).type == "worker":
                    return redirect('/worker')

            else:
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})


        else:
            return render(request, 'login.html', {'message': "Invalid Username or Password"})

class Contractor_Reg(TemplateView):
    template_name = 'con_registration.html'

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        address = request.POST['address']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            return render(request, 'con_registration.html', {'message': "Email already exists."})
        else:
            # Create a user with is_active=False
            user = User.objects.create_user(username=email, password=password, email=email, first_name=name,
                                             is_staff=False, is_active=False)
            user.save()

            # Create Manager_Reg instance
            manager_reg = Contractor_Registration(user=user, address=address, phonenumber=phonenumber)
            manager_reg.save()

            # Create UserType instance
            user_type = UserType(user=user, type="contractor")
            user_type.save()

            # Send email verification
            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            message = render_to_string('activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()

            return render(request, 'verify_email.html', {'email': email})


class Worker_Reg(TemplateView):
    template_name = 'worker_reg.html'

    def get_context_data(self, **kwargs):
        categ = Category.objects.all()
        context = {
            'category': categ
        }
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        address = request.POST['address']
        phonenumber = request.POST['phonenumber']
        category = request.POST['category']

        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            return render(request, 'reg.html', {'message': "Email already exists."})
        else:
            # Create a user with is_active=False
            user = User.objects.create_user(username=email, password=password, email=email, first_name=name,
                                             is_staff=False, is_active=False)
            user.save()

            # Create Manager_Reg instance
            manager_reg = worker_Registration(user=user, address=address,category_id=category,phonenumber=phonenumber,status="Available")
            manager_reg.save()

            # Create UserType instance
            user_type = UserType(user=user, type="worker")
            user_type.save()

            # Send email verification
            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            message = render_to_string('activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()

            return render(request, 'verify_email.html', {'email': email})

def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'index.html')  # Render a success message after activation
    else:
        return HttpResponse('Activation link is invalid or expired.')


def reset_password_view(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

            reset_link = f"{request.scheme}://{request.META['HTTP_HOST']}/reset-password-confirm/{uidb64}/{token}/"
            mail_subject = 'Reset Your Password'
            message = render_to_string('password_reset_email.html', {
                'reset_link': reset_link,
            })
            email = EmailMessage(mail_subject, message, to=[email])
            email.send()

            return render(request, 'password_reset_done.html')
    else:
        form = CustomPasswordResetForm()

    return render(request, 'reset_password.html', {'form': form})


def reset_password_confirm_view(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your password has been successfully reset.')
                return redirect('login')  # Redirect to login page upon successful password reset
        else:
            form = SetPasswordForm(user)

        return render(request, 'reset_password_confirm.html', {'form': form})
    else:
        messages.error(request, 'Invalid password reset link.')
        return redirect('login')  # Redirect to login page if the password reset link is invalid
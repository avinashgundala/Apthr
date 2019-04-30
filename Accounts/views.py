from django.shortcuts import render,redirect

#----------- import HttpResponse---------#
from django.http import HttpResponse

######## importing SingnUpform #######
from Accounts.forms import UserSignupForm,ProfileForm,LoginForm,FeedBackForm,ActivationEmailForm
#from Accounts.forms import  ContactUsForm

#---------- importing messages ----------#
from django.contrib import messages

######### login required #########
from django.contrib.auth.decorators import login_required

#------------ Smtp email send ---------------#
from django.core.mail import EmailMultiAlternatives

#---------- importing models -----------#
from Accounts.models import UserProfile

#----------importing token -----------#
from Accounts.tokens import account_activation_token

#----------- importing utils ------------#
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string

#------------- getting current site domain --------------#
from django.contrib.sites.shortcuts import get_current_site

#----- importing --------#
from Accounts.models import User
from django.contrib.auth import authenticate,login as auth_login

#------ import JsonResponse --- #
from django.http import JsonResponse



def register(request):

    if request.method == 'POST':
        u_form = UserSignupForm(request.POST)
        p_form = ProfileForm(request.POST, request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            user_form = u_form.save(commit = False)
            user_form.user_type = 'Employer'
            user_form.save()
            profile = UserProfile.objects.get(user=user_form)
            profile.industry = p_form.cleaned_data['industry']
            profile.company_name = p_form.cleaned_data['company_name']
            #profile.company_size = p_form.cleaned_data['company_size']
            profile.contact_no = p_form.cleaned_data['contact_no']
            profile.company_type = p_form.cleaned_data['company_type']
            profile.city = p_form.cleaned_data['city']
            profile.postcode = p_form.cleaned_data['postcode']
            profile.country = p_form.cleaned_data['country']
            profile.company_logo = p_form.cleaned_data['company_logo']
            profile.save()
            messages.success(request,f'successfully registered Please login')

            #---------- sending user details to admin ------------#

            mail_subject_admin = "New User"
            message_admin = render_to_string('Email_Template/aptahr_New_User_Alert.html',{
                             'profile':profile,
            })
            to_email_admin = list(User.objects.filter(is_staff=True).values_list('email',flat=True))
            email_admin = EmailMultiAlternatives(mail_subject_admin,message_admin,to=to_email_admin)
            email_admin.attach_alternative(message_admin,"text/html")
            email_admin.send()


            #---------- sending registerlink to registered user ---------#

            current_site = get_current_site(request)
            mail_subject = 'Activate your Account'
            message = render_to_string('Email_Template/aptahr_activation_link.html',{
                    'user': user_form,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user_form.pk)),
                    'token': account_activation_token.make_token(user_form),
            })
            to_email = user_form.email
            email = EmailMultiAlternatives(mail_subject,message,to=[to_email])
            email.attach_alternative(message,"text/html")
            email.send()

            return redirect('registration_success')

    else:
        u_form = UserSignupForm()
        p_form = ProfileForm()
    context = {
                'u_form':u_form,
                'p_form':p_form
             }
    return render(request,'Index_Template/register.html',context)

#--------------------- activate funtion to activate--------#

def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user,token):
        user.email_confirmed = True
        user.save()
        #login(request,user)
        return redirect('activation_success')
    else:
        messages.error(request,'This link is used')
        return redirect('activation_success')

def validate_email(request):
    email = request.GET.get('email',None)
    data ={
              'is_taken': User.objects.filter(email__iexact = email).exists()
    }
    print(data['is_taken'])
    return JsonResponse(data)


def landingpage(request):

    if request.POST:
        form_type = request.POST.get('form_name','')
        if form_type == 'feedback':
            feedback_form = FeedBackForm(request.POST)
            if feedback_form.is_valid():
                feedback = feedback_form.save(commit= False)
                feedback.save()
                #------------- mailing to admin ----#
                mail_subject_admin = ""
                message_admin = render_to_string('Email_Template/aptahr_admin_feedback_email.html',{
                                                    'feedback':feedback
                })
                to_email = list(User.objects.filter(is_staff=True).values_list('email',flat=True))
                email = EmailMultiAlternatives(mail_subject_admin,message_admin,to=to_email)
                email.attach_alternative(message_admin,"text/html")
                email.send()
                #----------- mailling to user -----#

                mail_subject_user = ""
                message_user = render_to_string('Email_Template/aptahr_user_feedback_email.html',{
                                        'feedback':feedback
                })
                to_email_user = feedback.email
                email_user = EmailMultiAlternatives(mail_subject_user,message_user,to=[to_email_user])
                email_user.attach_alternative(message_user,"text/html")
                email_user.send()
                return redirect('landingpage')
            else:
                feedback_form = FeedBackForm()
        elif form_type == 'loginform':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                email = login_form.cleaned_data['email']
                email = email.lower()
                password =  login_form.cleaned_data['password']
                user = authenticate(username=email, password=password)
                if user is not None:
                    if user.is_active:
                        if user.user_type == 'Admin':
                            auth_login(request,user)
                            if 'next' in request.GET and request.GET['next']:
                                return redirect(request.GET['next'])
                            return redirect('admin')
                        if user.user_type == 'Employer':
                            auth_login(request,user)
                            if 'next' in request.GET and request.GET['next']:
                                return redirect(request.GET['next'])
                            return redirect('dashboard')
                        else:
                            return redirect('landingpage')
                    else:
                        messages.add_message(request,messages.ERROR,'Your Account is not Activated admin will active your account with in 24 hours.')
                else:
                    messages.add_message(request,messages.ERROR,'Your Email or Password is Incorrect.')
            else:
                 login_form = LoginForm()
        else:
            feedback_form = FeedBackForm()
            login_form = LoginForm()

    else:
        feedback_form = FeedBackForm()
        login_form = LoginForm()

    context = {
                 "login_form":login_form,
                 "feedback_form":feedback_form,
             }
    return render(request, 'Index_Template/landing.html', context)

def dashboard(request):
    return render(request,'Index_Template/dashboard.html')

def registration_success(request):
    return render(request,'Index_template/registration_success.html')

def register_resent_active(request):
    return render(request,'Index_Template/new_activation_link.html')

def activation_success(request):
    return render(request,'Index_Template/activation_success.html')

def activationemail(request):
    if request.method == 'POST':
        activationform = ActivationEmailForm(request.POST)
        if activationform.is_valid():
            email = activationform.cleaned_data['email']
            try:
                user = User.objects.get(email = email)
            except user.DoesNotExist:
                raise messages.error(request,'Email address Does not exit')
            current_site = get_current_site(request)
            mail_subject = 'Activate your Account'
            message = render_to_string('Email_Template/aptahr_activation_link.html',{
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
            })
            to_email = email
            email_to = EmailMultiAlternatives(mail_subject,message,to=[to_email])
            email_to.attach_alternative(message,"text/html")
            email_to.send()
            messages.success(request,'Email Sent successfully')
            return redirect('register_resent_active')

    else:
        activationform = ActivationEmailForm()
    return render(request,'Index_Template/new_activation_link.html',{'activationform':activationform})

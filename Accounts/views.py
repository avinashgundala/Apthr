from django.shortcuts import render,redirect

######## importing SingnUpform #######
from Accounts.forms import UserSignupForm,ProfileForm

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
            profile.company_size = p_form.cleaned_data['company_size']
            profile.address = p_form.cleaned_data['address']
            profile.state = p_form.cleaned_data['state']
            profile.city = p_form.cleaned_data['city']
            profile.postcode = p_form.cleaned_data['postcode']
            profile.country = p_form.cleaned_data['country']
            profile.company_logo = p_form.cleaned_data['company_logo']
            profile.save()
            messages.success(request,f'successfully registered Please login')

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

            return redirect('login')
    else:
        u_form = UserSignupForm()
        p_form = ProfileForm()
    context = {
                'u_form':u_form,
                'p_form':p_form
             }
    return render(request,'Index_Template/register.html',context)

#--------------------- activate funtion to activate--------#

'''def activate(request,uibd64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):'''


def login(request):
    return render(request,'Index_Template/login.html')

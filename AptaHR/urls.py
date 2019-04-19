from django.contrib import admin
from django.urls import path,re_path,include

########### import setting ############
from django.conf import settings
from django.conf.urls.static import static

########### import default viewe ############
from django.contrib.auth import views as auth_views
########## import Accounts Views ############
from Accounts import views as acc_views

urlpatterns = [
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='admin_password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('',include('Accounts.urls')),
    # path('',include('Accounts.urls')),
    path('register/',acc_views.register,name='register'),

    path('admin/', admin.site.urls),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

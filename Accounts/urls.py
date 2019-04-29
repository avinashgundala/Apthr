from django.urls import path,re_path

########### import viewe ############
from Accounts import views

urlpatterns = [
    #path('', views.login,name='login'),
    path('',views.landingpage,name='landingpage'),
    #path('',views.landingpage,name='landingpage'),
    path('ajax/validate_username/', views.validate_email, name='validate_email'),
    path('dashboard/',views.dashboard,name='dashboard'),
]

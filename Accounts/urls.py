from django.urls import path,re_path

########### import viewe ############
from Accounts import views

urlpatterns = [
    # path('', views.landingpage,name='landingpage'),
    path('login/',views.login,name='login'),
]


from django.urls import path
from .views import *
urlpatterns = [
    path('',login_page,name='login'),
    path('register/',register,name='register'),
    path('home/',home,name='home'),

    path('token/',token,name='token'),
    path('verify/<auth_token>',verify_mail,name='verify'),#verify
    path('forget/',forget,name='forget'),
    path('edit/<int:id>',edit,name='edit'),
    path('delete/<int:id>',delete,name='delete'),
    path('bmi/',bmi),
    # path('send/',send)
]
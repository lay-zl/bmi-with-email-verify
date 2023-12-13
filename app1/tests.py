from django.test import TestCase
from django.urls import resolve,reverse
from .views import *
from .models import CustomUser
from django.contrib.auth.models import User
# Create your tests here.
from django.contrib.auth import get_user
from django.urls import reverse

class LoginTest(TestCase):
    def setUp(self) -> None:
        self.user=CustomUser.objects.create_user(username='abc',email='a@gmail.com')
        self.user.set_password('12345')
        self.user.save()

    def test_sucess(self):
        l_u = reverse('login')
        data = {'User Name':self.user.username,'Password':self.user.password}
        respons = self.client.post(l_u,data)
        self.assertRedirects(respons,reverse('home'))


    # def test_url(self):
    #     rs = self.client.get('http://127.0.0.1:8000/')
    #     self.assertEqual(rs.status_code,200)
    #
    # # def test_post_data(self):
    # #     rs = self.client.post('http://127.0.0.1:8000/',data={
    # #         'username':'abc',
    # #         'password' : '12345'
    # #     })
    #
    # def test_url_all(self):
    #     url=reverse('login')
    #     url1=reverse('register')
    #     url2=reverse('home')
    #     url3=reverse('token')
    #     url4=reverse('verify',args=[123456])
    #     url5=reverse('forget')
    #     url6=reverse('edit',args=[1])
    #     url7=reverse('delete',args=[1])
    #     self.assertEqual(resolve(url).func,login_page)
    #     self.assertEqual(resolve(url1).func,register)
    #     self.assertEqual(resolve(url2).func,home)
    #     self.assertEqual(resolve(url3).func,token)
    #     self.assertEqual(resolve(url4).func,verify_mail)
    #     self.assertEqual(resolve(url5).func,forget)
    #     self.assertEqual(resolve(url6).func,edit)
    #     self.assertEqual(resolve(url7).func,delete)

    def test_login(self):
        us = CustomUser.objects.get(username='abc')
        rs = self.client.post('http://127.0.0.1:8000/',{
            'username':'abc',
            'password':'12345'
        })
        print(rs.context)
        # self.assertEqual(rs.status_code,302)
        # self.assertEqual(rs[0][5], "Login Successful !!")
        #self.assertEqual(rs[0][3], "Login Successful !!")


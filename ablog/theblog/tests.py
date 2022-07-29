from urllib import response
from django.test import TestCase,SimpleTestCase
import json
from django.contrib.auth.models import User
from django.urls import reverse,resolve
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase,APIClient

from theblog.views import ApiView
#from ..theblog.serializers import UserSerializer,PostSerializer
#from ..theblog.models import User,Post
# Create your tests here.
'''
class TestAddUser(APITestCase):

    def test_add(self):
        data={'title':'Testapi','title_tag':'test','author':'1','body':'body','category':'Nature','snippet':'sn'}
        response =self.client.post("/api/",data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)'''

class ApiUrlTest(SimpleTestCase):
    #Check url go to right view
    def test_get_addpost(self):
        url=reverse('api')
        #print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ApiView)

class AddPostApiTest(APITestCase):

    add_post_urls=reverse('api')
    # For Authentication
    def setUp(self):
       # {'title':'UNIT_Testapi','title_tag':'test','author':'1','body':'body','category':'Nature','snippet':'sn'}
        self.user=User.objects.create_user(username='admin2',password='admin2')
        #create token
        self.token=Token.objects.create(user=self.user)
        # assign token
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
    
    def tearDown(self):
        pass

    def test_get_user_authenticated(self):
        response=self.client.get(self.add_post_urls)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_get_user_un_authenticated(self):
        self.client.force_authenticate(user=None,token=None)
        response=self.client.get(self.add_post_urls)
        self.assertEqual(response.status_code,401)      

    def test_post_addpost(self):
        data={'title':'UNIT_Testapi','title_tag':'test','author':1,'body':'body','category':'Nature','snippet':'sn'}
        response=self.client.post(self.add_post_urls,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        #self.assertEqual(response.data['title_tag'],'test')

class ProfileTest(APITestCase):
    url=reverse('users')

    def setUp(self):
        self.user=User.objects.create_user(username='admin',password='admin')
        #create token
        self.token=Token.objects.create(user=self.user)
        # assign token
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    def tearDown(self):
        pass

    def test_get_profile(self):
        response=self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_post_profile(self):
        data={'username':'apiname','first_name':'api','last_name':'name','email':'apiuser@gmail.com','password':'Nitesh@13'}
        response=self.client.post(self.url,data,format='json')
        print("2222222222222",response)
        self.assertEqual(response.status_code,200)

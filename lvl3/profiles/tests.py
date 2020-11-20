import json
import sys

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from profiles.api.serializers import ProfileSerializer, ProfileStatusSerializer
from profiles.models import Profile, ProfileStatus

class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            "username": "testcase",
            "email": "test@localhost.app",
            "password1": "some_strong_pws",
            "password2": "some_strong_pws",
        }

        rs = self.client.post("/api/rest-auth/registration/", data=data)
        self.assertEqual(rs.status_code, status.HTTP_201_CREATED)


class ProfileViewSetTestCase(APITestCase):
    
    list_url = reverse("profile-list")

    def setUp(self):
        self.user = User.objects.create_user(username="davinci",
                                             password="somefasdofjasodfij")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token "+self.token.key)

    def test_profile_list_authenticated(self):
        rs = self.client.get(self.list_url)
        self.assertEqual(rs.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        rs = self.client.get(self.list_url)
        self.assertEqual(rs.status_code, status.HTTP_403_FORBIDDEN)

    def test_profile_detail_retrieve(self):
        rs = self.client.get(reverse("profile-detail", kwargs={"pk": self.user.id}))
        self.assertEqual(rs.status_code, status.HTTP_200_OK)
        self.assertEqual(rs.data["user"], "davinci")

    def test_profile_update_by_owner(self):
        rs = self.client.put(reverse("profile-detail", kwargs={"pk": self.user.id}),
                             {"city": "city", "bio": "bio"})
        self.assertEqual(rs.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(rs.content),
                         {"id": self.user.id, "user": "davinci", "bio": "bio",
                          "city": "city", "avatar": None})

    def test_profile_update_by_random_user(self):
        random_user = User.objects.create_user(username="random", password="dfasdfasdf")
        self.client.force_authenticate(user=random_user)
        rs = self.client.put(reverse("profile-detail", kwargs={"pk": self.user.id}),
                             {"city": "city", "bio": "bio"})
        self.assertEqual(rs.status_code, status.HTTP_403_FORBIDDEN)


class ProfileStatusViewSetTestCase(APITestCase):
    
    url = reverse("status-list")

    def setUp(self):
        self.user = User.objects.create_user(username="davinci",
                                             password="somefasdofjasodfij")
        self.status = ProfileStatus.objects.create(user_profile=self.user.profile,
                                                    status_content="status test")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token "+self.token.key)

    def test_status_list_authenticated(self):
        rs = self.client.get(self.url)
        self.assertEqual(rs.status_code, status.HTTP_200_OK)

    def test_status_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        rs = self.client.get(self.url)
        self.assertEqual(rs.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_status_create(self):
        data = {"status_content": "a new status!"}
        rs = self.client.post(self.url, data)
        self.assertEqual(rs.status_code, status.HTTP_201_CREATED)
        self.assertEqual(rs.data['user_profile'], 'davinci')
        self.assertEqual(rs.data['status_content'], 'a new status!')

    def test_single_status_retrieve(self):
        serializer_data = ProfileStatusSerializer(instance=self.status).data
        rs = self.client.get(reverse('status-detail', kwargs={'pk': self.status.id}))
        self.assertEqual(rs.status_code, status.HTTP_200_OK)
        rs_data = rs.json()
        self.assertEqual(serializer_data, rs_data)

    def test_status_update_owner(self):
        data = {"status_content": "content updated"}
        rs = self.client.put(reverse("status-detail", kwargs={'pk': self.status.id}),
                             data=data)
        self.assertEqual(rs.status_code, status.HTTP_200_OK)
        self.assertEqual(rs.data['status_content'], 'content updated')

    def test_status_update_random_user(self):
        random_user = User.objects.create(username="random", password="dfasdfasdf")
        self.client.force_authenticate(user=random_user)
        data = {"status_content": "you have been hacked"}
        url = reverse("status-detail", kwargs={'pk': self.status.id})
        rs = self.client.put(url,
                             data=data)
        self.assertEqual(rs.status_code, status.HTTP_403_FORBIDDEN)



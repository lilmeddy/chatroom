from django.test import TestCase
from django.test import TestCase, Client
from django.contrib.auth.models import User
from chatapp.models import *
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.

class ChatAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")
        self.chatroom = Rooms.objects.create(name="Test Room", topic="Django Testing", creator=self.user)

    def test_user_authentication(self):
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'password123'})
        self.assertEqual(response.status_code, 200)
        self.client.logout()
        response = self.client.get('/profile/')
        self.assertNotEqual(response.status_code, 200)  # Should redirect if not logged in

    def test_chatroom_creation(self):
        response = self.client.post('/create-room/', {'name': 'New Room', 'topic': 'Testing'})
        self.assertEqual(response.status_code, 302)  # Redirects on success
        self.assertTrue(Rooms.objects.filter(name="New Room").exists())

    def test_send_message(self):
        response = self.client.post(f'/chatroom/{self.chatroom.id}/', {'message': 'Hello World'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Messages.objects.filter(content="Hello World", chatroom=self.chatroom).exists())

    def test_ai_interaction(self):
        response = self.client.post(f'/chatroom/{self.chatroom.id}/', {'message': '@eckert What is Django?'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "AI Response")  # Assuming the AI sends back a response

    def test_document_upload(self):
        test_file = SimpleUploadedFile("testfile.txt", b"Hello, this is a test file.")
        response = self.client.post('/upload-document/', {'file': test_file})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('testfile.txt' in response.content.decode())

    def test_profile_update(self):
        response = self.client.post('/profile/edit/', {'username': 'newuser', 'email': 'newuser@example.com'})
        self.assertEqual(response.status_code, 302)  # Redirects on success
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'newuser')
        self.assertEqual(self.user.email, 'newuser@example.com')


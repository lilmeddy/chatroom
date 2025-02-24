from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Rooms(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    documents = models.FileField(upload_to="filesd", null=True, blank=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    profile_id = models.UUIDField(unique=True, default=uuid.uuid4)
    user = models.OneToOneField(User, related_name="topic_user", on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, blank=True, null=True)
    profile_picture = models.ImageField(default="hinata.jpg")
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Messages(models.Model):
    body = models.TextField(max_length=500)
    owner = models.ForeignKey(User, related_name="message_user", on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room.name
class ChatbotTopic(models.Model):
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, related_name="chatbot_topics", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Chat(models.Model):
    chat_id = models.UUIDField(unique=True, default=uuid.uuid4)
    title = models.CharField(max_length=20, blank=True, null=True)

class Chatbot(models.Model):
    user =models.ForeignKey(User, related_name="chat_user", on_delete=models.CASCADE, null=True)
    message = models.TextField()
    response = models.TextField()
    topic = models.ForeignKey(ChatbotTopic, related_name="messages", on_delete=models.CASCADE, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    chat_bot = models.ForeignKey(Chat, related_name="chat", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'




    
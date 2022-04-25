from django.db import models
from chat.models import Chat

# Create your models here.

class ChatMessages(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    name = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f"{self.chat.room_name}-{self.name}"

    
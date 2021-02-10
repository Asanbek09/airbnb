from django.db import models
from core import models as core_models

class Conversations(core_models.TimeStampedModel):
    """ Conversations Model Definition """
    participants = models.ManyToManyField("users.User", related_name="conversations", blank=True)

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "NUmber of Messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "NUmber of Participants"

    class Meta:
        verbose_name = "Conversation"

class Message(core_models.TimeStampedModel):
    """ Message Model Conversation """
    message = models.TextField()
    user = models.ForeignKey("users.User", related_name="messages", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversations", related_name="messages", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.message}"
from django.db import models
from django.utils import timezone


class Mailing(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    message_text = models.TextField()
    operator_code = models.CharField(max_length=10)
    tag = models.CharField(max_length=255)

    def __str__(self):
        return f"Mailing {self.id}"


class Client(models.Model):
    phone_number = models.CharField(max_length=12)
    operator_code = models.CharField(max_length=10)
    tag = models.CharField(max_length=255)
    timezone = models.CharField(max_length=255)

    def __str__(self):
        return f"Client {self.id}"


class Message(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failure', 'Failure'),
    )

    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"Message {self.id}"

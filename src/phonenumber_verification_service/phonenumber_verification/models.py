from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Verification(models.Model):
    phone_number = PhoneNumberField(max_length=10, null=False, blank=False)
    connection_id = models.UUIDField()
    invite_url = models.URLField(max_length=2000)

class SessionState(models.Model):
    connection_id = models.UUIDField()
    state = models.TextField()
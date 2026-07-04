from django.db import models
import uuid
from users.models import User
# Create your models here.

class Ticket(models.Model):
    STATUS = {
        ('Pending', "Pending"),
        ('Active', 'Active'),
        ('Completed', 'Completed'),
    }

    number = models.CharField(max_length=100, default=uuid.uuid4 )
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    is_resolved = models.BooleanField(default=False)
    accepted_date = models.DateTimeField(null=True, blank=True)
    closed_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return self.title

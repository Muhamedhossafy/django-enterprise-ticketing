from django.contrib.auth.forms import UserCreationForm
from .models import *

class ResgisterCustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
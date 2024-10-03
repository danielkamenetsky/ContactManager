from django.db import models
from django.contrib.auth.models import User
import uuid

class Transaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    transaction_id = models.CharField(max_length=100, unique=True, default=uuid.uuid4, editable=False)
    ticker = models.CharField(max_length=50)
    exchange = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=5)
    price = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.ticker} - {self.transaction_id}"
    
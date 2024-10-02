import uuid
from django.db import models

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=100, unique=True, default=uuid.uuid4, editable=False)
    ticker = models.CharField(max_length=50)  # e.g., 'Bitcoin', 'Ethereum'
    exchange = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=5)
    price = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.ticker} - {self.transaction_id}"
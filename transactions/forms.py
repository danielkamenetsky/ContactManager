from django import forms
from .models import Transaction 

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_id', 'ticker', 'exchange', 'amount', 'price', 'date']

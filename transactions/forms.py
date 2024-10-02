from django import forms
from .models import Transaction 

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['ticker', 'exchange', 'amount', 'price', 'date']
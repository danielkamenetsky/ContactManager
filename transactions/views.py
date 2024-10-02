from django.shortcuts import render, redirect, get_object_or_404

from.models import Transaction
from .forms import TransactionForm



def home(request):
    return render(request, 'transactions/home.html')



def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})


def transaction_detail(request, transaction_id):  
    transaction = get_object_or_404(Transaction, transaction_id=transaction_id)
    return render(request, 'transactions/transaction_detail.html', {'transaction': transaction})  # Passing 'transaction'




def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            return redirect('transaction_detail', transaction_id=transaction.transaction_id)
    else:
        form = TransactionForm()
    return render(request, 'transactions/add_transaction.html', {'form': form})

def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, transaction_id=transaction_id)
    transaction.delete()
    messages.success(request, f"Successfully deleted transaction with ID {transaction_id}.")
    return redirect('transaction_list')
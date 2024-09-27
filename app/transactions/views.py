from django.shortcuts import render, redirect

from.models import Transaction
from .forms import TransactionForm



def home(request):
    return render(request, 'transactions/home.html')



def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})


def transaction_detail(request, pk):  
    transaction = Transaction.objects.get(pk=pk)  
    return render(request, 'transactions/transaction_detail.html', {'transaction': transaction})  # Passing 'transaction'




def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            return redirect('transaction_detail', pk=transaction.id)
    else:
        form = TransactionForm()
    return render(request, 'transactions/add_transaction.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from.models import Transaction
from .forms import TransactionForm
from django.contrib import messages  


@login_required
def home(request):
    return render(request, 'transactions/home.html')


@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})

@login_required
def transaction_detail(request, transaction_id):
    transaction = get_object_or_404(Transaction, transaction_id=transaction_id, user=request.user)
    return render(request, 'transactions/transaction_detail.html', {'transaction': transaction})


@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            messages.success(request, f"Transaction {transaction.transaction_id} created successfully.")
            return redirect('transaction_detail', transaction_id=transaction.transaction_id)
    else:
        form = TransactionForm()
    return render(request, 'transactions/add_transaction.html', {'form': form})

@login_required
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, transaction_id=transaction_id, user=request.user)
    transaction.delete()
    messages.success(request, f"Successfully deleted transaction with ID {transaction_id}.")
    return redirect('transaction_list')
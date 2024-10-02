from django.core.management.base import BaseCommand
from transactions.models import Transaction

class Command(BaseCommand):
    help = 'Removes duplicate transactions based on transaction_id'

    def handle(self, *args, **options):
        for transaction_id in Transaction.objects.values_list('transaction_id', flat=True).distinct():
            transactions = Transaction.objects.filter(transaction_id=transaction_id)
            if transactions.count() > 1:
                to_keep = transactions.first()
                Transaction.objects.filter(transaction_id=transaction_id).exclude(id=to_keep.id).delete()
                self.stdout.write(f'Cleaned up duplicates for transaction_id: {transaction_id}')
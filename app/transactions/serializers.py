from rest_framework import serializers

from .models import Transaction, RecurringTransaction
from datetime import datetime, timedelta

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        transaction = Transaction.objects.create(**validated_data)
        if transaction.is_recurring:
            """do some magic with recurring transaction"""
            RecurringTransaction.objects.create(transaction=transaction,
                                                next_due_date= datetime.now() + timedelta(minutes=transaction.recurring_frequency))
            return transaction

#toDo update: beacuse the transation frequency may be updated during put or patch conside updating recurring model as well

from celery import shared_task
from django.core.mail import send_mail
import time
from .models import Transaction, RecurringTransaction
from datetime import datetime, timedelta
from django_celery_beat.models import PeriodicTask, IntervalSchedule



@shared_task
def add(x, y):
    return x + y


@shared_task(serializer='json', name="send_mail")
def send_email_fun(subject, message, sender, receiver):
    time.sleep(20) # for check that sending email process runs in background
    send_mail(subject, message, sender, [receiver])

@shared_task
def create_recurring_transactions():
    """setup the recurring transaction"""
    transactions = RecurringTransaction.objects.filter(next_due_date__lte=datetime.now())
    for t in transactions:
        """create a new transaction for each of recurring transactions"""
        Transaction.objects.create(amount=t.transaction.amount,
                                   description=t.transaction.description,
                                   user=t.transaction.user,
                                   date=datetime.now(),
                                   category=t.transaction.category)
        t.next_due_date = datetime.now() + timedelta(minutes=t.transaction.recurring_frequency)
        t.save()


schedule, _ = IntervalSchedule.objects.get_or_create(every=1, period=IntervalSchedule.MINUTES)
PeriodicTask.objects.get_or_create(
    name='Create Recurring Transactions',
    task='transactions.task.create_recurring_transactions',
    interval=schedule,
)
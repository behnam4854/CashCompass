from django.contrib import admin
from .models import Transaction, RecurringTransaction

# Register the User model in the admin panel
admin.site.register(Transaction)
admin.site.register(RecurringTransaction)



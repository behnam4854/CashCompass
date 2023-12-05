from django.db import models
from django.contrib.auth import User

class Account(models.Model):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)  # Options: deposit, withdrawal, transfer
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Financial Transactions:

# Transaction ID (primary key)
# User ID (foreign key)
# Date
# Category
# Amount
# Description
# Payment method

# Budget Details:

# Budget ID (primary key)
# User ID (foreign key)
# Budget name
# Budget category
# Spending limit
# Start date
# End date
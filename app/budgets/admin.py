from django.contrib import admin
from .models import Budget, BudgetCategory

# Register the User model in the admin panel
admin.site.register(Budget)
admin.site.register(BudgetCategory)


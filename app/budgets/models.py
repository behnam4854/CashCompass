from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Budget model to store details of budget templates and user budgets
class Budget(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    income = models.DecimalField(max_digits=17, decimal_places=0)  # Monthly income figure
    savings_goal = models.DecimalField(max_digits=17, null=True, blank=True, decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def total_spent(self):
        return self.categories.aggregate(total_spent=models.Sum('spent'))['total_spent'] or 0

class BudgetCategory(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)

    allocated = models.DecimalField(max_digits=17, decimal_places=0)
    spent = models.DecimalField(max_digits=17, default=0, decimal_places=0)  # Gets updated

    def __str__(self):
        return self.name


# todo. for the remaining of the budget i have spent i can implement the function to calculate sum of all the budget
#  category and simply i know i al over the spending or not

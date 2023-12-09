from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Budget model to store details of budget templates and user budgets
class Budget(models.Model):

    name = models.CharField(max_length=255) 
    is_template = models.BooleanField(default=False)
    
    # Template budgets are base budgets users can select from  
    template = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    # Actual budgets are copied from templates and associated with user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')

    income = models.DecimalField(max_digits=17,decimal_places=0) # Monthly income figure
    savings_goal = models.DecimalField(max_digits=17, null=True, blank=True, decimal_places=0)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Budget Category to allocate $ amounts in each budget  
class BudgetCategory(models.Model):

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)

    allocated = models.DecimalField(max_digits=17, decimal_places=0)
    spent = models.DecimalField(max_digits=17, default=0, decimal_places=0) # Gets updated

    def __str__(self):
        return self.name
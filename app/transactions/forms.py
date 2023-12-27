from django import forms
# from budgets.models import Budget
from .models import Transaction


class TransactionForm(forms.Form):
    """For managing the form data that comes from home url and any page that contain data"""
    amount = forms.CharField(label="نام بودجه", max_length=100)
    description= forms.CharField(label="مبلغ", max_length=100)
    def save_data():
        pass
    
# class BudgetFormModel(forms.ModelForm):
#     class Meta :
#         model = Transaction
#         fields = ["name", "income", "savings_goal"]




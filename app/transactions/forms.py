from django import forms
# from budgets.models import Budget
from .models import Transaction

    
class TransactionForm(forms.ModelForm):
    class Meta :
        model = Transaction
        fields = ["amount", "description", "category","date"]

        widgets = {
            'date': forms.DateInput(attrs={'type':'date'}),
            'amount': forms.DateInput(attrs={'class':'number'}),
        }
        labels = {
            'amount':'مبلغ',
            'description':'توضیحات',
            'category':'نام بودجه',
            # 'budget':'نام سرمایه ',
            'date':' تاریخ',
        }

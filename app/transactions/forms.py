from django import forms
# from budgets.models import Budget
from .models import Transaction


# class TransactionForm(forms.Form):
#     """For managing the form data that comes from home url and any page that contain data"""
#     amount = forms.CharField(label="نام بودجه", max_length=100)
#     description= forms.CharField(label="مبلغ", max_length=100)
    
#     def save_data():
#         pass
    
class TransactionForm(forms.ModelForm):
    class Meta :
        model = Transaction
        fields = ["amount", "description", "category","budget","date"]

        widgets = {
            'date': forms.DateInput(attrs={'type':'date'}),
            'amount': forms.DateInput(attrs={'class':'number'}),
        }
        labels = {
            'amount':'مبلغ',
            'description':'توضیحات',
            'category':'نام بودجه',
            'budget':'نام سرمایه ',
            'date':' تاریخ',
        }

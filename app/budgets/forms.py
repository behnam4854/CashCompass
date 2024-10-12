from django import forms
from budgets.models import Budget


    
class BudgetFormModel(forms.ModelForm):
    class Meta :
        model = Budget
        fields = ["income"]

        widgets = {
            'income': forms.DateInput(attrs={'class':'number'}),
        }
        labels = {
            # 'template':'نام',
            'income':'مبلغ',
        }
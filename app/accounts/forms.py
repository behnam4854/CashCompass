from django import forms
from budgets.models import Budget


class BudegtForm(forms.Form):
    """For managing the form data that comes from home url and any page that contain data"""
    BudgetName = forms.CharField(label="نام بودجه", max_length=100)
    BudgetAmount = forms.CharField(label="مبلغ", max_length=100)
    BudgetGoal = forms.CharField(label='نام هدف',max_length=256)

    def save_data():
        pass
    
class BudgetFormModel(forms.ModelForm):
    class Meta :
        model = Budget
        fields = ["name", "income", "savings_goal"]

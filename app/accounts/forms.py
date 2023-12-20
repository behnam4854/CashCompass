from django import forms


class BudegtForm(forms.Form):
    """For managing the form data that comes from home url and any page that contain data"""
    BudgetName = forms.CharField(label="نام بودجه", max_length=100)
    BudgetAmount = forms.CharField(label="مبلغ", max_length=100)
    BudgetGoal = forms.CharField(label='نام هدف',max_length=256)
    
from django import forms
from budgets.models import Budget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


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




User = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    username = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )


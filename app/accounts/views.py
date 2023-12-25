from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BudegtForm, BudgetFormModel
from django.views.generic.edit import FormView
from budgets.models import Budget

# Create your views here.

# def home(request):
#     form = BudegtForm()
#     if request.method == 'POST':
#         form = BudegtForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect("/thanks/")
#         else:
#             form = BudegtForm()
#     return render(request,'home.html', {"form": form})



class DashboardView(FormView):
    template_name = "home.html"
    form_class = BudegtForm
    success_url = "/dashboard/"

    def form_valid(self, form):
        BudgetName = form.cleaned_data['BudgetName']
        BudgetAmount = form.cleaned_data['BudgetAmount']
        BudgetGoal = form.cleaned_data['BudgetGoal']
        print(BudgetGoal)
        p = Budget(user = self.request.user, name=BudgetName,income=BudgetAmount,savings_goal=BudgetGoal)
        p.save()
        return super().form_valid(form)

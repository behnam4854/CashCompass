from django.shortcuts import render
from transactions.forms import TransactionForm
from .forms import BudgetFormModel
from django.views.generic.edit import FormView
from budgets.models import Budget, BudgetCategory
from transactions.models import Transaction
from django.views.generic import View

class AddMoneyView(View):

    context = {}

    def get(self,request):
        form = BudgetFormModel()
        self.context['form'] = form
        return render(request,'addmoney.html',self.context)
    
    def post(self,request):
        # form = BudgetFormModel(request.POST)
        data = Budget.objects.get(user=request.user)
        form = BudgetFormModel(request.POST or None, instance=data)

        if form.is_valid():
            instance = form.save(commit=False)
            # instance.user = request.user
            income = form.cleaned_data['income']
            instance.income += int(income)
            instance.save()
            
        self.context['form'] = form
        return render(request, 'addmoney.html', self.context)
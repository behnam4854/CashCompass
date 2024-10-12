from django.shortcuts import render
from transactions.forms import TransactionForm
from .forms import BudgetFormModel
from django.views.generic.edit import FormView
from budgets.models import Budget, BudgetCategory
from transactions.models import Transaction
from django.views.generic import View

from rest_framework import viewsets

from .models import Budget
from .serializers import addBugegetSerializer, AddBudgetCatgs
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class BudgetViewSet(viewsets.ModelViewSet):

    queryset = Budget.objects.all()
    serializer_class = addBugegetSerializer

    def get_queryset(self):
        # Filter expenses to only show those belonging to the authenticated user
        return self.queryset.filter(user=self.request.user)

class BudgetsCatgsViewSet(viewsets.ModelViewSet):
    queryset = BudgetCategory.objects.all()
    serializer_class = AddBudgetCatgs
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get_queryset(self):
        # Get the authenticated user
        user = self.request.user

        # Filter BudgetCategories by the user's budgets
        return BudgetCategory.objects.filter(budget__user=user)

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


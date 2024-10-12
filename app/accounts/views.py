from django.shortcuts import render
from .forms import BudegtForm, BudgetFormModel, SignUpForm
from transactions.forms import TransactionForm
from budgets.models import Budget, BudgetCategory
from transactions.models import Transaction
from django.views.generic import View
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserLoginAPIView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# class UserRegisterAPIView(APIView):
#     def post(self, request, *args, **kargs):
#         serializer = UserRegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 'success': True,
#                 'user': serializer.data,
#                 'token': Token.objects.get(user=User.objects.get(username=serializer.data['username'])).key
#             }
#             return Response(response, status=status.HTTP_200_OK)
#         raise ValidationError(
#             serializer.errors, code=status.HTTP_406_NOT_ACCEPTABLE)


# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'user': serializer.data,
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({"success": True, "detail": "Logged out!"}, status=status.HTTP_200_OK)


class DashboardView(View):
    context = {}

    def get(self, request):
        transactions = Transaction.objects.filter(user=request.user)[:10]
        budgetsCats = BudgetCategory.objects.all()
        budgetDetail = Budget.objects.filter(user=request.user).last()
        form = TransactionForm()
        self.context['form'] = form
        self.context['transaction_list'] = transactions
        self.context['budget'] = budgetDetail
        self.context['budgetCats'] = budgetsCats
        return render(request, 'home.html', self.context)

    def post(self, request):
        form = TransactionForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            # this is for adding or subtracing the value everytime i add a value
            addToBudget = BudgetCategory.objects.get(name=instance.category)
            addToBudget.spent += instance.amount
            addToBudget.save()

        self.context['form'] = form
        return render(request, 'home.html', self.context)


class SignupView(View):
    context = {}

    def get(self, request):
        form = SignUpForm()
        self.context['form'] = form
        return render(request, 'signup.html', self.context)

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            # instance = form.save(commit=False)
            # instance.user = request.user
            form.save()
        self.context['form'] = form
        return render(request, 'signup.html', self.context)

# def SignupView(request):
#         if request.method == 'POST':
#             form = SignUpForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 username = None
#                 raw_password = form.cleaned_data.get('password1')
#                 user = authenticate(password=raw_password)
#                 login(request, user)
#                 return redirect('home')
#         else:
#             form = SignUpForm()
#         return render(request, 'signup.html', {'form': form})


# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"

# def DashboardView(request):

#     transactions = Transaction.objects.filter(user=request.user)[:15]

#     if request.method == 'POST': 
#         form = TransactionForm(request.POST)
#         if form.is_valid():
#             amount = form.cleaned_data['amount']
#             description = form.cleaned_data['description']
#             p = Transaction(user = request.user, amount=amount,description=description)
#             p.save()
#     else:
#         form = TransactionForm()

#     context = {
#         'transaction_list': transactions, 
#         'form': form
#     }

#     return render(request, 'home.html', context)


# def home(request):
#     form = BudegtForm()
#     if request.method == 'POST':
#         form = BudegtForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect("/thanks/")
#         else:
#             form = BudegtForm()
#     return render(request,'home.html', {"form": form})


# class DashboardView(FormView):
#     template_name = "home.html"
#     form_class = BudegtForm
#     success_url = "/dashboard/"

#     def form_valid(self, form):
#         BudgetName = form.cleaned_data['BudgetName']
#         BudgetAmount = form.cleaned_data['BudgetAmount']
#         BudgetGoal = form.cleaned_data['BudgetGoal']
#         print(BudgetGoal)
#         p = Budget(user = self.request.user, name=BudgetName,income=BudgetAmount,savings_goal=BudgetGoal)
#         p.save()
#         return super().form_valid(form)

# class DashboardView(FormView):
#     template_name = "home.html"
#     form_class = TransactionForm
#     success_url = "/dashboard/"

#     def form_valid(self, form):
#         amount = form.cleaned_data['amount']
#         description = form.cleaned_data['description']
#         p = Transaction(user = self.request.user, amount=amount,description=description)
#         p.save()
#         return super().form_valid(form)

# class DashboardView(ListView):
#     model = Transaction
#     context_object_name = "transactions"
#     queryset = Transaction.objects.all()
#     template_name = "templates/home.html"

#     def post(self, request, *args, **kwargs):
#         # When the form is submitted, it will enter here
#         self.object = None
#         self.form = TransactionForm
#         if self.form.is_valid():
#             self.object = self.form.save()
#             # Here ou may consider creating a new instance of form_class(),
#             # so that the form will come clean.

#         # Whether the form validates or not, the view will be rendered by get()
#         return self.get(request, *args, **kwargs)


#     def get_context_data(self, **kwargs):
#         context = super(DashboardView, self).get_context_data(**kwargs)
#         context['form'] = TransactionForm()
#         return context


# class FormListView(FormMixin, ListView):
#     def get(self, request, *args, **kwargs):
#         # From ProcessFormMixin
#         form_class = self.get_form_class()
#         self.form = self.get_form(form_class)

#         # From BaseListView
#         self.object_list = self.get_queryset()
#         allow_empty = self.get_allow_empty()
#         if not allow_empty and len(self.object_list) == 0:
#             raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
#                           % {'class_name': self.__class__.__name__})

#         context = self.get_context_data(object_list=self.object_list, form=self.form)
#         return self.render_to_response(context)

#     def post(self, request, *args, **kwargs):
#         return self.get(request, *args, **kwargs)
# class DashboardView(ListView, ModelFormMixin):
#     model = Transaction
#     context_object_name = "transactions"
#     queryset = Transaction.objects.all()
#     template_name = "templates/home.html"
#     form_class = TransactionForm

#     # def get(self, request, *args, **kwargs):
#     #     self.object = None
#     #     self.form = self.get_form(self.form_class)
#     #     # Explicitly states what get to call:
#     #     return ListView.get(self, request, *args, **kwargs)

#     # def post(self, request, *args, **kwargs):
#     #     # When the form is submitted, it will enter here
#     #     self.object = None
#     #     self.form = self.get_form(self.form_class)

#     #     if self.form.is_valid():
#     #         self.object = self.form.save()
#     #         # Here ou may consider creating a new instance of form_class(),
#     #         # so that the form will come clean.

#     #     # Whether the form validates or not, the view will be rendered by get()
#     #     return self.get(request, *args, **kwargs)


#     def get_context_data(self, **kwargs):
#         context = super(DashboardView, self).get_context_data(**kwargs)
#         context['form'] = TransactionForm()
#         return context

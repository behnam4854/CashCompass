from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from transactions.views import TransactionViewSet
from budgets.views import BudgetViewSet, BudgetsCatgsViewSet
from rest_framework.authtoken import views
from accounts.views import UserLoginAPIView,RegisterView,CustomTokenObtainPairView



router = routers.DefaultRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'budgets', BudgetViewSet)
router.register(r'budgetCatgs', BudgetsCatgsViewSet)
# router.register(r'transactions', TransactionViewSet, basename='transaction')

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("accounts/", include("django.contrib.auth.urls")),
    path('budgets/', include('budgets.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path("login/", UserLoginAPIView.as_view(), name="user_login"),
    path('register/', RegisterView.as_view(), name="sign_up"),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/',include('accounts.urls')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("plot/", include("transactions.urls")),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.contrib import admin
from .models import User

# Register the User model in the admin panel
admin.site.register(User)

# Register the UserProfile model in the admin panel
# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'address', 'city', 'occupation')
#     search_fields = ('user__name', 'address', 'city',  'occupation')
#     fieldsets = (
#         (None, {
#             'fields': ('user', 'address', 'city')
#         }),
#         ('Occupation and Financial Information', {
#             'fields': ('occupation', 'income', 'monthly_expenses')
#         }),
#     )

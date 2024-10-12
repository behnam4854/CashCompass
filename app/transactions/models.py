from django.db import models
from django.contrib.auth import get_user_model
from budgets.models import Budget, BudgetCategory

User = get_user_model()


class Transaction(models.Model):
    """
    User transactions affecting their budget tracking
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #  budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(BudgetCategory, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        # Call the original save method to save the transaction first
        super().save(*args, **kwargs)

        # Update the spent amount in the related BudgetCategory
        if self.category:
            self.category.spent += self.amount  # Increment spent amount
            self.category.save()

    def delete(self, *args, **kwargs):
        # Decrement the spent amount in the related BudgetCategory
        if self.category:
            self.category.spent -= self.amount  # Decrease spent amount
            self.category.save()  # Save the updated category
        super().delete(*args, **kwargs)

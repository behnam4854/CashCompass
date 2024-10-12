from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from .models import Budget, BudgetCategory


class addBugegetSerializer(serializers.ModelSerializer):
    """Serializer for adding budget"""

    class Meta:
        model = Budget
        fields = "__all__"
        read_only_fields = ["user"]

    def create(self, validated_data):
        budget = Budget(
            user=self.context['request'].user,
            name=validated_data['name'],
            income=validated_data['income'],
            savings_goal=validated_data['savings_goal']
        )
        budget.save()
        return budget


class AddBudgetCatgs(serializers.ModelSerializer):
    """for adding budget categories to use in spendings"""
    budget_name = serializers.CharField(source='budget.name', read_only=True)
    remaining_budget = serializers.SerializerMethodField()

    class Meta:
        model = BudgetCategory
        fields = ['id', 'name', 'allocated', 'spent', 'budget_name', 'remaining_budget']

    def get_remaining_budget(self, obj):
        return int(obj.allocated - obj.spent)


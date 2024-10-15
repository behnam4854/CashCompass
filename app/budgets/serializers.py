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

    def update(self, instance, validated_data):
        """for uodating the amount of money added to the current budget"""
        new_income = validated_data.get('income', None)
        if new_income is not None:
            instance.income += new_income
            instance.name = validated_data.get("name")
            instance.savings_goal = validated_data.get("savings_goal")
        instance.save()
        return instance


class AddBudgetCatgs(serializers.ModelSerializer):
    """for adding budget categories to use in spendings"""
    budget_name = serializers.CharField(source='budget.name', read_only=True)
    remaining_budget = serializers.SerializerMethodField()

    class Meta:
        model = BudgetCategory
        fields = ['id', 'name', 'budget', 'allocated', 'spent', 'budget_name', 'remaining_budget']
        read_only_fields = ["spent"]



    def get_remaining_budget(self, obj):
        return int(obj.allocated - obj.spent)


#todo i need recuring transactions that every mounth i get a paycheck and the rent and also the isurence of the car
# so how can i implement that?

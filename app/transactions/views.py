from django.db.models import Count
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Transaction
from .serializers import TransactionSerializer
# from .visulize_helper import analyze_data, plot_data
import matplotlib.pyplot as plt
import io
import base64
import urllib.parse

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [AllowAny]
    def perform_create(self, serializer):
        # Automatically set the user to the currently authenticated user
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Filter expenses to only show those belonging to the authenticated user
        return self.queryset.filter(user=self.request.user)

def plot_view(request):
    """plot the data that we get from analyzing our data"""
    data = Transaction.objects.values('created_at').annotate(count=Count('id')).order_by('created_at')
    # Generate the plot
    days = [d['created_at'] for d in data]
    counts = [d['count'] for d in data]
    plt.figure(figsize=(10, 4))
    plt.plot(days, counts, '--bo')
    plt.xlabel('Days')
    plt.ylabel('Count')
    plt.title('Records per Day')

    # Convert graph to bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Convert bytes buffer to base64 string
    string = base64.b64encode(buf.read()).decode()
    uri = urllib.parse.quote(string)

    # Close the figure to free up resources
    plt.close()

    return render(request, 'report.html', {'data': uri})


def full_screen_plot(request):
    # Generate the plot
    plt.figure(figsize=(10, 5))
    plt.plot([1, 2], [1, 2])
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Full Screen Plot')



    # Get the current figure manager
    figManager = plt.get_current_fig_manager()

    # For Qt backends
    if figManager.window.qtbinder is not None:
        figManager.window.showMaximized()
    else:
        # For other backends like TkAgg
        figManager.full_screen_toggle()

    plt.show()

    return render(request, 'report.html')

    # return render(request, 'report.html', {'data': uri})






# this is helper function to visulize the data using pandas and matplotlib

import pandas as pd
from .models import Transaction

from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import base64
import urllib.parse

from django.http import HttpResponse

def analyze_data():
    """to give us a simple summery about our data"""
    data = Transaction.objects.all().values('amount', 'date')
    df = pd.DataFrame(list(data))
    summery = df.describe()
    return summery




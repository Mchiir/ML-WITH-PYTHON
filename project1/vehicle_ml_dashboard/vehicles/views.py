from django.shortcuts import render

import os

# Create your views here.
import pandas as pd
from django.shortcuts import render
from .dashboard import frequency_table, display_my_dataset, aggregated_df, crossed_table, pivot_table
from django.conf import settings

def dashboard_view(request):
    file_path = os.path.join(       # Used relative file_paths to prevent file referential errors
        settings.BASE_DIR,
        "dummy_data",
        "vehicles_data_1000.csv"
    )

    # queryset = pd.read_csv("dummy_data/vehicles_data_1000.csv")
    df = pd.read_csv(file_path)
    
    return render(request, "vehicles/index.html", {
        "frequency_table": frequency_table(df),
        "my_dataset": display_my_dataset(df),
        "aggregated_data": aggregated_df(df),
        "crossed_table": crossed_table(df),
        "pivot_table": pivot_table(df),
    })
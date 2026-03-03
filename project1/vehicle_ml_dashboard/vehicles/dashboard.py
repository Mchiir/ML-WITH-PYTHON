import plotly.express as px
import plotly.offline as opy
import plotly.graph_objects as go
import pandas as pd

def frequency_table(df):
    manufacturer_counts = df['manufacturer'].value_counts().reset_index()
    manufacturer_counts.columns = ['Manufacturer', 'Count']
    
    table_html = manufacturer_counts.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='%.2f',
        justify='center'
    )
    return table_html

def display_my_dataset(df):
    return df.head(10).to_html(
        index=False, 
        classes="table table-bordered table-striped table-sm", 
        justify='center'
    )

def aggregated_df(df):
    df["profit"] = df["selling_price"] - df["wholesale_price"]
    
    grouped = df.groupby(['manufacturer', 'transmission', 'fuel_type']).agg({
        'selling_price': 'sum',
        'wholesale_price': 'sum',
        'profit': 'sum'
    })
    
    return grouped.to_html(
        classes="table table-bordered table-striped table-sm", 
        justify='center'
    )


def crossed_table(df):

    
    crossed = pd.crosstab(df['manufacturer'], df['body_type'], values = df['selling_price'], aggfunc=["sum"], margins=True)

    return crossed.to_html(
        classes="table table-bordered table-striped table-sm",
        justify='center'
    )

def pivot_table(df):
    pivot = pd.pivot_table(df, values='selling_price', index='manufacturer', columns='fuel_type', aggfunc=['sum','mean'])
    return pivot.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='%.2f',
        justify='center'
    )
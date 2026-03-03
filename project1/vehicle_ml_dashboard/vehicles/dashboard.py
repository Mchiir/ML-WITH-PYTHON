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


def visualize_sales_with_sunburst_chart(df, height=800):
    fig = px.sunburst(df, path=['manufacturer', 'fuel_type', 'body_type'], values='selling_price')
    fig.update_traces(textinfo='label+value')
    fig.update_layout(height=height)
    return opy.plot(fig, auto_open=False, output_type='div')

def visualize_sales_with_treemap(df, height=800):
    df_grouped = df.groupby(
        ['manufacturer', 'fuel_type', 'body_type'],
        as_index=False
    )['selling_price'].sum()

    fig = px.treemap(
        df_grouped,
        path=['manufacturer', 'fuel_type', 'body_type'],
        values='selling_price',
        title="Sales Distribution Treemap"
    )

    fig.update_layout(
        height=height,
        margin=dict(t=40, l=0, r=0, b=0)
    )

    return opy.plot(fig, auto_open=False, output_type='div')

def visualize_manufacturer_bar_chart(df, height=600):
    manufacturer_counts = df['manufacturer'].value_counts().reset_index()
    manufacturer_counts.columns = ['Manufacturer', 'Count']

    fig = px.bar(
        manufacturer_counts,
        x='Manufacturer',
        y='Count',
        title="Vehicle Count per Manufacturer",
        text='Count'
    )

    fig.update_layout(
        height=height,
        xaxis_title="Manufacturer",
        yaxis_title="Number of Vehicles",
        margin=dict(t=40, l=0, r=0, b=0)
    )

    fig.update_traces(textposition='outside')

    return opy.plot(fig, auto_open=False, output_type='div')

def visualize_sales_with_icicle(df, height=800):
    df_grouped = df.groupby(
        ['manufacturer', 'fuel_type', 'body_type'],
        as_index=False
    )['selling_price'].sum()

    fig = px.icicle(
        df_grouped,
        path=['manufacturer', 'fuel_type', 'body_type'],
        values='selling_price',
        title="Sales Distribution Icicle Chart"
    )

    fig.update_layout(
        height=height,
        margin=dict(t=40, l=0, r=0, b=0)
    )

    return opy.plot(fig, auto_open=False, output_type='div')

def sales_by_country(df, height=600):
    country_sales = df.groupby('client_country')['selling_price'].sum().reset_index()
    country_sales.columns = ['Country', 'Total Sales']
    fig = px.choropleth(
        country_sales,
        locations='Country',
        locationmode='country names',
        color='Total Sales',
        color_continuous_scale='Viridis',
        title='Total Sales by Country',
    )
    fig.add_scattergeo(
        locations=country_sales['Country'],
        locationmode='country names',
        text=country_sales['Country'],
        mode='text',
        textfont=dict(size=9, color='white'),
        showlegend=False,
    )
    fig.update_layout(height=height, geo=dict(showframe=False, projection_type='natural earth'))
    return opy.plot(fig, auto_open=False, output_type='div')
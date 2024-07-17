"""
FRED Data Visualization App

This module provides a Streamlit-based web application for visualizing
Federal Reserve Economic Data (FRED).
It allows users to select and compare different economic indicators,
apply various aggregations,
and generate insights from the data.
"""
import os
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from dotenv import load_dotenv
from fredapi import Fred

from .fred_categories import category_component, fetch_fred_categories

# Load environment variables
load_dotenv()

# Initialize FRED API
fred = Fred(api_key=os.getenv('FRED_API_KEY'))

# Streamlit configuration
st.set_page_config(layout="wide")
st.title('FRED Data Visualization App')

# --- Data Selection Sidebar ---
st.sidebar.header('Data Selection')

# 1. Category Selection (using memoization for efficiency)
@st.cache_data
def get_fred_categories():
    return fetch_fred_categories()


categories = get_fred_categories()
category_names = [cat['name'] for cat in categories]
selected_category_name = st.sidebar.selectbox("Select Category", options=category_names)
selected_category_id = next(
    cat['id'] for cat in categories if cat['name'] == selected_category_name
)

# 2. Series Selection (using memoization for efficiency)
@st.cache_data
def get_series_list(category_id):
    return fred.get_series_in_category(category_id)


series_list = get_series_list(selected_category_id)
series_id = st.sidebar.selectbox('Select FRED Series:', options=series_list)

# 3. Comparison Series (Conditional)
enable_comparison = st.sidebar.checkbox('Compare with another dataset')
series_id2 = None
if enable_comparison:
    series_id2 = st.sidebar.selectbox(
        'Select second FRED Series:',
        options=series_list,
        key='series2'  # Important for widget state
    )

# 4. Date Range Selection
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')

# Aggregation option
aggregation = st.sidebar.selectbox(
    'Aggregation',
    options=['None', 'Weekly', 'Monthly', 'Quarterly', 'Yearly']
)

# Visualization options
viz_type = st.sidebar.selectbox(
    'Visualization Type',
    options=['Line', 'Bar', 'Scatter', '3D Scatter', 'Area']
)

@st.cache_data
def get_fred_data(series_id, start_date, end_date):
    """
    Fetch data from FRED API for a given series and date range.

    Args:
        series_id (str): The FRED series identifier
        start_date (str): Start date for the data range
        end_date (str): End date for the data range

    Returns:
        pd.DataFrame: DataFrame containing the fetched data
    """
    try:
        data = fred.get_series(series_id, start_date, end_date)
        df = pd.DataFrame(data).reset_index()
        df.columns = ['Date', 'Value']
        return df
    except fredapi.fred.HTTPError as e:
        st.error(f"Error fetching data from FRED: {str(e)}")
        return pd.DataFrame(columns=['Date', 'Value'])
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")
        return pd.DataFrame(columns=['Date', 'Value'])


def aggregate_data(df, agg_type):
    """
    Aggregate data based on the specified aggregation type.

    Args:
        df (pd.DataFrame): Input DataFrame
        agg_type (str): Aggregation type (
            'None', 'Weekly', 'Monthly', 'Quarterly', 'Yearly'
        )

    Returns:
        pd.DataFrame: Aggregated DataFrame
    """
    df['Date'] = pd.to_datetime(df['Date'])

    resampling_options = {
        'Weekly': 'W',
        'Monthly': 'M',
        'Quarterly': 'Q',
        'Yearly': 'Y'
    }

    if agg_type in resampling_options:
        return df.resample(
            """ How to use this app:
            1. Select a category and series from the sidebar
            2. Choose to compare with another dataset (optional)
            3. Select start and end dates
            4. Choose aggregation and visualization type
            5. Click 'Fetch Data' to visualize
            6. Explore insights below the visualization
            7. Use the FRED Categories section for more information"""
        )

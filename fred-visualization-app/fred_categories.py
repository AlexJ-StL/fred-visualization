import requests
from dash import html, dcc
import dash_bootstrap_components as dbc

FRED_API_KEY = 'your_fred_api_key_here' 
# Replace with your actual FRED API key

def fetch_fred_categories():
    url = f"https://api.stlouisfed.org/fred/category/children?category_id=0&api_key={FRED_API_KEY}&file_type=json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['categories']
    else:
        return []


def create_category_list():
    categories = fetch_fred_categories()
    return html.Div([
        html.H3("FRED Categories"),
        dbc.ListGroup([
            dbc.ListGroupItem([
                html.Div(f"{category['name']} (ID: {category['id']})"),
                html.A(
                    "View on FRED",
                    href=f"https://fred.stlouisfed.org/categories/{category['id']}",
                    target="_blank"
                )
            ]) for category in categories
        ]),
        html.Div([
            html.A("View all categories on FRED", href="https://fred.stlouisfed.org/categories", target="_blank"),
            html.Br(),
            html.A("Search for FRED series", href="https://fred.stlouisfed.org/tags/series", target="_blank")
        ], className="mt-3")
    ])


def category_component():
    return html.Div([
        html.H2("FRED Categories and Series"),
        dbc.Input(
            id="category-search",
            type="text",
            placeholder="Search categories..."
        ),
        html.Div(id="category-list", children=[create_category_list()])
    ])

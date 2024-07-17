# FRED Data Visualization App

This Streamlit app creates visualizations using data from the Federal Reserve Bank of St. Louis (FRED, ALFRED, and Maps APIs).

## Setup

1. Perquisites

a. Ensure you have a FRED API which can be obtained by creating an account at https://fredaccount.stlouisfed.org/login/secure/ and requesting an API from the menu on the left hand side of the page.

b. Python 3.7+ installed on your system.

2. Install Poetry if you haven't already:
   ```
   pip install poetry
   ```

3. Clone this repository:
   ```
   git clone <repository-url>
   cd fred-visualization-app
   ```

4. Install the project dependencies using Poetry:
   ```
   poetry install
   ```

5. Activate the virtual environment created by Poetry:
   ```
   poetry shell
   ```

6. Create an `.env` file in the project root and add your FRED API key:
   ```
   FRED_API_KEY=your_api_key_here
   ```

## Running the App

To run the Streamlit app, use the following command within the Poetry shell:

```
streamlit run app.py
```

The app should open in your default web browser. If it doesn't, you can access it at `http://localhost:8501`.

## Using the App

1. Enter a FRED Series ID in the sidebar (e.g., 'GDP' for Gross Domestic Product).
2. Select start and end dates for the data you want to visualize.
3. Click 'Fetch Data' to retrieve and visualize the data.
4. Use the ALFRED section to view historical releases of a specific series.
5. Use the Maps section to view geographical data (note: this is a simplified representation and doesn't include actual map visualizations).

## Available Data Sources

- FRED (Federal Reserve Economic Data)
- ALFRED (Archival Federal Reserve Economic Data)
- FRED Maps (Geographical Economic Data)

## Troubleshooting

If you encounter any issues:

1. Ensure you have the latest version of Poetry installed:
   ```
   pip install --upgrade poetry
   ```

2. Try removing the existing virtual environment and reinstalling dependencies:
   ```
   poetry env remove python
   poetry install
   ```

3. If you're still having issues with specific packages, you can try updating them individually:
   ```
   poetry update package_name
   ```

4. Verify that your API key is correct in the `.env` file.

5. Check your internet connection, as the app requires access to the FRED API.

6. If you're experiencing issues related to Streamlit or its dependencies, you can try using a specific Python version that's known to work well with the current Streamlit version:
   ```
   poetry env use python3.9
   poetry install
   ```

For more information on available FRED series IDs and API usage, visit: https://fred.stlouisfed.org/docs/api/fred/

## License

This project is open source and available under the [MIT License](LICENSE).
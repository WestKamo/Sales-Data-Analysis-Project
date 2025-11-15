import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Set backend BEFORE importing pyplot
import matplotlib.pyplot as plt
import seaborn as sns

class SalesAnalyzer:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)

        # Rename columns to standard names
        self.df.rename(columns={
            "saledate": "Date",
            "model": "Product",
            "sellingprice": "Revenue"
        }, inplace=True)

        # Convert Date column safely
        self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')

        # Drop rows where Date could not be parsed
        self.df = self.df.dropna(subset=['Date'])

    def calculate_total_revenue(self):
        return self.df['Revenue'].sum()

    def get_best_selling_products(self, top_n=5):
        return self.df['Product'].value_counts().head(top_n)

    def analyze_monthly_trends(self):
        # Ensure Date is datetime before using .dt
        if not pd.api.types.is_datetime64_any_dtype(self.df['Date']):
            self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')
            self.df = self.df.dropna(subset=['Date'])

        monthly_sales = (
            self.df.groupby(self.df['Date'].dt.to_period('M'))['Revenue'].sum()
        )
        return monthly_sales

    def get_sales_summary(self):
        return {
            'Total Revenue': self.calculate_total_revenue(),
            'Total Orders': len(self.df),
            'Average Order Value': self.df['Revenue'].mean(),
            'Best Selling Product': self.get_best_selling_products(1).index[0]
        }

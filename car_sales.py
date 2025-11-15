from sales_analysis import SalesAnalyzer

# Path to your dataset
data_path = "data/car_prices.csv"   # adjust if your file is elsewhere

# Create analyzer object
analyzer = SalesAnalyzer(data_path)

# Print summary
print("Car Sales Summary:")
print(analyzer.get_sales_summary())

# Show top 5 best-selling models
print("\nTop 5 Best-Selling Models:")
print(analyzer.get_best_selling_products())

# Plot monthly trends
analyzer.plot_monthly_trends()

# Plot product distribution
analyzer.plot_product_distribution()





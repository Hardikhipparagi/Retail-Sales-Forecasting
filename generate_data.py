import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
num_days = 365   # 1 year data
num_products = 5
num_stores = 3

# Date range
dates = pd.date_range(start="2023-01-01", periods=num_days)

data = []

for store in range(1, num_stores + 1):
    for product in range(1, num_products + 1):

        base_demand = np.random.randint(20, 50)

        for date in dates:
            
            # Seasonality (weekend boost)
            if date.weekday() >= 5:
                seasonal = 10
            else:
                seasonal = 0

            # Random noise
            noise = np.random.randint(-5, 6)

            # Promo effect
            on_promo = np.random.choice([0, 1], p=[0.8, 0.2])
            promo_boost = 15 if on_promo else 0

            qty = max(0, base_demand + seasonal + noise + promo_boost)

            price = np.random.randint(100, 500)

            data.append([
                date,
                f"Store_{store}",
                f"Product_{product}",
                qty,
                price,
                on_promo
            ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "date", "store_id", "product_id",
    "qty_sold", "price", "on_promo"
])

# Save CSV
df.to_csv("data/retail_data.csv", index=False)

print("✅ Dataset generated successfully!")
print(df.head())
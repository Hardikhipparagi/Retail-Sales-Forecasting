from src.data_loader import load_data
from src.features import create_features
from src.model import train_model, predict
from src.inventory import inventory_policy
import pandas as pd

df = load_data("data/retail_data.csv")

df = create_features(df)

model = train_model(df)

predictions = predict(model, df)

result = inventory_policy(predictions)

df["predicted_sales"] = predictions
df.to_csv("outputs/forecast.csv", index=False)

print("Inventory Decision:", result)
print(df.columns)
print(df.head())

output = pd.DataFrame([result])
output.to_csv("outputs/inventory_results.csv", index=False)
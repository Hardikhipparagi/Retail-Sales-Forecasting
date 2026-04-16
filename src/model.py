import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

def train_model(df):

    # =========================
    # FEATURES & TARGET
    # =========================
    features = [
        "lag_1", "lag_7",
        "rolling_mean_7", "rolling_std_7",
        "day_of_week", "month", "price", "on_promo"
    ]

    X = df[features]
    y = df["qty_sold"]

    # =========================
    # TRAIN TEST SPLIT (TIME BASED)
    # =========================
    split = int(len(df) * 0.8)

    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    # =========================
    # MODEL
    # =========================
    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=10,
        random_state=42
    )

    model.fit(X_train, y_train)

    # =========================
    # EVALUATION
    # =========================
    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    print(f"MAE: {mae:.2f}")

    # Save model
    joblib.dump(model, "models/model.pkl")

    return model
def predict(model, df):

    features = [
        "lag_1", "lag_7",
        "rolling_mean_7", "rolling_std_7",
        "day_of_week", "month", "price", "on_promo"
    ]

    X = df[features]

    predictions = model.predict(X)

    return predictions
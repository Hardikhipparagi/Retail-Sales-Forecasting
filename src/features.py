import pandas as pd

def create_features(df):
    
    # Sort data properly
    df = df.sort_values(["store_id", "product_id", "date"])
    
    # =========================
    # LAG FEATURES
    # =========================
    df["lag_1"] = df.groupby(["store_id", "product_id"])["qty_sold"].shift(1)
    df["lag_7"] = df.groupby(["store_id", "product_id"])["qty_sold"].shift(7)
    
    # =========================
    # ROLLING FEATURES
    # =========================
    df["rolling_mean_7"] = df.groupby(["store_id", "product_id"])["qty_sold"].shift(1).rolling(7).mean()
    df["rolling_std_7"] = df.groupby(["store_id", "product_id"])["qty_sold"].shift(1).rolling(7).std()
    
    # =========================
    # DATE FEATURES
    # =========================
    df["day_of_week"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month
    
    # =========================
    # PROMOTION FEATURE
    # =========================
    df["promo_effect"] = df["on_promo"] * df["qty_sold"]
    
    # Drop NA values (important)
    df = df.dropna()
    
    return df
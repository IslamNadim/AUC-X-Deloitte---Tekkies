import pandas as pd
from sklearn.cluster import KMeans


def menu_engineering_clusters(df: pd.DataFrame) -> pd.DataFrame:
    """
    Classifies menu items into Stars, Plowhorses, Puzzles, Dogs
    using K-Means on popularity and profit.
    """

    if df.empty:
        return df

    features = df[["Sales_Volume", "Profit"]]

    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    df["cluster"] = kmeans.fit_predict(features)

    # Map clusters to business labels
    cluster_summary = (
        df.groupby("cluster")[["Sales_Volume", "Profit"]]
        .mean()
        .sort_values(by=["Sales_Volume", "Profit"])
    )

    labels = ["Dog", "Puzzle", "Plowhorse", "Star"]

    mapping = {
        cluster: label
        for cluster, label in zip(cluster_summary.index, labels)
    }

    df["menu_category"] = df["cluster"].map(mapping)

    return df

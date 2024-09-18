
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

def train_model():
    X, _ = make_blobs(n_samples=300, centers=4, cluster_std=1.0, random_state=42)
    kmeans = KMeans(n_clusters=4, random_state=42)
    kmeans.fit(X)
    
    # Save model
    pd.to_pickle(kmeans, "kmeans_model.pkl")

if __name__ == "__main__":
    train_model()

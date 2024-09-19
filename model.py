
import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Function to train and save KMeans model
def train_model():
    # Generate synthetic data
    X, _ = make_blobs(n_samples=300, centers=4, cluster_std=1.0, random_state=42)
    
    # Train the KMeans model
    kmeans = KMeans(n_clusters=4, random_state=42)
    kmeans.fit(X)
    
    # Define model path
    model_path = "kmeans_model.pkl"
    
    # Check if model file already exists
    if os.path.exists(model_path):
        print(f"Warning: '{model_path}' already exists and will be overwritten.")
    
    # Save model to file
    pd.to_pickle(kmeans, model_path)
    print(f"Model saved to '{model_path}'.")

if __name__ == "__main__":
    train_model()

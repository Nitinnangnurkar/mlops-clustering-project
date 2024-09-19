import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Load and run inference
def run_inference():
    # Generate synthetic data
    X, _ = make_blobs(n_samples=300, centers=4, cluster_std=1.0, random_state=42)
    
    # Load the pre-trained model
    try:
        model = pd.read_pickle("kmeans_model.pkl")
    except FileNotFoundError:
        st.error("Model file 'kmeans_model.pkl' not found!")
        return
    
    # Perform prediction
    labels = model.predict(X)
    
    # Plot the results
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
    st.pyplot(plt)
    plt.close()  # Close the plot after rendering

# UI for Streamlit
st.title("KMeans Clustering Inference")
if st.button("Run Clustering"):
    run_inference()

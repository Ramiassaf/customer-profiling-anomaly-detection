from sklearn.cluster import KMeans


def run_kmeans(X, n_clusters=5, random_state=42):
    """
    Perform customer segmentation using K-Means clustering.

    Parameters
    ----------
    X : Scaled feature matrix
    n_clusters : Number of clusters
    random_state : Random seed for reproducibility

    Returns
    -------
    labels : Cluster labels for each customer

    """

    model = KMeans(
        n_clusters=n_clusters,
        random_state=random_state,
        n_init=10
    )

    labels = model.fit_predict(X)

    return labels, model
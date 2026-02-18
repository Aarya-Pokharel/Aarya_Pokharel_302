from sklearn.cluster import KMeans

# Data points
X = [[1,2],[1,4],[1,0],[10,2],[10,4],[10,0]]

# Create kMeans object with 2 clusters
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)

print("Cluster centers:", kmeans.cluster_centers_)
print("Labels:", kmeans.labels_)
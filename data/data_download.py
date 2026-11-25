import kagglehub

# Download latest version
path = kagglehub.dataset_download("energy-utilities-application-data")

print("Path to dataset files:", path)
import kagglehub as kg

# Download latest version
path = kg.dataset_download("dansbecker/melbourne-housing-snapshot")

print("Path to dataset files:", path)
# Import required libraries (pandas is pre-installed in Colab)
import pandas as pd
import numpy as np

def analyze_csv(file_path):
    """
    Read a CSV file and calculate mean, min, and max for all numeric columns.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        dict: Dictionary containing statistics for each numeric column
    """
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    
    # Select only numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    # Calculate statistics for each numeric column
    stats = {}
    for col in numeric_cols:
        stats[col] = {
            'mean': df[col].mean(),
            'min': df[col].min(),
            'max': df[col].max()
        }
    
    return stats

# Create sample data (in Colab, you'll upload your own CSV)
sample_data = pd.DataFrame({
    'temperature': [22.5, 23.1, 21.8, 22.7, 22.4],
    'humidity': [45.0, 44.5, 46.2, 45.8, 45.3],
    'text_column': ['a', 'b', 'c', 'd', 'e']  # Non-numeric column
})

# Save sample data to CSV
sample_file = 'sample_data.csv'
sample_data.to_csv(sample_file, index=False)

# Analyze the data
stats = analyze_csv(sample_file)

# Print results
print("Statistics for each numeric column:")
for column, values in stats.items():
    print(f"\n{column}:")
    for stat, value in values.items():
        print(f"  {stat}: {value:.2f}")

"""
To use this in Google Colab:

1. Create a new notebook
2. Copy this code into a cell
3. To use with your own CSV:
   - Click on the folder icon in the left sidebar
   - Upload your CSV file
   - Replace 'sample_data.csv' with your file name
   
Example Colab usage:
```python
from google.colab import files
uploaded = files.upload()  # Opens file upload dialog

# Get the filename of the uploaded file
file_name = next(iter(uploaded))

# Analyze the uploaded file
stats = analyze_csv(file_name)

# Print results
print("Statistics for each numeric column:")
for column, values in stats.items():
    print(f"\n{column}:")
    for stat, value in values.items():
        print(f"  {stat}: {value:.2f}")
```
"""

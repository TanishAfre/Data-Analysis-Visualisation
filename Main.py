import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np
import seaborn as sns
import warnings
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Load the data into a pandas DataFrame
data = pd.read_csv("C:\\Users\\tanis\\Data-Analysis-Visualisation\\WHR2023.csv")

df = pd.read_csv("C:\\Users\\tanis\\Data-Analysis-Visualisation\\WHR2023.csv")

# Display the first 5 rows of the data
print(df.head(5))


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data
df = pd.read_csv('Mall_Customers.csv')

# Sidebar filters
age_range = st.sidebar.slider('Select Age Range', int(df['Age'].min()), int(df['Age'].max()), (18, 60))
income_range = st.sidebar.slider('Select Income Range', int(df['Annual Income (k$)'].min()), int(df['Annual Income (k$)'].max()), (15, 120))

# Filter data
filtered_data = df[(df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1]) & 
                   (df['Annual Income (k$)'] >= income_range[0]) & 
                   (df['Annual Income (k$)'] <= income_range[1])]

# Display spending score by age and income
st.title("Customer Segmentation Dashboard")
st.write("Spending Score vs Age and Income")

fig, ax = plt.subplots()
sns.scatterplot(data=filtered_data, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Gender', palette='coolwarm', s=100, ax=ax)
st.pyplot(fig)

def recommend_services(cluster):
    if cluster == 'High-Income High-Spenders':
        return "Premium Memberships, Luxury Product Discounts"
    elif cluster == 'Young Low-Spenders':
        return "Discount Coupons, Budget-Friendly Products"
    # Define recommendations for other clusters

# Test recommendations
cluster = 'High-Income High-Spenders'
print(f"Recommended for {cluster}: {recommend_services(cluster)}")
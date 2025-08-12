import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Page Configuration ---
st.set_page_config(page_title="Terrorism Analysis Dashboard", layout="wide")

# --- Load Data ---
# This function caches the data so it doesn't have to reload every time
@st.cache_data
def load_data():
    # Make sure your cleaned CSV file is in the same folder
    df = pd.read_csv('global_terrorism_cleaned.csv')
    return df

df = load_data()

# --- Dashboard Title ---
st.title('Global Terrorism Analysis Dashboard 🌍')

# --- Interactive Sidebar ---
st.sidebar.header('Filter Options')
country_list = ['All'] + sorted(df['Country'].unique().tolist())
selected_country = st.sidebar.selectbox('Select a Country', country_list)

# --- Filter Data Based on Selection ---
if selected_country == 'All':
    filtered_df = df
    st.header('Showing Global Data')
else:
    filtered_df = df[df['Country'] == selected_country]
    st.header(f'Showing Data for {selected_country}')

# --- Display Visualizations ---
st.subheader('Top 10 Most Attacked States/Provinces')

if not filtered_df.empty:
    state_counts = filtered_df['State'].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=state_counts.index, y=state_counts.values, ax=ax, palette='plasma')
    ax.set_title('Top 10 Affected States/Provinces')
    ax.set_xlabel('State / Province')
    ax.set_ylabel('Number of Attacks')
    plt.xticks(rotation=45)

    st.pyplot(fig)
else:
    st.write("No data available for the selected country.")
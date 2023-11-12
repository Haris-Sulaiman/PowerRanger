import pandas as pd
import streamlit as st
import plotly.express as px

st.title('Power Ranger')
st.subheader("Use this web app to view different user's power usage data")

def read_file(name):
    with open(name, 'r') as f:
        data = f.read().splitlines()
    return data

# Selectbox for choosing the user
users = ["36", "26"]
current_user = st.selectbox("Select a user to view their power consumption", users)

# Assuming your file has a single column of power values
power = read_file(current_user +'p.txt')

# Create a DataFrame with 'time' as the index and 'power' as the column
df = pd.DataFrame({'time': range(len(power)), 'power': power})

# Display the data in a dataframe
st.dataframe(df)

# Plot the data using Plotly Express
plot_title = "Power Usage Over Time"
fig = px.line(df, x='time', y='power', title=plot_title)

# Display the plot
st.plotly_chart(fig, use_container_width=True)

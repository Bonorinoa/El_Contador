# STREAMLIT DASHBOARD [Page 2]
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
import squarify
import seaborn as sb
from update_budget import get_last_text, create_database, update_database

st.title('El Contador: Budget Analysis')

budget = pd.read_csv("Contadurias.csv")

if st.button("Visualizations"):
    # Histogram (Distribution Value)
    fig, ax = plt.subplots()
    ax.hist(budget['Value'], bins=20)

    st.pyplot(fig)
    
    ## Pie Chart (Category; Value)
    st.markdown('## Dummy data (TODO: Replace with budget when fixed)')
    fig_plotly = px.pie(values = [20, 50, 37, 18],
             names = ['G1', 'G2', 'G3', 'G4'],
             color = ['G1', 'G2', 'G3', 'G4'],
             hole = 0.5)
    
    st.plotly_chart(fig_plotly)
    
    ## Funnel chart (Category; Value; Type)
    st.markdown('## Dummy data (TODO: Replace with budget when fixed)')
    # Sample data
    df = pd.DataFrame(dict(
        stage = ['Sent', 'Received', 'Clicks', 'Sales',
                'Sent', 'Received', 'Clicks', 'Sales'],
        percentage = [70, 32, 20, 4,
                    30, 38, 10, 6],
        campaign = ['C1', 'C1', 'C1', 'C1',
                    'C2', 'C2', 'C2', 'C2']))

    plotly_funnel = px.funnel(df, x = 'percentage', y = 'stage', color = 'campaign')

    st.plotly_chart(plotly_funnel)

    ## Boxplot
    st.markdown('## Dummy data (TODO: Replace with budget when fixed)')
    # Sample data
    plotly_boxplot = go.Figure()
    plotly_boxplot.add_trace(go.Box(
        y=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5, 7.5, 7.75, 8.15,
        8.15, 8.65, 8.93, 9.2, 9.5, 10, 10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
        name="All Points",
        jitter=0.3,
        pointpos=-1.8,
        boxpoints='all', # represent all points
        marker_color='rgb(7,40,89)',
        line_color='rgb(7,40,89)'
    ))

    plotly_boxplot.add_trace(go.Box(
        y=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5, 7.5, 7.75, 8.15,
            8.15, 8.65, 8.93, 9.2, 9.5, 10, 10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
        name="Only Whiskers",
        boxpoints=False, # no data points
        marker_color='rgb(9,56,125)',
        line_color='rgb(9,56,125)'
    ))

    plotly_boxplot.add_trace(go.Box(
        y=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5, 7.5, 7.75, 8.15,
            8.15, 8.65, 8.93, 9.2, 9.5, 10, 10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
        name="Suspected Outliers",
        boxpoints='suspectedoutliers', # only suspected outliers
        marker=dict(
            color='rgb(8,81,156)',
            outliercolor='rgba(219, 64, 82, 0.6)',
            line=dict(
                outliercolor='rgba(219, 64, 82, 0.6)',
                outlierwidth=2)),
        line_color='rgb(8,81,156)'
    ))

    plotly_boxplot.add_trace(go.Box(
        y=[0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5, 7.5, 7.75, 8.15,
            8.15, 8.65, 8.93, 9.2, 9.5, 10, 10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
        name="Whiskers and Outliers",
        boxpoints='outliers', # only outliers
        marker_color='rgb(107,174,214)',
        line_color='rgb(107,174,214)'
    ))


    plotly_boxplot.update_layout(title_text="Box Plot Styling Outliers")
    
    st.plotly_chart(plotly_boxplot)
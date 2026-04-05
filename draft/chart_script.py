import plotly.graph_objects as go
import json

# Data from the provided JSON
data = {
    "libraries": ["Recharts", "Chart.js", "ECharts"],
    "metrics": {
        "Ease of Use": [9, 10, 6],
        "React Integration": [10, 6, 7],
        "Performance": [7, 9, 10],
        "Chart Types": [7, 7, 10],
        "TypeScript Support": [9, 7, 8]
    }
}

# Brand colors for the 5 metrics
colors = ['#1FB8CD', '#DB4545', '#2E8B57', '#5D878F', '#D2BA4C']

# Create the figure
fig = go.Figure()

# Add a trace for each metric
for i, (metric, values) in enumerate(data["metrics"].items()):
    # Abbreviate metric names to fit 15 character limit
    metric_abbrev = {
        "Ease of Use": "Ease of Use",
        "React Integration": "React Integ",
        "Performance": "Performance", 
        "Chart Types": "Chart Types",
        "TypeScript Support": "TypeScript"
    }[metric]
    
    fig.add_trace(go.Bar(
        y=data["libraries"],
        x=values,
        name=metric_abbrev,
        orientation='h',
        marker_color=colors[i]
    ))

# Update layout
fig.update_layout(
    title="Chart Library Comparison for Admin Dashboard",
    xaxis_title="Score out of 10",
    yaxis_title="Library",
    barmode='group',
    legend=dict(
        orientation='h', 
        yanchor='bottom', 
        y=1.05, 
        xanchor='center', 
        x=0.5
    )
)

# Update traces with cliponaxis=False for bar charts
fig.update_traces(cliponaxis=False)

# Set x-axis range to 0-10
fig.update_xaxes(range=[0, 10])

# Save as both PNG and SVG
fig.write_image("chart.png")
fig.write_image("chart.svg", format="svg")

print("Chart saved successfully as chart.png and chart.svg")
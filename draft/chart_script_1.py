import plotly.graph_objects as go
import plotly.express as px
import json

# Load the data
data = {
  "tasks": [
    {"task": "Project Setup & Configuration", "start": 0, "duration": 2, "day": 1},
    {"task": "MongoDB Schema & Connection", "start": 2, "duration": 2, "day": 1},
    {"task": "Authentication API Routes", "start": 4, "duration": 4, "day": 1},
    {"task": "Analytics API Routes", "start": 8, "duration": 4, "day": 2},
    {"task": "Middleware & RBAC", "start": 12, "duration": 2, "day": 2},
    {"task": "Dashboard Layout", "start": 14, "duration": 2, "day": 2},
    {"task": "KPI Cards & Charts", "start": 16, "duration": 4, "day": 3},
    {"task": "Leaderboard & Tables", "start": 20, "duration": 2, "day": 3},
    {"task": "Login/Register Pages", "start": 22, "duration": 2, "day": 3},
    {"task": "Responsive Design", "start": 24, "duration": 2, "day": 4},
    {"task": "Testing & Bug Fixes", "start": 26, "duration": 2, "day": 4},
    {"task": "Documentation & Deployment", "start": 28, "duration": 4, "day": 4}
  ]
}

# Define colors for each day (using brand colors in order)
day_colors = {
    1: '#1FB8CD',  # Strong cyan
    2: '#DB4545',  # Bright red
    3: '#2E8B57',  # Sea green
    4: '#5D878F'   # Cyan
}

# Abbreviate task names to 15 characters
task_abbreviations = {
    "Project Setup & Configuration": "Proj Setup",
    "MongoDB Schema & Connection": "MongoDB Schema",
    "Authentication API Routes": "Auth API",
    "Analytics API Routes": "Analytics API",
    "Middleware & RBAC": "Middleware",
    "Dashboard Layout": "Dashboard",
    "KPI Cards & Charts": "KPI Cards",
    "Leaderboard & Tables": "Leaderboard",
    "Login/Register Pages": "Login Pages",
    "Responsive Design": "Responsive",
    "Testing & Bug Fixes": "Testing",
    "Documentation & Deployment": "Documentation"
}

# Create the figure
fig = go.Figure()

# Add bars for each task
for i, task_data in enumerate(data["tasks"]):
    task_name = task_abbreviations[task_data["task"]]
    start_time = task_data["start"]
    duration = task_data["duration"]
    day = task_data["day"]
    
    # Add horizontal bar
    fig.add_trace(go.Bar(
        y=[task_name],
        x=[duration],
        base=[start_time],
        orientation='h',
        marker_color=day_colors[day],
        name=f'Day {day}',
        showlegend=i == 0 or task_data["day"] != data["tasks"][i-1]["day"],  # Show legend only for first occurrence of each day
        hovertemplate=f'<b>{task_name}</b><br>' +
                     f'Start: {start_time}h<br>' +
                     f'Duration: {duration}h<br>' +
                     f'End: {start_time + duration}h<br>' +
                     '<extra></extra>'
    ))

# Update layout
fig.update_layout(
    title="4-Day Project Implementation Timeline",
    xaxis_title="Hours",
    yaxis_title="Tasks",
    barmode='overlay',
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.05,
        xanchor='center',
        x=0.5
    )
)

# Update axes
fig.update_xaxes(range=[0, 32], dtick=4)
fig.update_yaxes(categoryorder="array", categoryarray=[
    "Documentation", "Testing", "Responsive", "Login Pages", 
    "Leaderboard", "KPI Cards", "Dashboard", "Middleware", 
    "Analytics API", "Auth API", "MongoDB Schema", "Proj Setup"
])

# Save as PNG and SVG
fig.write_image("gantt_timeline.png")
fig.write_image("gantt_timeline.svg", format="svg")
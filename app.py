from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)


@app.route('/')
def index():
    # Read the data from the CSV file
    data = pd.read_csv('data.csv')

    # Create graph chart using Plotly
    graph_chart = px.bar(data, x='Category', y='Value', title='Graph Chart', color='Value',
                         color_discrete_sequence=px.colors.qualitative.Set3)

    # Create pie chart using Plotly
    pie_chart = px.pie(data, values='Value', names='Category', title='Pie Chart')

    # Convert the chart data and layout to JSON
    graph_json = graph_chart.to_json()
    pie_json = pie_chart.to_json()

    # Render the dashboard template with the chart JSON
    return render_template('dashboard.html', graph_json=graph_json, pie_json=pie_json)


if __name__ == '__main__':
    app.run(debug=True)

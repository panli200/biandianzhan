from flask import Flask, render_template
import plotly.graph_objs as go
import plotly.offline as pyo
import random
import datetime

app = Flask(__name__)

def generate_data():
    now = datetime.datetime.now()
    times = [(now - datetime.timedelta(minutes=5*i)).strftime('%H:%M') for i in reversed(range(12))]
    values = [round(random.uniform(1.0, 2.5), 2) for _ in range(12)]
    return times, values

def create_chart(title, y_label, color):
    times, values = generate_data()
    trace = go.Scatter(x=times, y=values, mode='lines+markers', line=dict(color=color))
    layout = go.Layout(title=title, xaxis_title='Time', yaxis_title=y_label, margin=dict(t=40, b=40, l=40, r=20))
    fig = go.Figure(data=[trace], layout=layout)
    return pyo.plot(fig, output_type='div', include_plotlyjs=False)

@app.route('/')
def dashboard():
    graphs = {
        'Electricity Usage': create_chart('Electricity Usage', 'kW', '#3b82f6'),
        'Solar Output': create_chart('Solar Output', 'kW', '#facc15'),
        'Battery Storage': create_chart('Battery Storage', 'kWh', '#10b981'),
        'Grid Feed-In': create_chart('Grid Feed-In', 'kW', '#ef4444'),
        'HVAC Power': create_chart('HVAC Power', 'kW', '#8b5cf6'),
        'Lighting': create_chart('Lighting', 'kW', '#f59e0b'),
    }
    return render_template('dashboard.html', graphs=graphs)

if __name__ == '__main__':
    app.run(debug=True)

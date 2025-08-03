from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

def get_electrical_data():
    # Simulated real-time data
    return {
        'ux': 73.00,
        'current': 49.00,
        'power': 229.00,
        'reactive': 253.00,
        'cos': 0.39,
        'ua': 75.00,
        'ub': 43.00,
        'uc': 78.00,
        'ux2': 75.00,
        'ub2': 8.00,
        'uc2': 8.00,
        'uab': 79.00
    }

@app.route('/')
def index():
    data = get_electrical_data()
    current_time = datetime.now().strftime('%H:%M:%S')
    current_date = datetime.now().strftime('%d/%m/%Y')
    return render_template('index.html', data=data, current_time=current_time, current_date=current_date)

if __name__ == '__main__':
    app.run(debug=True)
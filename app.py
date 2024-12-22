from flask import Flask, render_template, request, url_for
import os
import plotly.graph_objects as go
import numpy as np

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/linear_programming', methods=['GET', 'POST'])
def linear_programming():
    plot_url = None
    if request.method == 'POST':
        try:
            x_min = float(request.form['x_min'])
            x_max = float(request.form['x_max'])
            y_min = float(request.form['y_min'])
            y_max = float(request.form['y_max'])
            plot_url = generate_3d_plot(x_min, x_max, y_min, y_max)
        except KeyError as e:
            print(f"Missing form field: {e}")
    return render_template('linear_programming.html', plot_url=plot_url)


def generate_3d_plot(x_min, x_max, y_min, y_max):
    # Generate some data
    x = np.linspace(x_min, x_max, 100)
    y = np.linspace(y_min, y_max, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))

    # Create the plot
    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
    fig.update_layout(title='Plot of Solution to XXX Problem', autosize=True,
                      margin=dict(l=65, r=50, b=65, t=90))

    # Ensure the directory exists
    plot_dir = os.path.join('static', 'plots')
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)

    # Save the plot as an HTML file
    plot_path = os.path.join(plot_dir, '3d_plot.html')
    fig.write_html(plot_path)

    return url_for('static', filename='plots/3d_plot.html')


if __name__ == '__main__':
    app.run(debug=True)

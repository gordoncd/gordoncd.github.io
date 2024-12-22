import plotly.graph_objects as go
import numpy as np


def generate_3d_plot():
    # Generate some data
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))

    # Create the plot
    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
    fig.update_layout(title='Fencing Problem Visualized', autosize=True,
                      margin=dict(l=65, r=50, b=65, t=90), xlabel='$x_1$', ylabel='$x_2$', zlabel='$f(x_1, x_2)$')

    # Save the plot as an HTML file
    fig.write_html('../templates/3d_plot.html')


if __name__ == '__main__':
    generate_3d_plot()

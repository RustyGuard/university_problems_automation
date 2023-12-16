"""
pip install matplotlib
pip install numpy
pip install plotdf

web: https://aeb019.hosted.uark.edu/pplane.html
"""


import numpy as np
from plotdf import plotdf
import matplotlib.pyplot as plt


def plot(dotx, doty, xrange, yrange, inits=None):
    if inits is None:
        inits = [(i, i) for i in range(*xrange)]
    f = lambda params: np.array([dotx(*params), doty(*params)])
    plotdf(f,  # Function giving the rhs of the diff. eq. system
           np.array(xrange),  # [xmin,xmax]
           np.array(yrange),  # [ymin,ymax]
           inits
           )

    plt.show()


if __name__ == '__main__':
    plot(lambda x, y: x - 2*y - 5, lambda x, y: 2*x + y, [-10, 10], [-10, 10])

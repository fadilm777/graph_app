import pandas as pd
import numpy as np

from scipy.spatial import ConvexHull

def graphGenerator(path: str, window):
    """
    A function that takes file path and an object of class MainWindow() 
    and returns x/y values of the hysteresis plot as well as the backbone curve.
    """
    window.ax.cla()
    window._initCanvas()
    if (path.split('.')[-1] == "csv"):
        dataframe = pd.read_csv(path, skiprows=5, usecols=[0, 1], header=None)
    else:
        dataframe = pd.read_excel(path, skiprows=5, usecols="A:B", header=None)
    
    force = pd.Series(pd.to_numeric(dataframe.iloc[:, 1], errors="coerce")).dropna()
    dispersion = pd.Series(pd.to_numeric(dataframe.iloc[:, 0], errors="coerce")).dropna()
    
    force = force.tolist()
    dispersion = dispersion.tolist()
    
    data = dataframe.to_numpy()
    x = dispersion
    y = force

    dfPos = data[(data[:, 0] > 0) & (data[:, 1] > 0)]
    dfNeg = data[(data[:, 0] < 0) & (data[:, 1] < 0)]
    
    max = 0
    xmax = 0
    max_list = []
    x_max = []
    min = 0
    xmin = 0
    min_list = []
    x_min = []

    for i in range(len(x)):
        
        if( x[i] > 0 and y[i] > 0 ):
            if ((min not in min_list) and (min !=0)):
                min_list.append(min)
                x_min.append(xmin)

            if ( y[i] > max):
                max = y[i]
                xmax = x[i]

        elif ( x[i] < 0 and y[i] < 0):
            if max not in max_list: 
                max_list.append(max)
                x_max.append(xmax)

            if (y[i] < min):
                min = y[i]
                xmin = x[i]
    window.plotCanvas(x, y, max_list, min_list, x_max, x_min)

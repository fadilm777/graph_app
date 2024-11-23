import pandas as pd
import numpy as np

from scipy.spatial import ConvexHull

def graphGenerator(path: str, window):
    window.ax.cla()
    window._initCanvas()
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
    
    boundaryPos = ConvexHull(dfPos)
    dispEnvPos1, forceEnvPos1 = dfPos[boundaryPos.vertices, 0], dfPos[boundaryPos.vertices, 1]
    boundaryNeg = ConvexHull(dfNeg)
    dispEnvNeg1, forceEnvNeg1 = dfNeg[boundaryNeg.vertices, 0], dfNeg[boundaryNeg.vertices, 1]
    
    posIndices = []
    negIndices = []
    
    for i in range(1, len(dispEnvPos1)):
        if(dispEnvPos1[i] < dispEnvPos1[i-1]):
            posIndices.append(i)
    
    posEnvTemp = (np.vstack((dispEnvPos1[posIndices], forceEnvPos1[posIndices]))).T
    zeroArray = np.array([[0., 0.]])
    posEnv = np.vstack((posEnvTemp, zeroArray))
    
    for i in range(1, len(dispEnvNeg1)):
        if(dispEnvNeg1[i] > dispEnvNeg1[i-1]):
            negIndices.append(i)
    
    negEnvTemp = (np.vstack((dispEnvNeg1[negIndices], forceEnvNeg1[negIndices]))).T
    zeroArray = np.array([[0., 0.]])
    negEnv = np.vstack((negEnvTemp, zeroArray))
    window.plotCanvas(dispEnvPos1=dispEnvPos1, forceEnvPos1=forceEnvPos1, x=x, y=y, negEnv=negEnv)

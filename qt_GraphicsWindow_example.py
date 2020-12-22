import time
import random
import pyqtgraph as pg
from collections import deque
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np


class Graph:
    def __init__(self,range0, ):
        ## init parameter
        self.maxLen = range0  #max number of data points to show on graph
        self.plotArray = []

        self.dat = deque()
        self.app = QtGui.QApplication([])
        self.win = pg.GraphicsWindow()
       
        self.p1 = self.win.addPlot(colspan=5)
        ## add new row for other plot !
        # self.win.nextRow()
        # self.p2 = self.win.addPlot(colspan=2)

        self.curve1 = self.p1.plot()
        
        graphUpdateSpeedMs = 50
        timer = QtCore.QTimer() #to create a thread that calls a function at intervals
        timer.timeout.connect(self.update) #the update function keeps getting called at intervals
        timer.start(graphUpdateSpeedMs)   
        QtGui.QApplication.instance().exec_()
    
       
    def update(self):
        data = random.randint(0,100)

        if len(self.plotArray) < self.maxLen:
            self.plotArray.append(data)
        else:
            self.plotArray[:-1] = self.plotArray[1:]
            self.plotArray[-1] = data
        
        self.curve1.setData(np.reshape(self.plotArray, (-1)))
        self.app.processEvents()  
       

if __name__ == '__main__':
    SingalRange = 100
    g = Graph(SingalRange)
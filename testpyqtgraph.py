"""TestProgramm"""
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore

app = QtGui.QApplication([])
mw = QtGui.QMainWindow()

layout = pg.GraphicsLayoutWidget()
layout.setBackground(background='w')
mw.setCentralWidget(layout)
mw.show()

p1 = layout.addPlot(title="CPU Usage", row=0, col=0)
x1 = np.arange(100)
y1 = np.random.random(size=100)
curve = p1.plot(fillLevel=0.0, pen='b', brush=(50,50,200,100))
curve.setData(x=x1, y=y1)

p2 = layout.addPlot(title="Network Monitor", row=1, col=0)
x2 = np.arange(100)
y2 = np.random.random(size=100)
curve = p2.plot(fillLevel=0.0, pen='r', brush=(200,50,50,100))
curve.setData(x=x2, y=y2)


if __name__ == '__main__':
        QtGui.QApplication.instance().exec_()
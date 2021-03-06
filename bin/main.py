from __future__ import with_statement
import numpy as np
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MplMainWindow
import threading
from lifethread import LifeThread
import multiprocessing

ALIVE = 1
DEAD = 0

class MyListModel(QtCore.QAbstractListModel): 
    def __init__(self, datain, parent=None, *args): 
        """ datain: a list where each item is a row
        """
        QtCore.QAbstractListModel.__init__(self, parent, *args) 
        self.listdata = datain
 
    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self.listdata) 
 
    def data(self, index, role): 
        if index.isValid() and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.listdata[index.row()])
        else: 
            return QtCore.QVariant()

class DesignerMainWindow(QtWidgets.QMainWindow, Ui_MplMainWindow):
    def __init__(self, parent=None):
        super(DesignerMainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.counter = 1
        self.size = 200
        print("thread count=", multiprocessing.cpu_count())
        self.thread_count = multiprocessing.cpu_count()
        self.grid = np.random.choice([ALIVE, DEAD], self.size * self.size, p=[0.1, 0.9]).reshape(self.size, self.size)
        self.mat = self.mpl.canvas.ax.matshow(self.grid, interpolation='none', cmap='Greens')
        
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)
        
        self.resume_button_clicked()
        self.list_configs()
        
        self.pauseButton.clicked.connect(self.pause_button_clicked)
        #self.resumeButton.clicked.connect(self.resume_button_clicked)
        self.stepModeButton.clicked.connect(self.activate_step_by_step)
        self.nextStepButton.clicked.connect(self.update)
        self.horizontalSlider.valueChanged.connect(self.slider_moved)
        self.fileMod.setText("Random")
        self.genMod.setText(str(self.counter))
        self.speedMod.setText(str(self.horizontalSlider.value()))
        
        
    def pause_button_clicked(self):
        self.timer.stop()
        self.pauseButton.setText("Resume Simulation")
        self.pauseButton.clicked.connect(self.resume_button_clicked)
        
    def resume_button_clicked(self):
        self.timer.start(self.horizontalSlider.value())
        self.pauseButton.setText("Pause Simulation")
        self.pauseButton.clicked.connect(self.pause_button_clicked)
        
    def slider_moved(self):
        self.timer.start(self.horizontalSlider.value())
        self.speedMod.setText(str(self.horizontalSlider.value()))

        
    def activate_step_by_step(self):
        self.pause_button_clicked()
        self.nextStepButton.setEnabled(True)
        self.stepModeButton.setText("Disable Step-by-Step")
        self.stepModeButton.clicked.connect(self.disable_step_by_step)
    
    def disable_step_by_step(self):
        self.resume_button_clicked()
        self.nextStepButton.setEnabled(False)
        self.stepModeButton.clicked.connect(self.activate_step_by_step)
        self.stepModeButton.setText("Enable Step-by-Step")
        
    def list_configs(self):
        initial_list = os.listdir("../config/")
        list_model = MyListModel(initial_list, self)
        self.listView.setModel(list_model)
        
    def select_file(self):
        file = QtGui.QFileDialog.getOpenFileName()
        if file:
            self.mpllineEdit.setText(file)

    def parse_file(self, filename):
        pass
    
    def thread_update(self):
        threading.Thread(target=self.update).start()

    def update(self):
        newGrid = np.empty([self.size,self.size])
        for i in range(self.thread_count):
            exec(
                "thread{} = LifeThread(self.grid[{}:{}], self.size, self.size//self.thread_count)".format(
                    i, "" if i == 0 else i*(self.size//self.thread_count),
                    "" if i==4 else (i+1)*(self.size//self.thread_count))
            )
            exec("thread{}.start()".format(i))
        for i in range(self.thread_count):
            exec(
                "newGrid[{}:{}] = thread{}.join()".format(
                    "" if i == 0 else i*(self.size//self.thread_count),
                    "" if i==4 else (i+1)*(self.size//self.thread_count),i)
            )
        self.counter += 1
        self.genMod.setText(str(self.counter))
        self.mat.set_data(newGrid)
        self.grid = newGrid
        # self.mpl.canvas.ax.clear()
        # self.mat = self.mpl.canvas.ax.matshow(self.grid, interpolation='sinc', cmap='tab20c')
        self.mpl.canvas.draw()


# create the GUI application
app = QtWidgets.QApplication(sys.argv)
# instantiate the main window
dmw = DesignerMainWindow()
# show it
dmw.show()
# start the Qt main loop execution, exiting from this script
# with the same return code of Qt application
sys.exit(app.exec_())

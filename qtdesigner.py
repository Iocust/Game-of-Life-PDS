# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdesigner.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MplMainWindow(object):
    def setupUi(self, MplMainWindow):
        MplMainWindow.setObjectName("MplMainWindow")
        MplMainWindow.resize(786, 600)
        self.mplcentralwidget = QtWidgets.QWidget(MplMainWindow)
        self.mplcentralwidget.setObjectName("mplcentralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mplcentralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mplhorizontalLayout = QtWidgets.QHBoxLayout()
        self.mplhorizontalLayout.setObjectName("mplhorizontalLayout")
        self.mpllineEdit = QtWidgets.QLineEdit(self.mplcentralwidget)
        self.mpllineEdit.setText("")
        self.mpllineEdit.setObjectName("mpllineEdit")
        self.mplhorizontalLayout.addWidget(self.mpllineEdit)
        self.mplpushButton = QtWidgets.QPushButton(self.mplcentralwidget)
        self.mplpushButton.setObjectName("mplpushButton")
        self.mplhorizontalLayout.addWidget(self.mplpushButton)
        self.verticalLayout.addLayout(self.mplhorizontalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalSlider = QtWidgets.QSlider(self.mplcentralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_5.addWidget(self.horizontalSlider)
        self.label = QtWidgets.QLabel(self.mplcentralwidget)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.pushButton_2 = QtWidgets.QPushButton(self.mplcentralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.mplcentralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.mplcentralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.mplcentralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton = QtWidgets.QPushButton(self.mplcentralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.mpl = MplWidget(self.mplcentralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl.sizePolicy().hasHeightForWidth())
        self.mpl.setSizePolicy(sizePolicy)
        self.mpl.setObjectName("mpl")
        self.verticalLayout.addWidget(self.mpl)
        MplMainWindow.setCentralWidget(self.mplcentralwidget)
        self.menubar = QtWidgets.QMenuBar(MplMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 786, 21))
        self.menubar.setObjectName("menubar")
        self.mplmenuFile = QtWidgets.QMenu(self.menubar)
        self.mplmenuFile.setObjectName("mplmenuFile")
        MplMainWindow.setMenuBar(self.menubar)
        self.mplactionOpen = QtWidgets.QAction(MplMainWindow)
        self.mplactionOpen.setObjectName("mplactionOpen")
        self.actionExit = QtWidgets.QAction(MplMainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit_2 = QtWidgets.QAction(MplMainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.mplactionQuit = QtWidgets.QAction(MplMainWindow)
        self.mplactionQuit.setObjectName("mplactionQuit")
        self.mplmenuFile.addAction(self.mplactionOpen)
        self.mplmenuFile.addSeparator()
        self.mplmenuFile.addAction(self.mplactionQuit)
        self.menubar.addAction(self.mplmenuFile.menuAction())

        self.retranslateUi(MplMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MplMainWindow)

    def retranslateUi(self, MplMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MplMainWindow.setWindowTitle(_translate("MplMainWindow", "MainWindow"))
        self.mplpushButton.setText(_translate("MplMainWindow", "Execute"))
        self.label.setText(_translate("MplMainWindow", "Speed"))
        self.pushButton_2.setText(_translate("MplMainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MplMainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MplMainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MplMainWindow", "PushButton"))
        self.pushButton.setText(_translate("MplMainWindow", "PushButton"))
        self.mplmenuFile.setTitle(_translate("MplMainWindow", "File"))
        self.mplactionOpen.setText(_translate("MplMainWindow", "Open"))
        self.actionExit.setText(_translate("MplMainWindow", "Pause"))
        self.actionExit_2.setText(_translate("MplMainWindow", "Exit"))
        self.mplactionQuit.setText(_translate("MplMainWindow", "Quit"))

from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MplMainWindow = QtWidgets.QMainWindow()
    ui = Ui_MplMainWindow()
    ui.setupUi(MplMainWindow)
    MplMainWindow.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'distDirAttr.ui'
#
# Created: Mon Mar 12 16:34:58 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_distDirAttr(object):
    def setupUi(self, distDirAttr):
        distDirAttr.setObjectName("distDirAttr")
        distDirAttr.resize(305, 201)
        self.gridLayout = QtGui.QGridLayout(distDirAttr)
        self.gridLayout.setObjectName("gridLayout")
        self.minDistLabel = QtGui.QLabel(distDirAttr)
        self.minDistLabel.setObjectName("minDistLabel")
        self.gridLayout.addWidget(self.minDistLabel, 0, 0, 1, 1)
        self.minDist = QtGui.QDoubleSpinBox(distDirAttr)
        self.minDist.setDecimals(3)
        self.minDist.setMinimum(-1000000000.0)
        self.minDist.setMaximum(1000000000.0)
        self.minDist.setProperty("value", 0.0)
        self.minDist.setObjectName("minDist")
        self.gridLayout.addWidget(self.minDist, 0, 1, 1, 1)
        self.maxDistLabel = QtGui.QLabel(distDirAttr)
        self.maxDistLabel.setObjectName("maxDistLabel")
        self.gridLayout.addWidget(self.maxDistLabel, 1, 0, 1, 1)
        self.maxDist = QtGui.QDoubleSpinBox(distDirAttr)
        self.maxDist.setDecimals(3)
        self.maxDist.setMinimum(-1000000000.0)
        self.maxDist.setMaximum(1000000000.0)
        self.maxDist.setProperty("value", 0.0)
        self.maxDist.setObjectName("maxDist")
        self.gridLayout.addWidget(self.maxDist, 1, 1, 1, 1)
        self.dirXLabel = QtGui.QLabel(distDirAttr)
        self.dirXLabel.setObjectName("dirXLabel")
        self.gridLayout.addWidget(self.dirXLabel, 2, 0, 1, 1)
        self.dirX = QtGui.QDoubleSpinBox(distDirAttr)
        self.dirX.setDecimals(3)
        self.dirX.setMinimum(-1000000000.0)
        self.dirX.setMaximum(1000000000.0)
        self.dirX.setProperty("value", 1.0)
        self.dirX.setObjectName("dirX")
        self.gridLayout.addWidget(self.dirX, 2, 1, 1, 1)
        self.dirYLabel = QtGui.QLabel(distDirAttr)
        self.dirYLabel.setObjectName("dirYLabel")
        self.gridLayout.addWidget(self.dirYLabel, 3, 0, 1, 1)
        self.dirY = QtGui.QDoubleSpinBox(distDirAttr)
        self.dirY.setDecimals(3)
        self.dirY.setMinimum(-1000000000.0)
        self.dirY.setMaximum(1000000000.0)
        self.dirY.setProperty("value", 0.0)
        self.dirY.setObjectName("dirY")
        self.gridLayout.addWidget(self.dirY, 3, 1, 1, 1)
        self.dirZLabel = QtGui.QLabel(distDirAttr)
        self.dirZLabel.setObjectName("dirZLabel")
        self.gridLayout.addWidget(self.dirZLabel, 4, 0, 1, 1)
        self.dirZ = QtGui.QDoubleSpinBox(distDirAttr)
        self.dirZ.setDecimals(3)
        self.dirZ.setMinimum(-1000000000.0)
        self.dirZ.setMaximum(1000000000.0)
        self.dirZ.setProperty("value", 0.0)
        self.dirZ.setObjectName("dirZ")
        self.gridLayout.addWidget(self.dirZ, 4, 1, 1, 1)
        self.spreadLabel = QtGui.QLabel(distDirAttr)
        self.spreadLabel.setObjectName("spreadLabel")
        self.gridLayout.addWidget(self.spreadLabel, 5, 0, 1, 1)
        self.spread = QtGui.QDoubleSpinBox(distDirAttr)
        self.spread.setDecimals(3)
        self.spread.setMinimum(0.0)
        self.spread.setMaximum(1.0)
        self.spread.setSingleStep(0.01)
        self.spread.setProperty("value", 0.0)
        self.spread.setObjectName("spread")
        self.gridLayout.addWidget(self.spread, 5, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 1, 1, 1)

        self.retranslateUi(distDirAttr)
        QtCore.QMetaObject.connectSlotsByName(distDirAttr)

    def retranslateUi(self, distDirAttr):
        distDirAttr.setWindowTitle(QtGui.QApplication.translate("distDirAttr", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.minDistLabel.setText(QtGui.QApplication.translate("distDirAttr", "Min Distance", None, QtGui.QApplication.UnicodeUTF8))
        self.maxDistLabel.setText(QtGui.QApplication.translate("distDirAttr", "Max Distance", None, QtGui.QApplication.UnicodeUTF8))
        self.dirXLabel.setText(QtGui.QApplication.translate("distDirAttr", "Direction X", None, QtGui.QApplication.UnicodeUTF8))
        self.dirYLabel.setText(QtGui.QApplication.translate("distDirAttr", "Direction Y", None, QtGui.QApplication.UnicodeUTF8))
        self.dirZLabel.setText(QtGui.QApplication.translate("distDirAttr", "Direction Z", None, QtGui.QApplication.UnicodeUTF8))
        self.spreadLabel.setText(QtGui.QApplication.translate("distDirAttr", "Spread", None, QtGui.QApplication.UnicodeUTF8))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ColorbarRange.ui'
#
# Created: Tue Jul 30 17:10:00 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ColorbarDialog(object):
    def setupUi(self, ColorbarDialog):
        ColorbarDialog.setObjectName("ColorbarDialog")
        ColorbarDialog.resize(362, 253)
        self.buttonBox = QtGui.QDialogButtonBox(ColorbarDialog)
        self.buttonBox.setGeometry(QtCore.QRect(-110, 190, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.minContour = QtGui.QDoubleSpinBox(ColorbarDialog)
        self.minContour.setEnabled(False)
        self.minContour.setGeometry(QtCore.QRect(160, 130, 81, 21))
        self.minContour.setMinimum(-999999999.0)
        self.minContour.setMaximum(999999999.0)
        self.minContour.setObjectName("minContour")
        self.maxContour = QtGui.QDoubleSpinBox(ColorbarDialog)
        self.maxContour.setEnabled(False)
        self.maxContour.setGeometry(QtCore.QRect(260, 130, 81, 21))
        self.maxContour.setMinimum(-999999999.0)
        self.maxContour.setMaximum(999999999.0)
        self.maxContour.setObjectName("maxContour")
        self.autoselectRange = QtGui.QCheckBox(ColorbarDialog)
        self.autoselectRange.setGeometry(QtCore.QRect(40, 40, 101, 51))
        self.autoselectRange.setChecked(True)
        self.autoselectRange.setObjectName("autoselectRange")
        self.label_2 = QtGui.QLabel(ColorbarDialog)
        self.label_2.setGeometry(QtCore.QRect(190, 110, 21, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtGui.QLabel(ColorbarDialog)
        self.label.setGeometry(QtCore.QRect(290, 110, 31, 16))
        self.label.setObjectName("label")
        self.fixedColorbar = QtGui.QCheckBox(ColorbarDialog)
        self.fixedColorbar.setGeometry(QtCore.QRect(40, 90, 161, 20))
        self.fixedColorbar.setObjectName("fixedColorbar")
        self.ManualRange = QtGui.QCheckBox(ColorbarDialog)
        self.ManualRange.setGeometry(QtCore.QRect(40, 130, 87, 20))
        self.ManualRange.setObjectName("ManualRange")

        self.retranslateUi(ColorbarDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ColorbarDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ColorbarDialog.reject)
        QtCore.QObject.connect(self.ManualRange, QtCore.SIGNAL("toggled(bool)"), self.maxContour.setEnabled)
        QtCore.QObject.connect(self.ManualRange, QtCore.SIGNAL("toggled(bool)"), self.minContour.setEnabled)
        QtCore.QObject.connect(self.ManualRange, QtCore.SIGNAL("clicked(bool)"), self.fixedColorbar.setChecked)
        QtCore.QObject.connect(self.ManualRange, QtCore.SIGNAL("clicked(bool)"), self.autoselectRange.setChecked)
        QtCore.QObject.connect(self.fixedColorbar, QtCore.SIGNAL("clicked(bool)"), self.ManualRange.setChecked)
        QtCore.QObject.connect(self.fixedColorbar, QtCore.SIGNAL("clicked(bool)"), self.autoselectRange.setChecked)
        QtCore.QObject.connect(self.autoselectRange, QtCore.SIGNAL("clicked(bool)"), self.ManualRange.setChecked)
        QtCore.QObject.connect(self.autoselectRange, QtCore.SIGNAL("clicked(bool)"), self.fixedColorbar.setChecked)
        QtCore.QObject.connect(self.ManualRange, QtCore.SIGNAL("clicked()"), self.autoselectRange.toggle)
        QtCore.QObject.connect(self.ManualRange, QtCore.SIGNAL("clicked()"), self.fixedColorbar.toggle)
        QtCore.QObject.connect(self.autoselectRange, QtCore.SIGNAL("clicked()"), self.ManualRange.toggle)
        QtCore.QObject.connect(self.autoselectRange, QtCore.SIGNAL("clicked()"), self.fixedColorbar.toggle)
        QtCore.QObject.connect(self.fixedColorbar, QtCore.SIGNAL("clicked()"), self.ManualRange.toggle)
        QtCore.QObject.connect(self.fixedColorbar, QtCore.SIGNAL("clicked()"), self.autoselectRange.toggle)
        QtCore.QObject.connect(self.ManualRange, QtCore.SIGNAL("toggled(bool)"), self.ManualRange.setDisabled)
        QtCore.QObject.connect(self.autoselectRange, QtCore.SIGNAL("toggled(bool)"), self.autoselectRange.setDisabled)
        QtCore.QObject.connect(self.fixedColorbar, QtCore.SIGNAL("toggled(bool)"), self.fixedColorbar.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(ColorbarDialog)

    def retranslateUi(self, ColorbarDialog):
        ColorbarDialog.setWindowTitle(QtGui.QApplication.translate("ColorbarDialog", "Colorbar Range", None, QtGui.QApplication.UnicodeUTF8))
        self.autoselectRange.setToolTip(QtGui.QApplication.translate("ColorbarDialog", "Select the range over which the colorbar is set", None, QtGui.QApplication.UnicodeUTF8))
        self.autoselectRange.setText(QtGui.QApplication.translate("ColorbarDialog", "Automatic", None, QtGui.QApplication.UnicodeUTF8))
        self.autoselectRange.setShortcut(QtGui.QApplication.translate("ColorbarDialog", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ColorbarDialog", "Min", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ColorbarDialog", "Max", None, QtGui.QApplication.UnicodeUTF8))
        self.fixedColorbar.setText(QtGui.QApplication.translate("ColorbarDialog", "Fix Across all Slices", None, QtGui.QApplication.UnicodeUTF8))
        self.fixedColorbar.setShortcut(QtGui.QApplication.translate("ColorbarDialog", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.ManualRange.setText(QtGui.QApplication.translate("ColorbarDialog", "Manual", None, QtGui.QApplication.UnicodeUTF8))
        self.ManualRange.setShortcut(QtGui.QApplication.translate("ColorbarDialog", "M", None, QtGui.QApplication.UnicodeUTF8))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ImportSignalFromMATWindow.ui'
#
# Created: Mon Jul 06 15:52:33 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ImportSignalFromMATWindow(object):
    def setupUi(self, ImportSignalFromMATWindow):
        ImportSignalFromMATWindow.setObjectName(_fromUtf8("ImportSignalFromMATWindow"))
        ImportSignalFromMATWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(10)
        ImportSignalFromMATWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(ImportSignalFromMATWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_input_file_preview = QtGui.QLabel(self.centralwidget)
        self.label_input_file_preview.setMinimumSize(QtCore.QSize(0, 20))
        self.label_input_file_preview.setMaximumSize(QtCore.QSize(120, 40))
        self.label_input_file_preview.setIndent(10)
        self.label_input_file_preview.setObjectName(_fromUtf8("label_input_file_preview"))
        self.gridLayout_2.addWidget(self.label_input_file_preview, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem, 0, 9, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem2, 9, 9, 2, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem3, 2, 9, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem4, 9, 0, 2, 7)
        self.tableWidget_input_preview = QtGui.QTableWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_input_preview.sizePolicy().hasHeightForWidth())
        self.tableWidget_input_preview.setSizePolicy(sizePolicy)
        self.tableWidget_input_preview.setMinimumSize(QtCore.QSize(0, 20))
        self.tableWidget_input_preview.setMaximumSize(QtCore.QSize(16777215, 160))
        self.tableWidget_input_preview.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_input_preview.setObjectName(_fromUtf8("tableWidget_input_preview"))
        self.tableWidget_input_preview.setColumnCount(0)
        self.tableWidget_input_preview.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget_input_preview, 2, 0, 1, 9)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem5, 7, 9, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem6, 6, 9, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem7, 5, 9, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem8, 8, 9, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 0, 4, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem10, 4, 9, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 0, 6, 1, 1)
        self.pushButton_Import = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Import.sizePolicy().hasHeightForWidth())
        self.pushButton_Import.setSizePolicy(sizePolicy)
        self.pushButton_Import.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_Import.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Import.setFont(font)
        self.pushButton_Import.setObjectName(_fromUtf8("pushButton_Import"))
        self.gridLayout_2.addWidget(self.pushButton_Import, 9, 7, 2, 2)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem12, 0, 7, 1, 1)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem13, 0, 5, 1, 1)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem14, 0, 8, 1, 1)
        spacerItem15 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem15, 3, 9, 1, 1)
        self.radioButton_select_all = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_select_all.setObjectName(_fromUtf8("radioButton_select_all"))
        self.gridLayout_2.addWidget(self.radioButton_select_all, 1, 7, 1, 2)
        self.label_select = QtGui.QLabel(self.centralwidget)
        self.label_select.setObjectName(_fromUtf8("label_select"))
        self.gridLayout_2.addWidget(self.label_select, 1, 1, 1, 6)
        self.listWidget_columns_names = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_columns_names.sizePolicy().hasHeightForWidth())
        self.listWidget_columns_names.setSizePolicy(sizePolicy)
        self.listWidget_columns_names.setMinimumSize(QtCore.QSize(0, 20))
        self.listWidget_columns_names.setMaximumSize(QtCore.QSize(16777215, 100))
        self.listWidget_columns_names.setObjectName(_fromUtf8("listWidget_columns_names"))
        self.gridLayout_2.addWidget(self.listWidget_columns_names, 6, 1, 2, 1)
        self.pushButton_removeColumn = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_removeColumn.sizePolicy().hasHeightForWidth())
        self.pushButton_removeColumn.setSizePolicy(sizePolicy)
        self.pushButton_removeColumn.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_removeColumn.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_removeColumn.setObjectName(_fromUtf8("pushButton_removeColumn"))
        self.gridLayout_2.addWidget(self.pushButton_removeColumn, 7, 2, 1, 1)
        self.pushButton_addColumn = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_addColumn.sizePolicy().hasHeightForWidth())
        self.pushButton_addColumn.setSizePolicy(sizePolicy)
        self.pushButton_addColumn.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_addColumn.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_addColumn.setObjectName(_fromUtf8("pushButton_addColumn"))
        self.gridLayout_2.addWidget(self.pushButton_addColumn, 6, 2, 1, 1)
        self.label_columns_names = QtGui.QLabel(self.centralwidget)
        self.label_columns_names.setMinimumSize(QtCore.QSize(0, 20))
        self.label_columns_names.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_columns_names.setIndent(10)
        self.label_columns_names.setObjectName(_fromUtf8("label_columns_names"))
        self.gridLayout_2.addWidget(self.label_columns_names, 6, 0, 2, 1)
        self.lineEdit_unit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_unit.sizePolicy().hasHeightForWidth())
        self.lineEdit_unit.setSizePolicy(sizePolicy)
        self.lineEdit_unit.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_unit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_unit.setObjectName(_fromUtf8("lineEdit_unit"))
        self.gridLayout_2.addWidget(self.lineEdit_unit, 4, 1, 1, 1)
        self.label_unit = QtGui.QLabel(self.centralwidget)
        self.label_unit.setMinimumSize(QtCore.QSize(0, 20))
        self.label_unit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_unit.setIndent(10)
        self.label_unit.setObjectName(_fromUtf8("label_unit"))
        self.gridLayout_2.addWidget(self.label_unit, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        spacerItem16 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem16, 1, 0, 1, 1)
        ImportSignalFromMATWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ImportSignalFromMATWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        ImportSignalFromMATWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ImportSignalFromMATWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ImportSignalFromMATWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ImportSignalFromMATWindow)
        QtCore.QMetaObject.connectSlotsByName(ImportSignalFromMATWindow)

    def retranslateUi(self, ImportSignalFromMATWindow):
        ImportSignalFromMATWindow.setWindowTitle(_translate("ImportSignalFromMATWindow", "Import a Signal from MAT file", None))
        self.label_input_file_preview.setText(_translate("ImportSignalFromMATWindow", "Input file preview : ", None))
        self.pushButton_Import.setText(_translate("ImportSignalFromMATWindow", "Import", None))
        self.radioButton_select_all.setText(_translate("ImportSignalFromMATWindow", "Select All", None))
        self.label_select.setText(_translate("ImportSignalFromMATWindow", "Select wanted variables by clicking on columns in the preview\n"
" (press Ctrl for multiple selection)", None))
        self.pushButton_removeColumn.setText(_translate("ImportSignalFromMATWindow", "-", None))
        self.pushButton_addColumn.setText(_translate("ImportSignalFromMATWindow", "+", None))
        self.label_columns_names.setText(_translate("ImportSignalFromMATWindow", "Define the columns names\n"
"associated to each \n"
"variable selected  :", None))
        self.label_unit.setText(_translate("ImportSignalFromMATWindow", "Define the time unit : ", None))

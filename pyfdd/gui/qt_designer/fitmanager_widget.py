# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fitmanager_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FitManagerWidget(object):
    def setupUi(self, FitManagerWidget):
        FitManagerWidget.setObjectName("FitManagerWidget")
        FitManagerWidget.resize(1150, 670)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FitManagerWidget.sizePolicy().hasHeightForWidth())
        FitManagerWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(FitManagerWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mplwindow = QtWidgets.QWidget(FitManagerWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow.sizePolicy().hasHeightForWidth())
        self.mplwindow.setSizePolicy(sizePolicy)
        self.mplwindow.setMinimumSize(QtCore.QSize(550, 550))
        self.mplwindow.setMaximumSize(QtCore.QSize(6000, 6000))
        self.mplwindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.mplwindow.setAutoFillBackground(False)
        self.mplwindow.setObjectName("mplwindow")
        self.mplvl = QtWidgets.QHBoxLayout(self.mplwindow)
        self.mplvl.setContentsMargins(9, 9, 9, 9)
        self.mplvl.setSpacing(6)
        self.mplvl.setObjectName("mplvl")
        self.textBrowser = QtWidgets.QTextBrowser(self.mplwindow)
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textBrowser.setObjectName("textBrowser")
        self.mplvl.addWidget(self.textBrowser)
        self.horizontalLayout.addWidget(self.mplwindow)
        self.widget_2 = QtWidgets.QWidget(FitManagerWidget)
        self.widget_2.setMaximumSize(QtCore.QSize(340, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.info_groupBox = QtWidgets.QGroupBox(self.widget_2)
        self.info_groupBox.setMinimumSize(QtCore.QSize(300, 0))
        self.info_groupBox.setObjectName("info_groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.info_groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.infotext = QtWidgets.QTextBrowser(self.info_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infotext.sizePolicy().hasHeightForWidth())
        self.infotext.setSizePolicy(sizePolicy)
        self.infotext.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.infotext.setFont(font)
        self.infotext.setAcceptRichText(True)
        self.infotext.setObjectName("infotext")
        self.verticalLayout_3.addWidget(self.infotext)
        self.pb_fitconfig = QtWidgets.QPushButton(self.info_groupBox)
        self.pb_fitconfig.setObjectName("pb_fitconfig")
        self.verticalLayout_3.addWidget(self.pb_fitconfig)
        self.verticalLayout_2.addWidget(self.info_groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 281, 80))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.sitesrange_layout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.sitesrange_layout.setObjectName("sitesrange_layout")
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.sitesrange_layout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label.setObjectName("label")
        self.sitesrange_layout.addWidget(self.label, 0, 0, 1, 1)
        self.lb_site1_name = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_site1_name.sizePolicy().hasHeightForWidth())
        self.lb_site1_name.setSizePolicy(sizePolicy)
        self.lb_site1_name.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lb_site1_name.setObjectName("lb_site1_name")
        self.sitesrange_layout.addWidget(self.lb_site1_name, 1, 0, 1, 1)
        self.le_site1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.le_site1.setEnabled(True)
        self.le_site1.setObjectName("le_site1")
        self.sitesrange_layout.addWidget(self.le_site1, 1, 1, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.addWidget(self.scrollArea_2)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 281, 250))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.parameters_layout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.parameters_layout.setObjectName("parameters_layout")
        self.lb_dx_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lb_dx_name.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lb_dx_name.setObjectName("lb_dx_name")
        self.parameters_layout.addWidget(self.lb_dx_name, 0, 0, 1, 1)
        self.pb_sigma = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pb_sigma.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_sigma.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pb_sigma.setObjectName("pb_sigma")
        self.parameters_layout.addWidget(self.pb_sigma, 4, 2, 1, 1)
        self.pb_dy = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pb_dy.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_dy.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pb_dy.setObjectName("pb_dy")
        self.parameters_layout.addWidget(self.pb_dy, 2, 2, 1, 1)
        self.lb_dy_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lb_dy_name.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lb_dy_name.setObjectName("lb_dy_name")
        self.parameters_layout.addWidget(self.lb_dy_name, 2, 0, 1, 1)
        self.pb_dx = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pb_dx.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_dx.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pb_dx.setObjectName("pb_dx")
        self.parameters_layout.addWidget(self.pb_dx, 0, 2, 1, 1)
        self.pb_reset = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pb_reset.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_reset.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pb_reset.setObjectName("pb_reset")
        self.parameters_layout.addWidget(self.pb_reset, 7, 2, 1, 1)
        self.lb_sigma = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lb_sigma.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lb_sigma.setObjectName("lb_sigma")
        self.parameters_layout.addWidget(self.lb_sigma, 4, 1, 1, 1)
        self.lb_phi_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lb_phi_name.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lb_phi_name.setObjectName("lb_phi_name")
        self.parameters_layout.addWidget(self.lb_phi_name, 3, 0, 1, 1)
        self.lb_dx = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lb_dx.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lb_dx.setObjectName("lb_dx")
        self.parameters_layout.addWidget(self.lb_dx, 0, 1, 1, 1)
        self.lb_total_cts = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lb_total_cts.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lb_total_cts.setObjectName("lb_total_cts")
        self.parameters_layout.addWidget(self.lb_total_cts, 5, 1, 1, 1)
        self.lb_phi = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lb_phi.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lb_phi.setObjectName("lb_phi")
        self.parameters_layout.addWidget(self.lb_phi, 3, 1, 1, 1)
        self.lb_sigma_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lb_sigma_name.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lb_sigma_name.setObjectName("lb_sigma_name")
        self.parameters_layout.addWidget(self.lb_sigma_name, 4, 0, 1, 1)
        self.pb_phi = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pb_phi.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_phi.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pb_phi.setObjectName("pb_phi")
        self.parameters_layout.addWidget(self.pb_phi, 3, 2, 1, 1)
        self.pb_f1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pb_f1.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_f1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pb_f1.setObjectName("pb_f1")
        self.parameters_layout.addWidget(self.pb_f1, 6, 2, 1, 1)
        self.lb_dy = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lb_dy.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lb_dy.setObjectName("lb_dy")
        self.parameters_layout.addWidget(self.lb_dy, 2, 1, 1, 1)
        self.lb_f1_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lb_f1_name.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lb_f1_name.setObjectName("lb_f1_name")
        self.parameters_layout.addWidget(self.lb_f1_name, 6, 0, 1, 1)
        self.lb_total_cts_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lb_total_cts_name.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lb_total_cts_name.setObjectName("lb_total_cts_name")
        self.parameters_layout.addWidget(self.lb_total_cts_name, 5, 0, 1, 1)
        self.pb_total_cts = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pb_total_cts.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_total_cts.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pb_total_cts.setObjectName("pb_total_cts")
        self.parameters_layout.addWidget(self.pb_total_cts, 5, 2, 1, 1)
        self.lb_f1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lb_f1.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lb_f1.setObjectName("lb_f1")
        self.parameters_layout.addWidget(self.lb_f1, 6, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_4.addWidget(self.pushButton_4, 3, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox_4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 1, 1, 1, 1)
        self.pb_abortfits = QtWidgets.QPushButton(self.groupBox_4)
        self.pb_abortfits.setObjectName("pb_abortfits")
        self.gridLayout_4.addWidget(self.pb_abortfits, 0, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_4.addWidget(self.pushButton_14, 2, 0, 1, 1)
        self.pb_runfits = QtWidgets.QPushButton(self.groupBox_4)
        self.pb_runfits.setObjectName("pb_runfits")
        self.gridLayout_4.addWidget(self.pb_runfits, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 4, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_4.addWidget(self.pushButton_5, 4, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.horizontalLayout.addWidget(self.widget_2)

        self.retranslateUi(FitManagerWidget)
        QtCore.QMetaObject.connectSlotsByName(FitManagerWidget)

    def retranslateUi(self, FitManagerWidget):
        _translate = QtCore.QCoreApplication.translate
        FitManagerWidget.setWindowTitle(_translate("FitManagerWidget", "Form"))
        self.textBrowser.setHtml(_translate("FitManagerWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.info_groupBox.setTitle(_translate("FitManagerWidget", "Info"))
        self.infotext.setHtml(_translate("FitManagerWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\';\">Data pattern set: False; Library set: False</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\';\">Cost function: chi-square; Get errors: True</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\';\">Number of sites: 1; Sub-pixels: 1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Miniminazion profile: default</p></body></html>"))
        self.pb_fitconfig.setText(_translate("FitManagerWidget", "Edit fit config"))
        self.groupBox_3.setTitle(_translate("FitManagerWidget", "Sites scan range"))
        self.lineEdit.setText(_translate("FitManagerWidget", "1, 2, 3, 5-10"))
        self.label.setText(_translate("FitManagerWidget", "Ex."))
        self.lb_site1_name.setText(_translate("FitManagerWidget", "Site #1"))
        self.le_site1.setText(_translate("FitManagerWidget", "1"))
        self.groupBox.setTitle(_translate("FitManagerWidget", "Parameters"))
        self.lb_dx_name.setText(_translate("FitManagerWidget", "dx"))
        self.pb_sigma.setText(_translate("FitManagerWidget", "Edit"))
        self.pb_dy.setText(_translate("FitManagerWidget", "Edit"))
        self.lb_dy_name.setText(_translate("FitManagerWidget", "dy"))
        self.pb_dx.setText(_translate("FitManagerWidget", "Edit"))
        self.pb_reset.setText(_translate("FitManagerWidget", "Reset"))
        self.lb_sigma.setText(_translate("FitManagerWidget", "0"))
        self.lb_phi_name.setText(_translate("FitManagerWidget", "phi"))
        self.lb_dx.setText(_translate("FitManagerWidget", "0.11; [-3,+3]; 0.01; True"))
        self.lb_total_cts.setText(_translate("FitManagerWidget", "0"))
        self.lb_phi.setText(_translate("FitManagerWidget", "0"))
        self.lb_sigma_name.setText(_translate("FitManagerWidget", "sigma"))
        self.pb_phi.setText(_translate("FitManagerWidget", "Edit"))
        self.pb_f1.setText(_translate("FitManagerWidget", "Edit"))
        self.lb_dy.setText(_translate("FitManagerWidget", "0"))
        self.lb_f1_name.setText(_translate("FitManagerWidget", "fraction #1"))
        self.lb_total_cts_name.setText(_translate("FitManagerWidget", "total cts"))
        self.pb_total_cts.setText(_translate("FitManagerWidget", "Edit"))
        self.lb_f1.setText(_translate("FitManagerWidget", "0"))
        self.groupBox_4.setTitle(_translate("FitManagerWidget", "Control"))
        self.pushButton_4.setText(_translate("FitManagerWidget", "Open last fit pattern"))
        self.pushButton_3.setText(_translate("FitManagerWidget", "Open best fit pattern"))
        self.pb_abortfits.setText(_translate("FitManagerWidget", "Abort fits"))
        self.pushButton_14.setText(_translate("FitManagerWidget", "View results table"))
        self.pb_runfits.setText(_translate("FitManagerWidget", "Run fits"))
        self.pushButton_2.setText(_translate("FitManagerWidget", "Save results table"))
        self.pushButton.setText(_translate("FitManagerWidget", "Fill DP w/ best fit"))
        self.pushButton_5.setText(_translate("FitManagerWidget", "Fill DP w/ last fit"))

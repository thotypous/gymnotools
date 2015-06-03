# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'discriminate_interface.ui'
#
# Created: Wed Jun  3 18:15:09 2015
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_discriminateWindow(object):
    def setupUi(self, discriminateWindow):
        discriminateWindow.setObjectName(_fromUtf8("discriminateWindow"))
        discriminateWindow.setWindowModality(QtCore.Qt.WindowModal)
        discriminateWindow.resize(1117, 896)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(discriminateWindow.sizePolicy().hasHeightForWidth())
        discriminateWindow.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(discriminateWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(discriminateWindow)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1099, 878))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.line_2 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 3, 1, 3, 1)
        self.step2Layout = QtGui.QVBoxLayout()
        self.step2Layout.setObjectName(_fromUtf8("step2Layout"))
        self.step2TitleLabel = ClickQLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.step2TitleLabel.setFont(font)
        self.step2TitleLabel.setObjectName(_fromUtf8("step2TitleLabel"))
        self.step2Layout.addWidget(self.step2TitleLabel)
        self.step2ParametersLayout = QtGui.QGridLayout()
        self.step2ParametersLayout.setObjectName(_fromUtf8("step2ParametersLayout"))
        self.saveSinglefishLineEdit = ClickQLineEdit(self.scrollAreaWidgetContents)
        self.saveSinglefishLineEdit.setObjectName(_fromUtf8("saveSinglefishLineEdit"))
        self.step2ParametersLayout.addWidget(self.saveSinglefishLineEdit, 8, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.step2ParametersLayout.addItem(spacerItem, 7, 0, 1, 3)
        self.loadSpikesLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.loadSpikesLabel.setObjectName(_fromUtf8("loadSpikesLabel"))
        self.step2ParametersLayout.addWidget(self.loadSpikesLabel, 0, 0, 1, 1)
        self.verifySpikesBut = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.verifySpikesBut.setObjectName(_fromUtf8("verifySpikesBut"))
        self.step2ParametersLayout.addWidget(self.verifySpikesBut, 1, 0, 1, 3)
        self.saveSinglefishLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.saveSinglefishLabel.setObjectName(_fromUtf8("saveSinglefishLabel"))
        self.step2ParametersLayout.addWidget(self.saveSinglefishLabel, 8, 0, 1, 1)
        self.loadSVMModelLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.loadSVMModelLabel.setObjectName(_fromUtf8("loadSVMModelLabel"))
        self.step2ParametersLayout.addWidget(self.loadSVMModelLabel, 6, 0, 1, 1)
        self.saveProbLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.saveProbLabel.setObjectName(_fromUtf8("saveProbLabel"))
        self.step2ParametersLayout.addWidget(self.saveProbLabel, 9, 0, 1, 1)
        self.loadRescaleLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.loadRescaleLabel.setObjectName(_fromUtf8("loadRescaleLabel"))
        self.step2ParametersLayout.addWidget(self.loadRescaleLabel, 5, 0, 1, 1)
        self.loadFilterLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.loadFilterLabel.setObjectName(_fromUtf8("loadFilterLabel"))
        self.step2ParametersLayout.addWidget(self.loadFilterLabel, 4, 0, 1, 1)
        self.loadWinlenLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.loadWinlenLabel.setObjectName(_fromUtf8("loadWinlenLabel"))
        self.step2ParametersLayout.addWidget(self.loadWinlenLabel, 3, 0, 1, 1)
        self.loadWinlen1LineEdit = ClickQLineEdit(self.scrollAreaWidgetContents)
        self.loadWinlen1LineEdit.setObjectName(_fromUtf8("loadWinlen1LineEdit"))
        self.step2ParametersLayout.addWidget(self.loadWinlen1LineEdit, 3, 1, 1, 1)
        self.loadWinlen2LineEdit = ClickQLineEdit(self.scrollAreaWidgetContents)
        self.loadWinlen2LineEdit.setObjectName(_fromUtf8("loadWinlen2LineEdit"))
        self.step2ParametersLayout.addWidget(self.loadWinlen2LineEdit, 3, 2, 1, 1)
        self.loadFilterLineEdit = ClickQLineEdit(self.scrollAreaWidgetContents)
        self.loadFilterLineEdit.setObjectName(_fromUtf8("loadFilterLineEdit"))
        self.step2ParametersLayout.addWidget(self.loadFilterLineEdit, 4, 1, 1, 2)
        self.loadRescaleLineEdit = ClickQLineEdit(self.scrollAreaWidgetContents)
        self.loadRescaleLineEdit.setObjectName(_fromUtf8("loadRescaleLineEdit"))
        self.step2ParametersLayout.addWidget(self.loadRescaleLineEdit, 5, 1, 1, 2)
        self.loadSVMModelLineEdit = ClickQLineEdit(self.scrollAreaWidgetContents)
        self.loadSVMModelLineEdit.setText(_fromUtf8(""))
        self.loadSVMModelLineEdit.setObjectName(_fromUtf8("loadSVMModelLineEdit"))
        self.step2ParametersLayout.addWidget(self.loadSVMModelLineEdit, 6, 1, 1, 2)
        self.saveProbLineEdit = ClickQLineEdit(self.scrollAreaWidgetContents)
        self.saveProbLineEdit.setObjectName(_fromUtf8("saveProbLineEdit"))
        self.step2ParametersLayout.addWidget(self.saveProbLineEdit, 9, 1, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.step2ParametersLayout.addItem(spacerItem1, 2, 0, 1, 3)
        self.applySVMBut = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.applySVMBut.setObjectName(_fromUtf8("applySVMBut"))
        self.step2ParametersLayout.addWidget(self.applySVMBut, 12, 0, 1, 3)
        self.loadSpikesLineEdit = ClickQLineEdit(self.scrollAreaWidgetContents)
        self.loadSpikesLineEdit.setObjectName(_fromUtf8("loadSpikesLineEdit"))
        self.step2ParametersLayout.addWidget(self.loadSpikesLineEdit, 0, 1, 1, 2)
        self.minWinLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.minWinLabel.setObjectName(_fromUtf8("minWinLabel"))
        self.step2ParametersLayout.addWidget(self.minWinLabel, 10, 0, 1, 1)
        self.minWinLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.minWinLineEdit.setObjectName(_fromUtf8("minWinLineEdit"))
        self.step2ParametersLayout.addWidget(self.minWinLineEdit, 10, 1, 1, 2)
        self.onlyAboveLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.onlyAboveLabel.setObjectName(_fromUtf8("onlyAboveLabel"))
        self.step2ParametersLayout.addWidget(self.onlyAboveLabel, 11, 0, 1, 1)
        self.onlyAboveLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.onlyAboveLineEdit.setObjectName(_fromUtf8("onlyAboveLineEdit"))
        self.step2ParametersLayout.addWidget(self.onlyAboveLineEdit, 11, 1, 1, 2)
        self.step2Layout.addLayout(self.step2ParametersLayout)
        self.gridLayout_2.addLayout(self.step2Layout, 3, 2, 1, 1)
        self.step1Layout = QtGui.QVBoxLayout()
        self.step1Layout.setObjectName(_fromUtf8("step1Layout"))
        self.step1TitleLabel = ClickQLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.step1TitleLabel.setFont(font)
        self.step1TitleLabel.setObjectName(_fromUtf8("step1TitleLabel"))
        self.step1Layout.addWidget(self.step1TitleLabel)
        self.step1ParametersLayout = QtGui.QGridLayout()
        self.step1ParametersLayout.setObjectName(_fromUtf8("step1ParametersLayout"))
        self.cutoffLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.cutoffLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cutoffLabel.setObjectName(_fromUtf8("cutoffLabel"))
        self.step1ParametersLayout.addWidget(self.cutoffLabel, 3, 0, 1, 1)
        self.tapsLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.tapsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tapsLabel.setObjectName(_fromUtf8("tapsLabel"))
        self.step1ParametersLayout.addWidget(self.tapsLabel, 2, 0, 1, 1)
        self.thresholdLevelLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.thresholdLevelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.thresholdLevelLabel.setObjectName(_fromUtf8("thresholdLevelLabel"))
        self.step1ParametersLayout.addWidget(self.thresholdLevelLabel, 6, 0, 1, 1)
        self.thresholdAssistBut = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.thresholdAssistBut.setObjectName(_fromUtf8("thresholdAssistBut"))
        self.step1ParametersLayout.addWidget(self.thresholdAssistBut, 5, 1, 1, 1)
        self.cutoffLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.cutoffLineEdit.setText(_fromUtf8(""))
        self.cutoffLineEdit.setObjectName(_fromUtf8("cutoffLineEdit"))
        self.step1ParametersLayout.addWidget(self.cutoffLineEdit, 3, 1, 1, 1)
        self.tapsLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.tapsLineEdit.setText(_fromUtf8(""))
        self.tapsLineEdit.setObjectName(_fromUtf8("tapsLineEdit"))
        self.step1ParametersLayout.addWidget(self.tapsLineEdit, 2, 1, 1, 1)
        self.thresholdLevelLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.thresholdLevelLineEdit.setObjectName(_fromUtf8("thresholdLevelLineEdit"))
        self.step1ParametersLayout.addWidget(self.thresholdLevelLineEdit, 6, 1, 1, 1)
        self.thresholdLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.thresholdLabel.setFont(font)
        self.thresholdLabel.setObjectName(_fromUtf8("thresholdLabel"))
        self.step1ParametersLayout.addWidget(self.thresholdLabel, 4, 0, 1, 1)
        self.filterLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.filterLabel.setFont(font)
        self.filterLabel.setObjectName(_fromUtf8("filterLabel"))
        self.step1ParametersLayout.addWidget(self.filterLabel, 0, 0, 1, 1)
        self.filterAssistBut = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.filterAssistBut.setObjectName(_fromUtf8("filterAssistBut"))
        self.step1ParametersLayout.addWidget(self.filterAssistBut, 1, 1, 1, 1)
        self.saveSpikesLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.saveSpikesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.saveSpikesLabel.setObjectName(_fromUtf8("saveSpikesLabel"))
        self.step1ParametersLayout.addWidget(self.saveSpikesLabel, 7, 0, 1, 1)
        self.saveSpikesLineEdit = ClickQLineEdit(self.scrollAreaWidgetContents)
        self.saveSpikesLineEdit.setObjectName(_fromUtf8("saveSpikesLineEdit"))
        self.step1ParametersLayout.addWidget(self.saveSpikesLineEdit, 7, 1, 1, 1)
        self.detectSpikesBut = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.detectSpikesBut.setObjectName(_fromUtf8("detectSpikesBut"))
        self.step1ParametersLayout.addWidget(self.detectSpikesBut, 8, 0, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.step1ParametersLayout.addItem(spacerItem2, 9, 0, 1, 2)
        self.step1Layout.addLayout(self.step1ParametersLayout)
        self.gridLayout_2.addLayout(self.step1Layout, 3, 0, 3, 1)
        self.step3Layout = QtGui.QVBoxLayout()
        self.step3Layout.setObjectName(_fromUtf8("step3Layout"))
        self.step3TitleLabel = ClickQLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.step3TitleLabel.setFont(font)
        self.step3TitleLabel.setObjectName(_fromUtf8("step3TitleLabel"))
        self.step3Layout.addWidget(self.step3TitleLabel)
        self.step3ParametersLayout = QtGui.QGridLayout()
        self.step3ParametersLayout.setObjectName(_fromUtf8("step3ParametersLayout"))
        self.loadProbLineEdit = ClickQLineEdit(self.scrollAreaWidgetContents)
        self.loadProbLineEdit.setObjectName(_fromUtf8("loadProbLineEdit"))
        self.step3ParametersLayout.addWidget(self.loadProbLineEdit, 1, 1, 1, 1)
        self.saveDBLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.saveDBLabel.setObjectName(_fromUtf8("saveDBLabel"))
        self.step3ParametersLayout.addWidget(self.saveDBLabel, 3, 0, 1, 1)
        self.saveDBLineEdit = ClickQLineEdit(self.scrollAreaWidgetContents)
        self.saveDBLineEdit.setObjectName(_fromUtf8("saveDBLineEdit"))
        self.step3ParametersLayout.addWidget(self.saveDBLineEdit, 3, 1, 1, 1)
        self.loadProbLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.loadProbLabel.setObjectName(_fromUtf8("loadProbLabel"))
        self.step3ParametersLayout.addWidget(self.loadProbLabel, 1, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.step3ParametersLayout.addItem(spacerItem3, 2, 0, 1, 2)
        self.loadSinglefishLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.loadSinglefishLabel.setObjectName(_fromUtf8("loadSinglefishLabel"))
        self.step3ParametersLayout.addWidget(self.loadSinglefishLabel, 0, 0, 1, 1)
        self.loadSinglefishLineEdit = ClickQLineEdit(self.scrollAreaWidgetContents)
        self.loadSinglefishLineEdit.setObjectName(_fromUtf8("loadSinglefishLineEdit"))
        self.step3ParametersLayout.addWidget(self.loadSinglefishLineEdit, 0, 1, 1, 1)
        self.applyContinuityBut = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.applyContinuityBut.setObjectName(_fromUtf8("applyContinuityBut"))
        self.step3ParametersLayout.addWidget(self.applyContinuityBut, 4, 0, 1, 2)
        self.step3Layout.addLayout(self.step3ParametersLayout)
        self.gridLayout_2.addLayout(self.step3Layout, 7, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_2.addWidget(self.line_3, 2, 0, 1, 1)
        self.line_6 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.gridLayout_2.addWidget(self.line_6, 4, 2, 1, 1)
        self.logoPixMap = KPixmapRegionSelectorWidget(self.scrollAreaWidgetContents)
        self.logoPixMap.setPixmap(QtGui.QPixmap(_fromUtf8("../../../Dropbox/LogoClaro_comLogo_w580.png")))
        self.logoPixMap.setObjectName(_fromUtf8("logoPixMap"))
        self.gridLayout_2.addWidget(self.logoPixMap, 5, 2, 1, 1)
        self.line = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 6, 0, 1, 1)
        self.line_5 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout_2.addWidget(self.line_5, 6, 2, 1, 1)
        self.line_4 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_2.addWidget(self.line_4, 7, 1, 1, 1)
        self.step4Layout = QtGui.QVBoxLayout()
        self.step4Layout.setObjectName(_fromUtf8("step4Layout"))
        self.step4TitleLabel = ClickQLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.step4TitleLabel.setFont(font)
        self.step4TitleLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.step4TitleLabel.setObjectName(_fromUtf8("step4TitleLabel"))
        self.step4Layout.addWidget(self.step4TitleLabel)
        self.step4ParametersLayout = QtGui.QGridLayout()
        self.step4ParametersLayout.setObjectName(_fromUtf8("step4ParametersLayout"))
        self.saveTimestampsLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.saveTimestampsLabel.setObjectName(_fromUtf8("saveTimestampsLabel"))
        self.step4ParametersLayout.addWidget(self.saveTimestampsLabel, 1, 0, 1, 1)
        self.loadDBLineEdit = ClickQLineEdit(self.scrollAreaWidgetContents)
        self.loadDBLineEdit.setObjectName(_fromUtf8("loadDBLineEdit"))
        self.step4ParametersLayout.addWidget(self.loadDBLineEdit, 0, 1, 1, 1)
        self.loadTimestampsLineEdit = ClickQLineEdit(self.scrollAreaWidgetContents)
        self.loadTimestampsLineEdit.setObjectName(_fromUtf8("loadTimestampsLineEdit"))
        self.step4ParametersLayout.addWidget(self.loadTimestampsLineEdit, 4, 1, 1, 1)
        self.saveTimestampsLineEdit = ClickQLineEdit(self.scrollAreaWidgetContents)
        self.saveTimestampsLineEdit.setObjectName(_fromUtf8("saveTimestampsLineEdit"))
        self.step4ParametersLayout.addWidget(self.saveTimestampsLineEdit, 1, 1, 1, 1)
        self.loadDBLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.loadDBLabel.setObjectName(_fromUtf8("loadDBLabel"))
        self.step4ParametersLayout.addWidget(self.loadDBLabel, 0, 0, 1, 1)
        self.loadTimestampsLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.loadTimestampsLabel.setObjectName(_fromUtf8("loadTimestampsLabel"))
        self.step4ParametersLayout.addWidget(self.loadTimestampsLabel, 4, 0, 1, 1)
        self.verifyCorrectTimestampsBut = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.verifyCorrectTimestampsBut.setObjectName(_fromUtf8("verifyCorrectTimestampsBut"))
        self.step4ParametersLayout.addWidget(self.verifyCorrectTimestampsBut, 5, 0, 1, 2)
        self.detectTimestampsBut = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.detectTimestampsBut.setObjectName(_fromUtf8("detectTimestampsBut"))
        self.step4ParametersLayout.addWidget(self.detectTimestampsBut, 2, 0, 1, 2)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.step4ParametersLayout.addItem(spacerItem4, 3, 0, 1, 2)
        self.step4Layout.addLayout(self.step4ParametersLayout)
        self.gridLayout_2.addLayout(self.step4Layout, 7, 2, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.lowSaturationLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lowSaturationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lowSaturationLabel.setObjectName(_fromUtf8("lowSaturationLabel"))
        self.gridLayout_6.addWidget(self.lowSaturationLabel, 1, 1, 1, 1)
        self.saturationLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(False)
        font.setWeight(50)
        self.saturationLabel.setFont(font)
        self.saturationLabel.setObjectName(_fromUtf8("saturationLabel"))
        self.gridLayout_6.addWidget(self.saturationLabel, 2, 0, 1, 1)
        self.lowSaturationLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lowSaturationLineEdit.setObjectName(_fromUtf8("lowSaturationLineEdit"))
        self.gridLayout_6.addWidget(self.lowSaturationLineEdit, 2, 1, 1, 1)
        self.highSaturationLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.highSaturationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.highSaturationLabel.setObjectName(_fromUtf8("highSaturationLabel"))
        self.gridLayout_6.addWidget(self.highSaturationLabel, 1, 2, 1, 1)
        self.highSaturationLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.highSaturationLineEdit.setObjectName(_fromUtf8("highSaturationLineEdit"))
        self.gridLayout_6.addWidget(self.highSaturationLineEdit, 2, 2, 1, 1)
        self.loadTimeseriesLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.loadTimeseriesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loadTimeseriesLabel.setObjectName(_fromUtf8("loadTimeseriesLabel"))
        self.gridLayout_6.addWidget(self.loadTimeseriesLabel, 0, 0, 1, 1)
        self.loadTimeseriesLineEdit = ClickQLineEdit(self.scrollAreaWidgetContents)
        self.loadTimeseriesLineEdit.setObjectName(_fromUtf8("loadTimeseriesLineEdit"))
        self.gridLayout_6.addWidget(self.loadTimeseriesLineEdit, 0, 1, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout_6, 1, 0, 1, 3)
        self.saveLoadParametersLayout = QtGui.QHBoxLayout()
        self.saveLoadParametersLayout.setObjectName(_fromUtf8("saveLoadParametersLayout"))
        self.saveParametersBut = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.saveParametersBut.setObjectName(_fromUtf8("saveParametersBut"))
        self.saveLoadParametersLayout.addWidget(self.saveParametersBut)
        self.loadParametersBut = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.loadParametersBut.setObjectName(_fromUtf8("loadParametersBut"))
        self.saveLoadParametersLayout.addWidget(self.loadParametersBut)
        self.gridLayout_2.addLayout(self.saveLoadParametersLayout, 0, 0, 1, 3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(discriminateWindow)
        QtCore.QMetaObject.connectSlotsByName(discriminateWindow)
        discriminateWindow.setTabOrder(self.scrollArea, self.saveParametersBut)
        discriminateWindow.setTabOrder(self.saveParametersBut, self.loadParametersBut)
        discriminateWindow.setTabOrder(self.loadParametersBut, self.loadTimeseriesLineEdit)
        discriminateWindow.setTabOrder(self.loadTimeseriesLineEdit, self.lowSaturationLineEdit)
        discriminateWindow.setTabOrder(self.lowSaturationLineEdit, self.highSaturationLineEdit)
        discriminateWindow.setTabOrder(self.highSaturationLineEdit, self.filterAssistBut)
        discriminateWindow.setTabOrder(self.filterAssistBut, self.tapsLineEdit)
        discriminateWindow.setTabOrder(self.tapsLineEdit, self.cutoffLineEdit)
        discriminateWindow.setTabOrder(self.cutoffLineEdit, self.thresholdAssistBut)
        discriminateWindow.setTabOrder(self.thresholdAssistBut, self.thresholdLevelLineEdit)
        discriminateWindow.setTabOrder(self.thresholdLevelLineEdit, self.saveSpikesLineEdit)
        discriminateWindow.setTabOrder(self.saveSpikesLineEdit, self.detectSpikesBut)
        discriminateWindow.setTabOrder(self.detectSpikesBut, self.loadSpikesLineEdit)
        discriminateWindow.setTabOrder(self.loadSpikesLineEdit, self.verifySpikesBut)
        discriminateWindow.setTabOrder(self.verifySpikesBut, self.loadWinlen1LineEdit)
        discriminateWindow.setTabOrder(self.loadWinlen1LineEdit, self.loadWinlen2LineEdit)
        discriminateWindow.setTabOrder(self.loadWinlen2LineEdit, self.loadFilterLineEdit)
        discriminateWindow.setTabOrder(self.loadFilterLineEdit, self.loadRescaleLineEdit)
        discriminateWindow.setTabOrder(self.loadRescaleLineEdit, self.loadSVMModelLineEdit)
        discriminateWindow.setTabOrder(self.loadSVMModelLineEdit, self.saveSinglefishLineEdit)
        discriminateWindow.setTabOrder(self.saveSinglefishLineEdit, self.saveProbLineEdit)
        discriminateWindow.setTabOrder(self.saveProbLineEdit, self.minWinLineEdit)
        discriminateWindow.setTabOrder(self.minWinLineEdit, self.applySVMBut)
        discriminateWindow.setTabOrder(self.applySVMBut, self.loadSinglefishLineEdit)
        discriminateWindow.setTabOrder(self.loadSinglefishLineEdit, self.loadProbLineEdit)
        discriminateWindow.setTabOrder(self.loadProbLineEdit, self.saveDBLineEdit)
        discriminateWindow.setTabOrder(self.saveDBLineEdit, self.applyContinuityBut)
        discriminateWindow.setTabOrder(self.applyContinuityBut, self.loadDBLineEdit)
        discriminateWindow.setTabOrder(self.loadDBLineEdit, self.saveTimestampsLineEdit)
        discriminateWindow.setTabOrder(self.saveTimestampsLineEdit, self.detectTimestampsBut)
        discriminateWindow.setTabOrder(self.detectTimestampsBut, self.loadTimestampsLineEdit)
        discriminateWindow.setTabOrder(self.loadTimestampsLineEdit, self.verifyCorrectTimestampsBut)

    def retranslateUi(self, discriminateWindow):
        discriminateWindow.setWindowTitle(_translate("discriminateWindow", "gymnotools - Discriminate", None))
        self.step2TitleLabel.setText(_translate("discriminateWindow", "2. Apply SVM >", None))
        self.loadSpikesLabel.setText(_translate("discriminateWindow", "Load spikes file:", None))
        self.verifySpikesBut.setText(_translate("discriminateWindow", "Verify detection", None))
        self.saveSinglefishLabel.setText(_translate("discriminateWindow", "Save SVM timestamps (singlefish) as:", None))
        self.loadSVMModelLabel.setText(_translate("discriminateWindow", "Load training SVM model:", None))
        self.saveProbLabel.setText(_translate("discriminateWindow", "Save probabilities as:", None))
        self.loadRescaleLabel.setText(_translate("discriminateWindow", "Load training rescale file:", None))
        self.loadFilterLabel.setText(_translate("discriminateWindow", "Load training filter file:", None))
        self.loadWinlenLabel.setText(_translate("discriminateWindow", "Load training window lengths files:", None))
        self.applySVMBut.setText(_translate("discriminateWindow", "Apply SVM", None))
        self.minWinLabel.setText(_translate("discriminateWindow", "Minimum windows needed to analyze with SVM:", None))
        self.minWinLineEdit.setText(_translate("discriminateWindow", "2", None))
        self.onlyAboveLabel.setText(_translate("discriminateWindow", "Only apply on spikes above (V) (same used for training):", None))
        self.step1TitleLabel.setText(_translate("discriminateWindow", "1. Select parameters and detect spikes >", None))
        self.cutoffLabel.setText(_translate("discriminateWindow", "Cutoff frequency (cycles/sample):", None))
        self.tapsLabel.setText(_translate("discriminateWindow", "Number of taps:", None))
        self.thresholdLevelLabel.setText(_translate("discriminateWindow", "Threshold level (V):", None))
        self.thresholdAssistBut.setText(_translate("discriminateWindow", "Threshold Assistant", None))
        self.thresholdLabel.setText(_translate("discriminateWindow", "Threshold:", None))
        self.filterLabel.setText(_translate("discriminateWindow", "Low-pass filter parameters:", None))
        self.filterAssistBut.setText(_translate("discriminateWindow", "Filter Assistant", None))
        self.saveSpikesLabel.setText(_translate("discriminateWindow", "Save detected spikes as: ", None))
        self.detectSpikesBut.setText(_translate("discriminateWindow", "Detect Spikes", None))
        self.step3TitleLabel.setText(_translate("discriminateWindow", "3. Apply continuity criteria >", None))
        self.saveDBLabel.setText(_translate("discriminateWindow", "Save DataBase as:", None))
        self.loadProbLabel.setText(_translate("discriminateWindow", "Load probabilities:", None))
        self.loadSinglefishLabel.setText(_translate("discriminateWindow", "Load SVM timestamps (singlefish):", None))
        self.applyContinuityBut.setText(_translate("discriminateWindow", "Apply continuity", None))
        self.step4TitleLabel.setText(_translate("discriminateWindow", "4. Detect zero-crossing timestamps >", None))
        self.saveTimestampsLabel.setText(_translate("discriminateWindow", "Save timetamps as:", None))
        self.loadDBLabel.setText(_translate("discriminateWindow", "Load DataBase:", None))
        self.loadTimestampsLabel.setText(_translate("discriminateWindow", "Load timestamps:", None))
        self.verifyCorrectTimestampsBut.setText(_translate("discriminateWindow", "Verify and Manually correct timestamps (Timeseries file needed!)", None))
        self.detectTimestampsBut.setText(_translate("discriminateWindow", "Detect timestamps", None))
        self.lowSaturationLabel.setText(_translate("discriminateWindow", "LOW saturation level (V):", None))
        self.saturationLabel.setText(_translate("discriminateWindow", "Saturation level:", None))
        self.highSaturationLabel.setText(_translate("discriminateWindow", "HIGH saturation level (V):", None))
        self.loadTimeseriesLabel.setText(_translate("discriminateWindow", "Load timeseries data:", None))
        self.saveParametersBut.setText(_translate("discriminateWindow", "Save parameters", None))
        self.loadParametersBut.setText(_translate("discriminateWindow", "Load parameters", None))

from PyKDE4.kdeui import KPixmapRegionSelectorWidget
from clickAux import ClickQLineEdit, ClickQLabel

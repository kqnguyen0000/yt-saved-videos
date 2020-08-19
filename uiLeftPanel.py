# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/leftPanel.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LeftPanel(object):
    def setupUi(self, LeftPanel):
        LeftPanel.setObjectName("LeftPanel")
        LeftPanel.resize(300, 720)
        self.leftPanelVertLayout = QtWidgets.QVBoxLayout(LeftPanel)
        self.leftPanelVertLayout.setContentsMargins(0, 0, 0, 0)
        self.leftPanelVertLayout.setSpacing(6)
        self.leftPanelVertLayout.setObjectName("leftPanelVertLayout")
        self.leftTabWidget = QtWidgets.QTabWidget(LeftPanel)
        self.leftTabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.leftTabWidget.setObjectName("leftTabWidget")
        self.filterTab = QtWidgets.QWidget()
        self.filterTab.setObjectName("filterTab")
        self.filterTabVertLayout = QtWidgets.QVBoxLayout(self.filterTab)
        self.filterTabVertLayout.setSpacing(6)
        self.filterTabVertLayout.setObjectName("filterTabVertLayout")
        self.filterListAlpha = QtWidgets.QListView(self.filterTab)
        self.filterListAlpha.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.filterListAlpha.setObjectName("filterListAlpha")
        self.filterTabVertLayout.addWidget(self.filterListAlpha)
        self.filterComboFrame = QtWidgets.QFrame(self.filterTab)
        self.filterComboFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.filterComboFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.filterComboFrame.setObjectName("filterComboFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.filterComboFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filterTypeDropDown = QtWidgets.QComboBox(self.filterComboFrame)
        self.filterTypeDropDown.setObjectName("filterTypeDropDown")
        self.filterTypeDropDown.addItem("")
        self.filterTypeDropDown.addItem("")
        self.filterTypeDropDown.addItem("")
        self.filterTypeDropDown.addItem("")
        self.horizontalLayout.addWidget(self.filterTypeDropDown)
        self.filterSortDropDown = QtWidgets.QComboBox(self.filterComboFrame)
        self.filterSortDropDown.setObjectName("filterSortDropDown")
        self.filterSortDropDown.addItem("")
        self.filterSortDropDown.addItem("")
        self.horizontalLayout.addWidget(self.filterSortDropDown)
        self.filterSortDirDropDown = QtWidgets.QComboBox(self.filterComboFrame)
        self.filterSortDirDropDown.setObjectName("filterSortDirDropDown")
        self.filterSortDirDropDown.addItem("")
        self.filterSortDirDropDown.addItem("")
        self.horizontalLayout.addWidget(self.filterSortDirDropDown)
        self.filterTabVertLayout.addWidget(self.filterComboFrame)
        self.filterSearchBar = QtWidgets.QLineEdit(self.filterTab)
        self.filterSearchBar.setClearButtonEnabled(True)
        self.filterSearchBar.setObjectName("filterSearchBar")
        self.filterTabVertLayout.addWidget(self.filterSearchBar)
        self.filterListBeta = QtWidgets.QListView(self.filterTab)
        self.filterListBeta.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.filterListBeta.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.filterListBeta.setObjectName("filterListBeta")
        self.filterTabVertLayout.addWidget(self.filterListBeta)
        self.leftTabWidget.addTab(self.filterTab, "")
        self.tagTab = QtWidgets.QWidget()
        self.tagTab.setObjectName("tagTab")
        self.tagTabVertLayout = QtWidgets.QVBoxLayout(self.tagTab)
        self.tagTabVertLayout.setObjectName("tagTabVertLayout")
        self.tagComboFrame = QtWidgets.QFrame(self.tagTab)
        self.tagComboFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tagComboFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tagComboFrame.setObjectName("tagComboFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tagComboFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tagTypeDropDown = QtWidgets.QComboBox(self.tagComboFrame)
        self.tagTypeDropDown.setObjectName("tagTypeDropDown")
        self.tagTypeDropDown.addItem("")
        self.tagTypeDropDown.addItem("")
        self.horizontalLayout_2.addWidget(self.tagTypeDropDown)
        self.tagSortDropDown = QtWidgets.QComboBox(self.tagComboFrame)
        self.tagSortDropDown.setObjectName("tagSortDropDown")
        self.tagSortDropDown.addItem("")
        self.tagSortDropDown.addItem("")
        self.horizontalLayout_2.addWidget(self.tagSortDropDown)
        self.tagSortDirDropDown = QtWidgets.QComboBox(self.tagComboFrame)
        self.tagSortDirDropDown.setObjectName("tagSortDirDropDown")
        self.tagSortDirDropDown.addItem("")
        self.tagSortDirDropDown.addItem("")
        self.horizontalLayout_2.addWidget(self.tagSortDirDropDown)
        self.tagTabVertLayout.addWidget(self.tagComboFrame)
        self.tagListAlpha = QtWidgets.QListView(self.tagTab)
        self.tagListAlpha.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tagListAlpha.setObjectName("tagListAlpha")
        self.tagTabVertLayout.addWidget(self.tagListAlpha)
        self.tagSearchBar = QtWidgets.QLineEdit(self.tagTab)
        self.tagSearchBar.setText("")
        self.tagSearchBar.setClearButtonEnabled(True)
        self.tagSearchBar.setObjectName("tagSearchBar")
        self.tagTabVertLayout.addWidget(self.tagSearchBar)
        self.tagListBeta = QtWidgets.QListView(self.tagTab)
        self.tagListBeta.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tagListBeta.setObjectName("tagListBeta")
        self.tagTabVertLayout.addWidget(self.tagListBeta)
        self.leftTabWidget.addTab(self.tagTab, "")
        self.leftPanelVertLayout.addWidget(self.leftTabWidget)

        self.retranslateUi(LeftPanel)
        self.leftTabWidget.setCurrentIndex(0)
        self.filterTypeDropDown.setCurrentIndex(2)
        self.filterSortDropDown.setCurrentIndex(1)
        self.filterSortDirDropDown.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(LeftPanel)

    def retranslateUi(self, LeftPanel):
        _translate = QtCore.QCoreApplication.translate
        LeftPanel.setWindowTitle(_translate("LeftPanel", "Form"))
        self.filterListAlpha.setToolTip(_translate("LeftPanel", "<html><head/><body><p>Double click to deactivate filters</p></body></html>"))
        self.filterTypeDropDown.setToolTip(_translate("LeftPanel", "<html><head/><body><p>Select filter category</p></body></html>"))
        self.filterTypeDropDown.setItemText(0, _translate("LeftPanel", "playlists"))
        self.filterTypeDropDown.setItemText(1, _translate("LeftPanel", "channels"))
        self.filterTypeDropDown.setItemText(2, _translate("LeftPanel", "tags"))
        self.filterTypeDropDown.setItemText(3, _translate("LeftPanel", "yt tags"))
        self.filterSortDropDown.setItemText(0, _translate("LeftPanel", "by name"))
        self.filterSortDropDown.setItemText(1, _translate("LeftPanel", "by video count"))
        self.filterSortDirDropDown.setItemText(0, _translate("LeftPanel", "ascending"))
        self.filterSortDirDropDown.setItemText(1, _translate("LeftPanel", "descending"))
        self.filterSearchBar.setToolTip(_translate("LeftPanel", "<html><head/><body><p>Search for a specific filter</p></body></html>"))
        self.filterSearchBar.setPlaceholderText(_translate("LeftPanel", "Search filters"))
        self.filterListBeta.setToolTip(_translate("LeftPanel", "<html><head/><body><p>Double click to filter video table</p></body></html>"))
        self.leftTabWidget.setTabText(self.leftTabWidget.indexOf(self.filterTab), _translate("LeftPanel", "Filters"))
        self.tagTypeDropDown.setToolTip(_translate("LeftPanel", "<html><head/><body><p><span style=\" font-size:9pt;\">Select tag type</span></p></body></html>"))
        self.tagTypeDropDown.setItemText(0, _translate("LeftPanel", "tags"))
        self.tagTypeDropDown.setItemText(1, _translate("LeftPanel", "yt tags"))
        self.tagSortDropDown.setItemText(0, _translate("LeftPanel", "by name"))
        self.tagSortDropDown.setItemText(1, _translate("LeftPanel", "by video count"))
        self.tagSortDirDropDown.setItemText(0, _translate("LeftPanel", "ascending"))
        self.tagSortDirDropDown.setItemText(1, _translate("LeftPanel", "descending"))
        self.tagListAlpha.setToolTip(_translate("LeftPanel", "<html><head/><body><p>Double click to remove tag from selected videos</p></body></html>"))
        self.tagSearchBar.setToolTip(_translate("LeftPanel", "<html><head/><body><p><span style=\" font-size:9pt;\">Search list of tags. Press enter to apply tag in search box, even if it doesn\'t exist yet</span></p></body></html>"))
        self.tagSearchBar.setPlaceholderText(_translate("LeftPanel", "Search tags"))
        self.tagListBeta.setToolTip(_translate("LeftPanel", "<html><head/><body><p>Double click to add tag to selected videos</p></body></html>"))
        self.leftTabWidget.setTabText(self.leftTabWidget.indexOf(self.tagTab), _translate("LeftPanel", "Tags"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LeftPanel = QtWidgets.QWidget()
    ui = Ui_LeftPanel()
    ui.setupUi(LeftPanel)
    LeftPanel.show()
    sys.exit(app.exec_())
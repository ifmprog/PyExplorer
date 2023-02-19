from PySide2.QtWidgets import (
    QWidget,
    QTreeView,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QFileSystemModel,
)
from PySide2.QtGui import QStandardItemModel
from PySide2.QtCore import QDir
from os import path


class ExplorerWidget(QWidget):
    def __init__(
        self,
    ) -> None:
        super().__init__()
        self.__openDirPath: str = ""
        self.__initUI()

    def __initUI(self):
        """開くボタン"""
        self.__openButton = QPushButton("Open")
        self.__openButton.clicked.connect(self.__openRootSelector)
        """ツリービュー"""
        self.__model = QFileSystemModel()
        # self.__model.setFilter(QDir.Dirs)
        # self.__model.setFilter(QDir.NoDotAndDotDot)
        self.__treeView = QTreeView()
        self.__treeView.setModel(self.__model)
        # self.__treeView.setRootIndex(self.__model.index("C:\\"))
        """レイアウト"""
        self.__layout = QVBoxLayout()
        self.__layout.addWidget(self.__openButton)
        self.__layout.addWidget(self.__treeView)
        self.setLayout(self.__layout)

    def __openRootSelector(self):
        dirPath = QFileDialog.getExistingDirectory(self, "Select Directory")
        if not dirPath:
            return
        self.__setup(dirPath)

    def __setup(self, dirPath: str):
        dirPath = path.normpath(dirPath)
        if not path.exists(dirPath):
            return
        self.__openDirPath = dirPath
        self.__model.setRootPath(self.__openDirPath)
        self.__model.setNameFilters(["*.txt"])
        self.__model.setNameFilterDisables(False)
        index = self.__model.index(self.__openDirPath)
        self.__treeView.setRootIndex(index)


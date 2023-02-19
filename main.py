import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from explorerWidget import ExplorerWidget


def main():
    app = QApplication()
    wnd = QMainWindow()
    explorer = ExplorerWidget()
    wnd.setCentralWidget(explorer)
    wnd.show()
    result = app.exec_()
    sys.exit(result)


if __name__ == "__main__":
    main()

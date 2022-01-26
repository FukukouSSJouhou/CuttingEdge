import cv2
import sys

from PySide2.QtCore import QStringListModel, Slot, QUrl
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

from GUIConnect import GUIConnect


def main():
    app=QGuiApplication(sys.argv)
    engine=QQmlApplicationEngine()
    context=engine.rootContext()
    #context.setContextProperty("GUIKan",guikan)
    #context.setContextProperty("modeloniisan",guikan.md)
    connection=GUIConnect()
    context.setContextProperty("mainwinconnect",connection)
    engine.load(QUrl("CuttingEdge.qml"))
    if not engine.rootObjects():
        sys.exit(-1)
    app.exec_()
    # ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    main()

# PyCharm のヘルプは https://www.jetbrains.com/help/pycharm/ を参照してください

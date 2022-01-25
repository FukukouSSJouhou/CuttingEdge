import os

from PySide2 import QtCore


class GUIConnect(QtCore.QObject):
    def __init__(self,parent=None):
        super(GUIConnect,self).__init__(parent)
    @QtCore.Slot(str,str)
    def running_process(self,stroniisan,outfileoniisan):
        print(stroniisan)
        print(outfileoniisan)
        inputfiles=os.listdir(stroniisan)
        for a in inputfiles:
            print(a)
            print(os.path.join(outfileoniisan , a))
    @QtCore.Slot(str)
    def print_stdout(selfself,strtextkun):
        print(strtextkun)
    @QtCore.Slot(str ,result='QVariant')
    def fpPathconv(self,furl):
        print(furl)
        return QtCore.QDir.toNativeSeparators(QtCore.QUrl(furl).toLocalFile())
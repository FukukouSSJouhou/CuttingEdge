import os

import cv2
from PySide2 import QtCore


def cv2kun(gazouniki,out_dir,nocolor,sizeresize):
    cascade_path = './FACE/models/haarcascade_frontalface_default.xml'
    cascade = cv2.CascadeClassifier(cascade_path)
    fr = cv2.imread(gazouniki)
    gray = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
    front_face_list = cascade.detectMultiScale(gray)
    print(front_face_list)
    i=0
    if len(front_face_list) == 0:
        print("")
    else:
        for (x, y, w, h) in front_face_list:
            save_path = out_dir + str(i) + '.jpg'
            if nocolor:
                img=gray[y:y+h,x:x+w]
            else:
                img=fr[y:y+h,x:x+w]
            if sizeresize:
                img=cv2.resize(img,(48,48))
            cv2.imwrite(save_path, img)
            i+=1
class GUIConnect(QtCore.QObject):
    success_dialogsignal=QtCore.Signal(str)
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
            base,ext=os.path.splitext(a)
            if ext == ".jpg":
                cv2kun(os.path.join(stroniisan , a),os.path.join(outfileoniisan , a),True,True)
        self.success_dialogsignal.emit("")
    @QtCore.Slot(str)
    def print_stdout(selfself,strtextkun):
        print(strtextkun)
    @QtCore.Slot(str ,result='QVariant')
    def fpPathconv(self,furl):
        print(furl)
        return QtCore.QDir.toNativeSeparators(QtCore.QUrl(furl).toLocalFile())
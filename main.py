import cv2
import sys
def main():
    print("Tdn")
    if(len(sys.argv) < 3):
        print("err")
        return
    cv2kun(sys.argv[1],sys.argv[2],True,True)
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
    # ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    main()

# PyCharm のヘルプは https://www.jetbrains.com/help/pycharm/ を参照してください

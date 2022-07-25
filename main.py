import os
from pyclbr import Function
from threading import Thread
from faceLogic import method_enum
import ui.mainUI as mainUI
import sys
import imutils
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from faceLogic import FaceLogic
import cv2 as cv
CASCADE_PATH = r'F:\python\ML\face\haarcascade_frontalface_default.xml' #人脸模型路径
class Ui_logic_window(QtWidgets.QMainWindow):
    
    def __init__(self, parent = None):
        super(Ui_logic_window, self).__init__(parent)
        # 主窗口初始化
        self.m = QMainWindow()
        # 实例化窗口
        self.ui = mainUI.Ui_MainWindow()
        self.ui.setupUi(self)
         # 初始化人脸检测器
        self.face_cascade = cv.CascadeClassifier(CASCADE_PATH)
        self.faceLogic = FaceLogic()
        self.catch_path = ''
        self.setSlot()
        self.logStr = ''
    def setSlot(self):
        self.ui.init.clicked.connect(self.init_model)
        self.ui.weight.clicked.connect(self.select_model)
        self.ui.videoCap.clicked.connect(self.cap_video)
        self.ui.cameraCap.clicked.connect(lambda a: self.faceLogic.catch_method_change(method_enum.video))
        self.ui.videoTest.clicked.connect(self.video_test)
        self.ui.cameraTest.clicked.connect(lambda a: self.faceLogic.test_method_change(method_enum.camera))
        self.ui.set_face.clicked.connect(lambda a: self.set_face_name)
    def init_model(self):
        self.thread1 = model_Thread()
        self.thread1._signal.connect(self.faceLogic.init_model)
        self.thread1.start()
        # self.thread1.exec()
    def cap_video(self):
        file_path, _ = QFileDialog.getOpenFileName(self, '选择人脸视频路径', './video')
        self.catch_path = file_path
        self.catch_face(method_enum.video)
    
    def show_img(self, img):
            show = cv.resize(img, (640, 480)) # 直接将原始img上的检测结果进行显示
            self.result = cv.cvtColor(show, cv.COLOR_BGR2RGB)
            self.result = imutils.resize(self.result, width= 640)
            showImage = QtGui.QImage(self.result.data, self.result.shape[1], self.result.shape[0],
                                 QtGui.QImage.Format_RGB888)
            self.ui.show.setPixmap(QtGui.QPixmap.fromImage(showImage))
            self.ui.show.setScaledContents(True)  # 设置图像自适应界面大小
    
    def video_test(self):
        file_path, _ = QFileDialog.getOpenFileName(self, '选择测试人脸视频路径', './video')
        self.test_path = file_path
        font = cv.FONT_HERSHEY_SIMPLEX
        cap = cv.VideoCapture(file_path)
        while cap.isOpened():
            ret, img = cap.read()
            if ret is not None and img is not None:
                img = imutils.resize(img, width=600)
                gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                face = self.face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in face:
                    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0))
                    id, conf = self.faceLogic.recog.predict(gray[y: y+h, x: x+w])
                    user = ''
                    if conf < 100:
                        user = self.faceLogic.face_names[id]
                        conf = "{0}%".format(round(100-conf))
                    else:
                        user = "unknown"
                        conf = " "
                    cv.putText(img, user, (x + 5, y - 5), font, 1, (0,255, 0), 1)
                    cv.putText(img, str(conf), (x + 50, y + h + 50), font, 1, (0,255, 0), 1)
                self.show_img(img)
                cv.waitKey(1)
        cap.release()
        cv.destroyAllWindows()
    def select_model(self):
        file_path, _ = QFileDialog.getOpenFileName(self, '选择模型文件', './trainner')
        if not file_path.endswith('.yaml'):
            self.log('模型文件选择有误')
        self.faceLogic.select_model_path(file_path)
        self.log('模型路径为' + file_path)
    # 获取人脸数据，默认八百张图片，实验可到最好效果
    def catch_face(self, catch_method):
        print(self.ui.face_name.toPlainText())
        face_id = self.faceLogic.check_face(self.ui.face_name.toPlainText())
        if not face_id:
            self.log('名字已存在')
            return
        self.log('开始抓取照片')
        #sampleNum用来计数样本数目
        count = 0
        cap = cv.VideoCapture(self.catch_path if catch_method == method_enum.video else 0)
        while cap.isOpened():
            # if len(os.listdir(self.faceLogic.data_path + 'user.' + str(face_id))) >= 800:
            #     break
            ret, img = cap.read()
            if ret is not None:
                if img is None:
                    continue
                img = imutils.resize(img, width=600)
                gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                face = self.face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in face:
                    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0))
                    count += 1
                    if not os.path.exists(self.faceLogic.data_path + 'user.' + str(face_id)):
                        os.mkdir(self.faceLogic.data_path + 'user.' + str(face_id))
                    gray_face = gray[y: y + h, x: x + w]
                    cv.imwrite(self.faceLogic.data_path + 'user.' + str(face_id) + "/count_" + str(count) + ".jpg", gray_face)
                if count >= 800:
                    break   
                self.show_img(img)
                self.faceLogic.add_train_data(gray_face)
                cv.waitKey(1)
                # if key == 27:
                    # break
            else:
                break
        cap.release()
        # 添加训练数据
        # self.log('开始读取训练数据')
        # self.faceLogic.get_imgs_labels()
        # cv.destroyAllWindows()
        # 训练
        self.log('开始训练数据')
        self.faceLogic.train_model()
        self.log('训练完成')
        
    def set_face_name(self):
        face_name = self.ui.face_name.toPlainText()
        self.faceLogic.set_face_name(face_name)
    def log(self, output):
        self.logStr += str(output)
        self.ui.log.setText(self.logStr)
        
class model_Thread(QThread):
    _signal = pyqtSignal()
    def __init__(self):
        super().__init__()
    
    def run(self):
        self._signal.emit()
if __name__ == '__main__':
    app = QApplication(sys.argv)    
    MainWindow = Ui_logic_window()
    MainWindow.show()
    sys.exit(app.exec_())
from enum import Enum

from scipy.misc import face
import cv2 as cv 
import numpy as np
import imutils
import os
from PIL import Image


RECOG_PATH = r'F:\python\ML\face/trainner/face.yaml' # 人脸识别模型加载
VIDEO_PATH = 'video/hero1.mp4' # 视频人脸补获路径
DATA_PATH = r'F:\python\ML\face/data/'

class method_enum(Enum):
    camera = 0
    video = 1
class FaceLogic(object):
    def __init__(self) -> None:
        self.recog_path = RECOG_PATH
        self.catch_path = VIDEO_PATH
        # 提取方式 默认设置为视频读取
        self.catch_method: method_enum = method_enum.video
        # 设置测试方式
        self.test_method: method_enum = method_enum.video
       
        # 初始化人脸识别器
        self.recog = cv.face.LBPHFaceRecognizer_create()
        # 所有的人脸id
        self.face_ids = []
        self.face_arr = []
        # 人脸名字
        self.face_names = ["unknow"]
        self.face_name = None
        # 数据路径
        self.data_path = DATA_PATH
        self.face_id = 1
    # 自定义文件路径
    def select_model_path(self, path:str):
        if path is None or not path.endswith('yaml'):
            return '自定义路径有误，请重新选择'
        self.recog_path = path
        
    def catch_method_change(self, method: method_enum):
        self.catch_method = method
        
    def set_face_name(self, face_name):
        self.face_name = face_name
        
    def test_method_change(self, method: method_enum):
        self.test_method = method
        
    # 初始化模型
    def init_model(self):
        if self.recog is None:
            return "模型路径有误"
        # 有模型就加载
        print(self.recog_path)
        self.recog.read(self.recog_path)
        print('模型初始化成功')
    # 训练模型
    def train_model(self):
        self.recog.train(self.face_arr, np.array(self.face_ids))
        # 保存模型
        self.recog.save(self.recog_path)
        self.face_id += 1
        print(self.face_id)
        print(self.face_names)
        
    # 获取所有训练数据
    def get_all_imgs_labels(self):
        for user_id in os.listdir(self.data_path):
            face_id = user_id.split('.')[1]
            self.get_imgs_labels(face_id)
            
    # 添加训练数据
    def get_imgs_labels(self):
        
        if self.face_name is None:
            return False
        # 判断是否有数据
        if self.face_id in self.face_ids:
            return '已有该人脸数据'
        elif self.face_name in self.face_names:
            return '人脸名称已存在'
        image_path = os.path.join(self.data_path, 'user.' + self.face_id)
        for path in os.listdir(image_path):
            img = cv.imread(path, 0)
            self.face_arr.append(img)
            self.face_ids.append(self.face_id)
    def add_train_data(self, img):
        self.face_arr.append(img)
        self.face_ids.append(self.face_id)
    # 获取人脸数据，默认八百张图片，实验可到最好效果
    def check_face(self, face_name):
        
        if face_name == "" or face_name in self.face_names:
            return False
        self.face_names.append(face_name)
        return self.face_id
    
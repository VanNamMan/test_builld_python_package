import cv2
import numpy as np
import logging
logging.basicConfig(format='%(message)s',
                    level=logging.DEBUG)

class Webcam():
    def __init__(self) -> None:
        self._camera:cv2.VideoCapture = None
        self._is_open = False

    def open(self, source) -> bool:
        '''
        @params
        @source: int or str
            - int: index of camera
            - str: rtsp stream link of camera
        return bool
        '''
        error = ""
        self._is_open = False
        try:
            self._camera = cv2.VideoCapture(source, cv2.CAP_DSHOW)
        except Exception as ex:
            error = str(ex)
            logging.error(error)
    
        if not error:
            logging.info("Camera open sucess")
            self._is_open = True
        else:            
            self._camera = None

        return self._is_open

    def close(self) -> bool:
        try:
            self._camera.release()
            logging.info("Camera closed")
            return True
        except Exception as ex:
            error = str(ex) 
            logging.error(error)
            return False

    def grab(self) -> np.ndarray:
        ret, mat = self._camera.read()
        if ret:
            return mat
        else:
            return None

    def get_camera(self):
        return self._camera
    
    def is_open(self):
        return self._is_open

    @staticmethod
    def get_devices() -> dict:
        dict_devives = {}
        return dict_devives
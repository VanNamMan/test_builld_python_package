# Installation
    1.Clone responsitory
    2.Extract folder
    3.cd folder
    4.pip install - e .
# Camera
## Basler
Using open Basler camera.
Reference [pypylon master](https://github.com/basler/pypylon).

    -Example:
        from connections.basler import Basler
        # init camera
        camera = Basler()
        # open camera by index 0
        camera.open(0)
        # open camera by serinumber
        # camera.open('serinumber_here')
        # grab image
        mat = camera.grab()
        print(mat.shape)
        # close camera
        camera.close()
## Webcam
Using open Webcam or RTSP camera.
Reference [opencv video capture](https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html).

    -Example:
        from connections.webcam import Webcam
        # init camera
        camera = Webcam()
        # open camera by index 0
        camera.open(0)
        # open camera by rtsp
        # camera.open('rtsp_link_here')
        # grab image
        mat = camera.grab()
        print(mat.shape)
        # close camera
        camera.close()
# Socket utils
# Logger
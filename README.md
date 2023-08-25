# Installation
1.Clone responsitory [Github page](https://github.com/VanNamMan/test_builld_python_package)\

2.Extract folder\
3.cd folder\
4.pip install -e .\
# Camera
## Basler
Using open Basler camera
Reference [pypylon master](https://github.com/basler/pypylon)

    from connections import Basler
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
Using open Webcam or RTSP camera\
Reference [opencv video capture](https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html)

    from connections import Webcam
    # init camera
    camera = Webcam()

    # open camera by rtsp
    # camera.open('rtsp_link_here')
    # open camera by index 0
    camera.open(0)

    # grab image
    mat = camera.grab()
    print(mat.shape)

    # close camera
    camera.close()
# Socket utils
Some function help send image(numpy array) or text over socket client and server

    import socket
    import numpy as np
    from connections.socket_utils import send_text, send_image

    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect(("localhost", 5000))

    # send text with length with format: {lenth}:text:{your_text}
    # ex client send "Hello", server revcieve "5:text:Hello"
    msg = time.strftime("Client sent %H:%M:%S\n")
    send_text(sk, msg)

    # send array with length with format: {lenth}:image:{your_array_encode}
    mat = np.random.radnint(0, 256, (640, 480, 3))
    send_image(sk, mat)
# Logger
Custom logger\
Reference [Logger console with color](https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output)\
Reference [Logging CookBook](https://docs.python.org/3/howto/logging-cookbook.html)

    from connections import Logger
    logger = Logger(name="mylog", 
                file_name="logfile.log", 
                file_level=logging.INFO,
                stream_level=logging.INFO)
    logger.info("this is info")
    logger.warning("this is warning")
    logger.error("this is error")
    logger.critical("this is critical")


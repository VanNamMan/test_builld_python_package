# Installation
    1.Clone responsitory
    2.Extract folder
    3.cd folder
    4.pip install - e .
# Camera
## Basler
1.Reference [pypylon master](https://github.com/basler/pypylon).
2.Example:
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
# Socket utils
# Logger
# Installation
    1.Clone responsitory
    2.Extract folder
    3.cd folder
    4.pip install - e .
# Camera
## Basler
    1.Example:
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

    2.Reference
        1.[pypylon-master](https://github.com/basler/pypylon)
## Webcam
# Socket utils
# Logger
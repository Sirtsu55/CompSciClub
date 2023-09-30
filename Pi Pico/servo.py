from ServoController import ServoController
import time
sg90 = ServoController(11, 0.55, 2.6, 180)

sg90.ContinuousRotate()

time.sleep(2)

sg90.Relax()








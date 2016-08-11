from ppm_decoder import Decoder
import pyb

ppm = Decoder('X1')
while True:
    a = ppm.get_channel_value(0)
    b = ppm.get_channel_value(1)
    c = ppm.get_channel_value(2)
    d = ppm.get_channel_value(3)
    pyb.delay(50)

    print("1: %s \t 2: %s \t 3: %s \t 4: %s" %(a, b, c, d))
